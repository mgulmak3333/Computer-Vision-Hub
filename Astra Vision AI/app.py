from collections import Counter
import numpy as np
from PIL import Image
import streamlit as st
from ultralytics import YOLO

st.title("Astra Vision AI")


@st.cache_resource
def load_model():
  
  return YOLO("astra_vision.pt")


model = load_model()

file = st.file_uploader(
    "Upload a satellite image", type=["jpg", "jpeg", "png"]
)

if file:
  img = np.array(Image.open(file).convert("RGB"))

  result = model(img)[0]

  
  st.image(result.plot())

  
  if result.obb is not None and len(result.obb) > 0:
    
    classes = [model.names[int(c)] for c in result.obb.cls]
    counts = Counter(classes)

    st.success(f"Total Detected Objects: {len(classes)}")
    st.subheader("Detected Objects")

    for name, count in counts.items():
      st.write(f"**{name}:** {count}")
  else:
    st.warning("No objects were detected in the image.")