# 🛡️ Guardian Edge: Instant Hazard Alert for Two-Wheelers via NICLA Vision

Guardian Edge is a real-time fall and jerk detection system designed for two-wheeler riders.  
It uses **dual IMU data** — one from an **Arduino Nicla Vision mounted on the helmet**, and another from a **mobile phone** — to instantly detect hazardous motions like **falls or sudden jerks** during rides.

---

## 🚀 Project Overview

Every second counts in accidents — and early hazard detection can save lives.  
Guardian Edge aims to bring **intelligent safety assistance** to bikers by combining on-device sensor data with lightweight ML models for immediate feedback.

This project focuses on:

- Collecting **IMU data** (accelerometer and gyroscope) from the rider’s helmet and smartphone.
- Predicting **falls** and **jerks** in real-time.
- Enabling **instant alerts** or automated responses through the Arduino Nicla Vision.

---

## 🧠 Workflow

1. **Data Collection**
   - Recorded IMU data from both sources during:
     - Normal riding sessions
     - Controlled falling/jerking simulations
   - Synced data via timestamp alignment for multi-sensor coherence.

2. **Exploratory Data Analysis (EDA)**
   - Visualized motion patterns for different activities.
   - Compared helmet and mobile sensor readings to identify distinctive features for hazardous events.
   - Filtered noise and handled outliers to improve signal reliability.

3. **Feature Engineering**
   - Derived new metrics like acceleration magnitude, jerk rate, orientation shifts, and angular velocity.
   - Built a meaningful feature set representing dynamic motion states.

4. **Modeling**
   - Trained and compared **Decision Tree** and **Neural Network** models.
   - Decision Tree provided interpretability, while the NN improved adaptability to subtle jerks.

5. **Training & Inference**
   - Split dataset into training and test sets for performance validation.
   - Achieved effective detection accuracy for fall and jerk classification.
   - Deployed trained models for **on-device inference** using Arduino Nicla Vision.

---

## ⚙️ Tech Stack

| Component | Description |
|------------|-------------|
| **Hardware** | Arduino Nicla Vision, Android smartphone |
| **Sensors** | IMU (Accelerometer + Gyroscope) |
| **Languages** | Python, MicroPython|
| **ML Frameworks** | PyTorch / Scikit-learn |
| **Data Processing** | NumPy, Pandas, Matplotlib |
| **Deployment** | Arduino IDE, Edge ML tools |

---

## 📊 Results

- Reliable detection of falls and jerks during real-world testing.
- Dual-sensor approach improved motion context understanding.
- Lightweight design suitable for **real-time edge deployment**.

---

## 🧩 Future Enhancements

- Integrate GPS for automatic location-based alerting.
- Add cloud backup for continuous ride monitoring.
- Optimize neural model for even lower latency on embedded hardware.

---

## 👨‍💻 Author

**Manas Kumar Mishra**
**Adarsh Dubey**
**Animesh Kumar**
**Abhijeet Kumar**
**Varshan P A**
---

> *Guardian Edge — because safety should always ride with you.*

