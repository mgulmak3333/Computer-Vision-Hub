import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

st.title("Brain Tumor AI - VGG Style CNN")

model = load_model("brain_tumor_model.h5")

classes = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

image = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png"])

if image:
    img = load_img(image, target_size=(224, 224))
    st.image(img)

    img = np.expand_dims(img_to_array(img), axis=0)

    predictions = model.predict(img)
    result = np.argmax(predictions)

    possibility = np.max(predictions) * 100

    st.success(f"Class: {classes[result]}")
    st.write(f"Possibility: %{possibility:.2f}")
