
import streamlit as st
from ultralytics import YOLO
from collections import Counter
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Astra Vision AI", layout="wide")
st.title("Astra Vision AI")

@st.cache_resource
def load_model():
    return YOLO("astra_vision.pt")

model = load_model()

file = st.file_uploader("Upload a satellite image", type=["jpg", "jpeg", "png"])

if file:
    img = np.array(Image.open(file).convert("RGB"))
    result = model(img, augment=True)[0]

    if result.masks is not None:
        masks = result.masks.data.cpu().numpy()

        segmentation = np.zeros(img.shape[:2], dtype=np.float32)

        for mask in masks:
            mask = cv2.resize(
                mask.astype(np.float32),
                (img.shape[1], img.shape[0])
            )
            segmentation = np.maximum(segmentation, mask)

      
        activation = cv2.GaussianBlur(
            segmentation, (0, 0), sigmaX=25
        )

        activation = cv2.normalize(
            activation, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        
        heatmap = cv2.applyColorMap(
            activation, cv2.COLORMAP_JET
        )

        heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

        
        output = cv2.addWeighted(
            img, 0.70, heatmap, 0.30, 0
        )

        st.subheader("Segmentation Heatmap")
        st.image(output, width=550)

    else:
        st.warning("No segmentation detected.")

    
    if result.boxes is not None and len(result.boxes) > 0:
        classes = [model.names[int(c)] for c in result.boxes.cls]
        counts = Counter(classes)

        st.success(f"Total Detected Objects: {len(classes)}")
        st.subheader("Detected Objects")

        for name, count in counts.items():
            st.write(f"**{name}:** {count}")
    else:
        st.info("No objects detected.")
