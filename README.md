# Guardian Edge: Instant Hazard Alert for Two-Wheelers via NICLA Vision

Guardian Edge is a real-time hazard detection system designed to enhance rider safety for two-wheelers. By leveraging the **Arduino Nicla Vision** and machine learning models, this project detects sudden falls and jerks during rides — enabling instant alerts to prevent accidents and ensure timely assistance.

---

## 🚀 Project Overview

Two-wheeler riders face frequent risks of falling or losing balance due to poor roads or sudden movements. **Guardian Edge** captures motion data and analyzes it in real-time to predict hazard events such as **falling** or **jerking**. 

The core idea is to process IMU (Inertial Measurement Unit) and camera data locally on **Nicla Vision**, perform on-device inference, and alert the user or connected system when an anomaly (fall/jerk) is detected.

---

## 🧩 Key Features

- Real-time detection of falls and jerks.  
- Machine learning–based classification using **Decision Tree** and **Neural Network models**.  
- Edge inference support using **Arduino Nicla Vision**.  
- Lightweight and power-efficient design for two-wheeler integration.  

---

## 🧠 Workflow

### 1. Data Collection
- Collected sensor data from **riding** and **falling scenarios** using the onboard sensors of Nicla Vision.  
- Captured accelerometer, gyroscope, and camera input during various motion states.  

### 2. Exploratory Data Analysis (EDA)
- Visualized motion data trends for normal and abnormal events.  
- Identified distinct patterns in acceleration and angular velocity during falls.  
- Filtered noise and normalized sensor readings.  

### 3. Feature Engineering
- Extracted statistical and temporal features (mean, standard deviation, peaks, energy, etc.).  
- Computed derived metrics like jerk magnitude and motion vector variance.  

### 4. Model Development
- Applied classical ML and deep learning models:
  - **Decision Tree Classifier** for baseline interpretability.  
  - **Neural Network** for improved generalization and performance.  
- Trained both models to classify states: *normal riding*, *jerk detected*, *fall detected*.

### 5. Training and Inference
- Split dataset into training and test sets.  
- Optimized hyperparameters and validated performance.  
- Deployed trained model on Nicla Vision for **real-time hazard inference**.  

---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Hardware | Arduino Nicla Vision |
| Language | Python, C++ |
| ML Tools | scikit-learn, TensorFlow / Keras |
| Data Processing | NumPy, Pandas, Matplotlib |
| Deployment | Arduino IDE, Edge Impulse / TensorFlow Lite |

---

## 📊 Results
- Achieved accurate classification between normal and abnormal riding states.  
- Demonstrated real-time alerting capability during tests.  
- Compact model fits within on-device resource constraints.  

---

## 🔄 Future Improvements
- Add GPS and connectivity features for automatic emergency alerts.  
- Integrate camera-based scene awareness for road hazard context.  
- Extend to detection of other risky ride behaviors (e.g., collisions, skidding).

---

Feel free to reach out for collaboration or technical discussion!

