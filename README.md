![Banner](Computer%20Vision%20Hub.png)

# 👁️ Computer Vision Hub

A personal collection of end-to-end Computer Vision and Deep Learning projects, exploring the intersection of intelligent systems, visual perception, and real-world applications.

This repository brings together my hands-on work across Object Detection, Oriented Object Detection (OBB), and Medical Image Classification. Each project represents a different technical challenge, where I experiment with model architectures, develop custom training pipelines, optimize inference workflows, and build interactive AI applications.

My approach goes beyond simply training existing models. I focus on understanding the underlying architectures, implementing custom solutions from scratch, experimenting with different deep learning techniques, and turning trained models into practical applications.

Built through experimentation, problem-solving, and continuous learning.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)]()
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)]()

---

## 📂 Repository Structure

- **`Astra Vision AI/`** — High-Resolution Satellite Imagery Segmentation
- **`Chess Vision AI/`** — Real-Time Chess Piece Object Detection (Image & Video)
- **`Brain Tumor AI - VGG Style/`** — Custom CNN Architecture Built from Scratch
- **`Brain Tumor AI - EfficientNetB0/`** — Transfer Learning Benchmark Model

*(Individual installation steps, model weights, and run commands are documented inside each project folder.)*

---

## 🚀 Projects, Engineering Notes & Visual Demos

### 1. 🛰️ Astra Vision AI — *Satellite Imagery Object Detection (OBB)*

Detects and localizes aerial objects—such as airplanes, ships, harbors, bridges, and ground vehicles—from top-down satellite and aerial imagery using oriented bounding boxes. By predicting rotated bounding boxes, the model can accurately represent objects regardless of their orientation in the image.

- **Architecture:** YOLO26 Small OBB
- **Task:** Oriented Object Detection (OBB)
- **Dataset:** [DOTA v1.5 Dataset](https://platform.ultralytics.com/ultralytics/datasets/dotav1-5)
- **Training Platform:** Ultralytics Platform

- **Key Features:** Detects multiple object categories in complex satellite imagery and uses rotated bounding boxes to represent the position, angle, and orientation of detected objects more precisely than conventional horizontal bounding boxes.

**Engineering Story & Highlights:** Developing Astra Vision AI allowed me to explore oriented object detection in large-scale satellite imagery. One of the main advantages of this approach is its ability to handle objects positioned at different angles, making it particularly suitable for aerial images where vehicles, ships, and aircraft rarely follow a consistent orientation. The trained model demonstrates strong detection capabilities across various satellite imagery scenarios, successfully identifying and localizing objects with rotated bounding boxes.

![Astra Vision Demo](Astra%20Vision%20AI/img4.png)

---

### 2. ♟️ Chess Vision AI — *Real-Time Chess Piece Detection*
A multi-class object detection system built to localize, classify, and count all white and black chess pieces in real time. Deployed with a custom **Streamlit** web app that supports both static image inference (with Test-Time Augmentation) and live frame-by-frame video analysis.

- **Task:** Object Detection (12+ Piece Classes)
- **Dataset:** [Chess Pieces Detection Dataset](https://www.kaggle.com/datasets/imtkaggleteam/chess-pieces-detection-image-dataset)

![Chess Vision Demo](Chess%20Vision%20AI/img3.png)

---

### 3. 🧠 Brain Tumor AI — *Comparative MRI Classification*
To explore the trade-offs between building neural networks from the ground up versus leveraging pre-trained backbones, I trained two distinct architectures on the same brain MRI dataset:

- **VGG Style (`Brain Tumor AI - VGG Style/`):** A custom VGG-inspired Convolutional Neural Network (CNN) whose layers and training pipeline I coded completely from scratch without relying on pre-trained weights.
- **EfficientNetB0 (`Brain Tumor AI - EfficientNetB0/`):** A transfer learning implementation utilizing compound scaling to achieve fast convergence and strong diagnostic accuracy.
- **Dataset:** [Brain Tumor MRI Data](https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data)

| Custom VGG-Style CNN (From Scratch) | EfficientNetB0 (Transfer Learning) |
| :---: | :---: |
| ![VGG Demo](Brain%20Tumor%20AI%20-%20VGG%20Style/img2.png) | ![EfficientNet Demo](Brain%20Tumor%20AI%20-%20EfficientNetB0/img1.png) |

---

## 🛠️ Tech Stack

`Python` • `PyTorch` • `TensorFlow / Keras` • `Ultralytics YOLO` • `OpenCV` • `Streamlit` • `NumPy & PIL`

---

**Developed by Musa Gülmak** ([@mgulmak3333](https://github.com/mgulmak3333)) — Licensed under [Apache 2.0](LICENSE)
