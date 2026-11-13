import requests

# 1. Define the URL of your local FastAPI endpoint
url = "http://127.0.0.1:8005/predict-balance"

# 2. Set up the test payload with your input features
payload = {
    "global_active_power": 3.5,
    "voltage": 230.0,
    "global_intensity": 15.0,
    "solar_ac_power": 2.1
}

try:
    # 3. Send a POST request with JSON data
    response = requests.post(url, json=payload)
    
    # 4. Check if the request was successful
    if response.status_code == 200:
        print("✅ Success! Server Response:")
        print(response.json())
    else:
        print(f"⚠️ Error {response.status_code}:")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("❌ Could not connect to the server. Make sure your Uvicorn server is running!")