# 👁️ Computer Vision Hub

A collection of my Computer Vision projects covering **Instance Segmentation**, **Object Detection**, and **Image Classification**. Almost all architectures, training pipelines, and Streamlit web interfaces in this repository were written and built from scratch.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)]()
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)]()

---

## 📂 Folders

* **`Astra Vision AI/`** — Satellite Imagery Segmentation
* **`Chess Vision AI/`** — Real-Time Chess Piece Detection
* **`Brain Tumor AI - VGG Style/`** — Custom CNN Classification (Built from Scratch)
* **`Brain Tumor AI - EfficientNetB0/`** — Transfer Learning Classification

*(Setup guides and run commands are located inside each project folder.)*

---

## 🚀 Projects & Visual Demos

### 1. 🛰️ Astra Vision AI (Satellite Segmentation)
Segments and detects objects like airplanes, ships, harbors, and vehicles from satellite imagery at the pixel level. While not a heavy commercial model, it successfully handles real-world aerial detection tasks.

* **Task:** Instance Segmentation
* **Dataset:** [iSAID Dataset (YOLO Format)](https://www.kaggle.com/datasets/redzapdos123/isaid-dataset-yolo11-seg-format)

![Astra Vision Demo](Astra Vision AI/img4.png)

---

### 2. ♟️ Chess Vision AI (Object Detection)
Detects, classifies, and counts all white and black chess pieces in real time. Supports both static images and video streams via a Streamlit interface.

* **Task:** Object Detection
* **Dataset:** [Chess Pieces Detection Dataset](https://www.kaggle.com/datasets/imtkaggleteam/chess-pieces-detection-image-dataset)

![Chess Vision Demo](assets/chess_demo.png)

---

### 3. 🧠 Brain Tumor AI (Classification — Two Approaches)
Two different neural networks trained on the same brain MRI dataset to compare custom model building against transfer learning:

* **VGG Style (`Brain Tumor AI - VGG Style/`):** A custom VGG-inspired CNN architecture I wrote from scratch without using pre-trained weights.
* **EfficientNetB0 (`Brain Tumor AI - EfficientNetB0/`):** Uses transfer learning for fast training and high classification accuracy.
* **Dataset:** [Brain Tumor MRI Data](https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data)

| Custom VGG-Style CNN | EfficientNetB0 |
| :---: | :---: |
| ![VGG Demo](assets/brain_vgg_demo.png) | ![EfficientNet Demo](assets/brain_eff_demo.png) |

---

## 🛠️ Main Tools Used
`Python` • `PyTorch` • `TensorFlow / Keras` • `Ultralytics YOLO` • `OpenCV` • `Streamlit`

---

**Developed by Musa Gülmak** ([@mgulmak3333](https://github.com/mgulmak3333)) — Licensed under [Apache 2.0](LICENSE)
