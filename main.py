from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this if needed for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


API_KEY = "195a81c4ff0a4968bea171847232912"
BASE_URL = "https://api.weatherapi.com/v1/current.json"


class CityRequest(BaseModel):
    city: str

@app.post("/get_weather")
async def get_weather(request: CityRequest):
    city = request.city
    url = f"{BASE_URL}?key={API_KEY}&q={city}"

   
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return {"error": "City not found"}

    
    temp_celsius = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    feels_like = data["current"]["feelslike_c"]

    return {
        "temperature": temp_celsius,
        "humidity": humidity,
        "feels_like": feels_like
    }
