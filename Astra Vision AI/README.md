# 🛰️ Astra Vision AI
### Satellite Imagery Instance Segmentation with YOLO26

Astra Vision AI is a Computer Vision project focused on detecting and segmenting objects in high-resolution satellite imagery using deep learning.

Built with **YOLO26 Small Segmentation (YOLO26s-seg)**, the model identifies and generates segmentation masks for various aerial objects, including aircraft, ships, harbors, bridges, and ground vehicles.

The project also includes a custom **Streamlit web application** that allows users to upload satellite images and visualize the model's segmentation results through an interactive interface.

---

## 📌 Project Overview

| Category | Details |
|---|---|
| Project Name | Astra Vision AI |
| Task | Instance Segmentation |
| Model | YOLO26 Small Segmentation |
| Framework | Ultralytics YOLO |
| Dataset | iSAID Dataset |
| Dataset Size | Approximately 22 GB |
| Training Duration | Approximately 6 Hours |
| Application | Streamlit |
| Inference | Image Upload |

---

## 🧠 Model & Training

The model was trained using the **iSAID (Instance Segmentation in Aerial Images) Dataset**, a large-scale dataset containing aerial images with pixel-level object annotations.

**Dataset:** [iSAID Dataset – YOLO11 Segmentation Format](https://www.kaggle.com/datasets/redzapdos123/isaid-dataset-yolo11-seg-format)

- **Dataset Size:** Approximately 22 GB
- **Architecture:** YOLO26 Small Segmentation
- **Training Duration:** Approximately 6 hours
- **Task:** Multi-class Instance Segmentation

The training process was particularly challenging due to the dataset's size and computational requirements. Processing approximately 22 GB of annotated satellite imagery pushed the limits of the available hardware and resulted in several unsuccessful training attempts.

After multiple experiments and adjustments, I successfully completed a training run and obtained a functional segmentation model.

### Model Performance & Limitations

Although the model is capable of identifying and segmenting important aerial objects, its performance is not yet perfect.

- It can successfully detect and segment several types of objects in satellite imagery.
- It may occasionally miss smaller objects, especially in densely populated scenes.
- Segmentation quality can vary depending on image resolution, object size, and scene complexity.

The current model is a working implementation and a foundation for further optimization and experimentation.

---

## 🖥️ Application Preview

The project includes a Streamlit interface for testing the trained model without manually writing inference code.

The application allows users to upload satellite images and visualize the predicted segmentation masks.

![Astra Vision AI Inference Demo](img4.png)

*Example output demonstrating that the trained model successfully processes an image and generates segmentation results.*

---

## ⚙️ Installation & Setup

Follow the steps below to run Astra Vision AI locally.

### 1. Clone the Repository

```bash
git clone https://github.com/mgulmak3333/Computer-Vision-Hub.git
```

Navigate to the project directory:

```bash
cd Computer-Vision-Hub/Astra-Vision-AI
```

*Make sure the folder name matches the actual directory name in your repository. If it contains spaces, use its exact name.*

### 2. Install Dependencies

All required Python libraries are listed in the `requirements.txt` file.

Install them using:

```bash
pip install -r requirements.txt
```

### 3. Verify the Project Files

Make sure the required files and directories are in place:

```text
Astra Vision AI/
│
├── app.py
├── requirements.txt
├── astra_vision.pt
├── README.md
│
├── test/
│   ├── 1.png
│   ├── 2.png
│   └── ...
│
└── img4.png
```

**Important:** The trained model weights (`astra_vision.pt`) must be present in the project directory because the application loads this file during startup.

The `test/` directory contains sample satellite images that can be used to try out the model.

---

## 🚀 Running the Application

Once the dependencies are installed and the model weights are in the correct directory, start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will launch the application in your default browser.

### How to Test the Model

1. Launch the application using the command above.
2. Open the Streamlit interface.
3. Upload a satellite image.
4. Select one of the sample images available in the `test/` directory.
5. Wait for the model to process the image.
6. Examine the resulting segmentation masks.

You can also upload your own satellite images to experiment with the model.

---

## 📁 Project Structure

```text
Astra Vision AI/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Required Python libraries
├── astra_vision.pt       # Trained YOLO26s segmentation model
├── README.md             # Project documentation
│
├── test/                  # Sample images for testing
│
└── img4.png               # Example inference result
```

---

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Ultralytics YOLO** – Object detection and instance segmentation
- **YOLO26s-seg** – Trained segmentation architecture
- **Streamlit** – Interactive web application
- **NumPy** – Numerical operations
- **Pillow (PIL)** – Image loading and processing

---

## 🔭 Future Improvements

Potential directions for further development include:

- Improving the detection of small objects in dense satellite scenes.
- Experimenting with higher-resolution inference.
- Optimizing segmentation accuracy and inference speed.
- Expanding the testing process with additional satellite imagery.
- Exploring image slicing techniques for detecting smaller aerial targets.

---

## 👨‍💻 Developer

**Developed by Musa Gülmak**

[GitHub Profile](https://github.com/mgulmak3333) · [Computer Vision Hub](https://github.com/mgulmak3333/Computer-Vision-Hub)

Part of my personal Computer Vision and Deep Learning portfolio.
