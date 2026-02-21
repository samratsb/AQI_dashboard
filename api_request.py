import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("secrets.env") 

def fetch_data():
    print("Fetch Data")
    try:

        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            raise ValueError("API_KEY not found in environment")

        params = {
            "access_key": API_KEY,
            "query": "New Delhi"
        }

        url = "http://api.weatherstack.com/current"
        
        response = requests.get(url, params=params, timeout=100)
        
        # if response.status_code == 429:
        #     raise Exception("Rate limit exceeded. Please wait before retrying.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        response.raise_for_status() #raises exception for 400, 500 http errors
        print("API response received successfully.")
        return response.json() 
    
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise  # Re-raise the exception to signal failure


# def mock_fetch_data():
#     return {
#     "request": {
#         "type": "City",
#         "query": "New York, United States of America",
#         "language": "en",
#         "unit": "m"
#     },
#     "location": {
#         "name": "New York",
#         "country": "United States of America",
#         "region": "New York",
#         "lat": "40.714",
#         "lon": "-74.006",
#         "timezone_id": "America/New_York",
#         "localtime": "2019-09-07 08:14",
#         "localtime_epoch": 1567844040,
#         "utc_offset": "-4.0"
#     },
#     "current": {
#         "observation_time": "12:14 PM",
#         "temperature": 13,
#         "weather_code": 113,
#         "weather_icons": [
#             "https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
#         ],
#         "weather_descriptions": [
#             "Sunny"
#         ],
#         "astro": {
#             "sunrise": "06:31 AM",
#             "sunset": "05:47 PM",
#             "moonrise": "06:56 AM",
#             "moonset": "06:47 PM",
#             "moon_phase": "Waxing Crescent",
#             "moon_illumination": 0
#         },
#         "air_quality": {
#             "co": "468.05",
#             "no2": "32.005",
#             "o3": "55",
#             "so2": "7.4",
#             "pm2_5": "6.66",
#             "pm10": "6.66",
#             "us-epa-index": "1",
#             "gb-defra-index": "1"
#         },
#         "wind_speed": 0,
#         "wind_degree": 349,
#         "wind_dir": "N",
#         "pressure": 1010,
#         "precip": 0,
#         "humidity": 90,
#         "cloudcover": 0,
#         "feelslike": 13,
#         "uv_index": 4,
#         "visibility": 16
#     }
# }


