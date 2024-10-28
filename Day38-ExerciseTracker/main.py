import requests
from datetime import datetime
import os

today = datetime.now()
post_date = today.strftime("%d/%m/%Y")
post_time = today.strftime("%H:%M:%S")


workout = input("What exercise did you do today?\n")

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST_ENDPOINT = os.environ["SHEETY_POST_ENDPOINT"]

NUTRITIONIX_PARAMS = {
    "query": workout
}

NUTRITIONIX_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

SHEETY_header = {
    "Authorization": f"Bearer {os.environ["BEARER_TOKEN"]}"
}

with requests.post(url=NUTRITIONIX_ENDPOINT, json=NUTRITIONIX_PARAMS, headers=NUTRITIONIX_header) as response:
    response.raise_for_status()
    exercises = response.json()["exercises"]

for exercise in exercises:
    temp_json = {
        "workout": {
            "date": post_date,
            "time": post_time,
            "exercise": exercise["name"].capitalize(),
            "duration": str(exercise["duration_min"]),
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_POST_ENDPOINT, json=temp_json, headers=SHEETY_header)
    print(response)
