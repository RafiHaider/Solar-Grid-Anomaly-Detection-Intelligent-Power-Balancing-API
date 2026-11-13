
from fastapi import FastAPI
import joblib
import pandas as pd
import warnings
from pydantic import BaseModel

# Suppress sklearn feature names warning globally inside the app
warnings.filterwarnings("ignore", category=UserWarning)

app = FastAPI(title="Solar-Grid Load Balancing & Energy Anomaly Predictor")

model = joblib.load('anomaly_model.pkl')
scaler = joblib.load('scaler.pkl')

class EnergyInput(BaseModel):
    global_active_power: float
    voltage: float
    global_intensity: float
    solar_ac_power: float

@app.post("/predict-balance")
def predict_energy_balance(data: EnergyInput):
    features_df = pd.DataFrame([[data.global_active_power, data.voltage, data.global_intensity]], 
                               columns=['Global_active_power', 'Voltage', 'Global_intensity'])
    
    scaled_features = scaler.transform(features_df)
    prediction = model.predict(scaled_features)[0]
    is_anomaly = 1 if prediction == -1 else 0
    
    solar_kw = data.solar_ac_power / 1000.0
    net_demand = data.global_active_power - solar_kw
    
    if net_demand > 0:
        action = "Draw from Grid & Solar"
    else:
        action = "Feed Excess Solar to Battery/Grid"
        
    return {
        "is_anomaly": bool(is_anomaly),
        "net_power_demand_kw": round(net_demand, 3),
        "recommended_action": action,
        "status": "Warning: Power Spike Detected!" if is_anomaly else "System Operating Normally"
    }
