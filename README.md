# ☀️ Solar Grid Anomaly Detection & Intelligent Power Balancing API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.162.6-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)]()

An enterprise-grade, high-performance machine learning backend engineered to monitor smart solar microgrids in real time. This system ingests live telemetry parameters, detects electrical anomalies using an unsupervised **Isolation Forest** model, and automatically computes optimal power balancing recommendations.

---

## 🚀 Key Features

* **Real-Time Telemetry Analysis:** Instantly processes key grid metrics (`global_active_power`, `voltage`, `global_intensity`, and `solar_ac_power`).
* **Unsupervised Outlier Detection:** Utilizes a pre-trained **Isolation Forest** machine learning model coupled with robust feature scalers (`joblib`).
* **Intelligent Power Balancing:** Automatically routes energy demands, calculating net power deficits/surpluses and issuing actionable grid recommendations.
* **Production-Ready FastAPI Backend:** Features automated request validation using Pydantic schemas and interactive Swagger UI documentation (`/docs`).
* **Rigorous Testing Suites:** Verified via automated Pytest validation pipelines and custom client integration test scripts (`test_api.py`).

---

## 📂 Project Architecture

```text
solar_grid_deployment/
│
├── main.py              # FastAPI application & prediction endpoint routing
├── anomaly_model.pkl    # Pre-trained Isolation Forest ML model
├── scaler.pkl           # Feature normalization scaler
├── test_api.py          # Automated client testing script
└── requirements.txt     # Project dependencies
```
## 🛠️ Tech Stack
* **Framework:** FastAPI, Uvicorn (ASGI Server)
* **Machine Learning:** Scikit-Learn, Joblib, NumPy, Pandas, SciPy
* **Validation & Documentation:** Pydantic, Swagger UI / OpenAPI

---

## ⚙️ Quick Start & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/RafiHaider04/solar_grid_deployment.git](https://github.com/RafiHaider04/solar_grid_deployment.git)
cd solar_grid_deployment
```
### 2. Install Dependencies
```bash
python -m pip install fastapi uvicorn joblib pandas scikit-learn
```
### 3. Launch the Server
```bash
python -m uvicorn main:app --reload --port 8005
```
The server will start locally at http://127.0.0.1:8005

## 🧪 Testing the API

### Option A: Interactive Browser UI
Navigate to http://127.0.0.1:8005/docs to test payloads directly via the built-in Swagger UI

### Option B: Automated Python Client (test_api.py)
Run the verification script in a separate terminal window:
```bash
python test_api.py
```
## Sample Request Payload:
```JSON
{
  "global_active_power": 3.5,
  "voltage": 230.0,
  "global_intensity": 15.0,
  "solar_ac_power": 2.1
}
```
## Sample JSON Response:
```JSON
{
  "is_anomaly": false,
  "net_power_demand_kw": 3.498,
  "recommended_action": "Draw from Grid & Solar",
  "status": "System Operating Normally"
}
```
## 👤 Author
### **Rafi Haider**
* **Registration No: 04102313004**
* **AI Academic Coursework**
