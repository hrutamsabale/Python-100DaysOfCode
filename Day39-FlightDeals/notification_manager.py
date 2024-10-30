import requests
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "[YOUR_ACCOUNT_SID_HERE]"

TWILIO_AUTH_TOKEN = "[YOUR_AUTH_TOKEN_HERE]"

TWILIO_SERVICE_ID = "[YOUR_SERVICE_ID_HERE]"

RECEIVER = "[RECEIVER'S_NUMBER_HERE]"

class NotificationManager:
    def send_notification(self, flight_details):
        start = flight_details["from"]
        stop = flight_details["to"]
        departure = flight_details["departure"]
        arrival = flight_details["arrival"]
        price = flight_details["price"]
        msg = f"DEAL FOUND!\n\nFlight from {start} to {stop} on {departure}. Return at {arrival}. At only ${price}"
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            messaging_service_sid=TWILIO_SERVICE_ID,
            body=msg,
            to=RECEIVER
        )
