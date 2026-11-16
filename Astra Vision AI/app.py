import streamlit as st
from ultralytics import YOLO
from collections import Counter
from PIL import Image
import numpy as np

st.title("Astra Vision AI")

@st.cache_resource
def load_model():
    return YOLO("astra_vision.pt")

model = load_model()

file = st.file_uploader("Upload a satellite image", type=["jpg", "jpeg", "png"])

if file:
    img = np.array(Image.open(file).convert("RGB"))
    result = model(img, augment=True)[0]

    st.image(result.plot(boxes=False))

    classes = [model.names[int(c)] for c in result.boxes.cls]
    counts = Counter(classes)

    st.success(f"Total Detected Objects: {len(classes)}")
    st.subheader("Detected Objects")

    for name, count in counts.items():
        st.write(f"**{name}:** {count}")