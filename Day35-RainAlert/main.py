import requests
from twilio.rest import Client


API_KEY = "[Your OWM API Key here]"
MY_LAT = 18.520430
MY_LON = 73.856743
account_sid = '[Your account sid here]'
auth_token = '[Your twilio auth token here]'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4
}

with requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters) as response:
    response.raise_for_status()
    data = response.json()

will_rain = False
for item in data["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='[Your messaging service if here]',
        body='Bring an umbrella☂️ It might rain.',
        to='[Receiver\'s contact here]'
    )
    print(message.status)
