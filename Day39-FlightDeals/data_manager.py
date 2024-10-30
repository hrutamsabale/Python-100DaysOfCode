import requests
from flight_search import FlightSearch

SHEETY_SHEET_ENDPOINT = "[Your Sheety Endpoint here]"
SHEETY_HEADER = {
    "Authorization": f"Bearer {"YOUR_TOKEN_HERE"}"
}


class DataManager:

    def get_flight_data(self):
        with requests.get(url=SHEETY_SHEET_ENDPOINT, headers=SHEETY_HEADER) as response:
            data = response.json()
        return data

    def format_wish_data(self):
        data = self.get_flight_data()["prices"]
        to_return = []
        for item in data:
            temp = {
                "start": "LON",
                "stop": item["iataCode"],
                "max_price": item["lowestPrice"]
            }
            to_return.append(temp)
        return to_return

    def update_codes(self):
        flights = (self.get_flight_data())['prices']
        for i in range(2, len(flights)+2):
            update_endpoint = f"[YOUR_UPDATE_ENDPOINT_URL_HERE]/{i}"
            city = flights[i-2]["city"]
            fs = FlightSearch()
            city_code = fs.get_city_code(city)
            temp_params = {
                "price": {
                    "iataCode": city_code
                }
            }
            requests.put(url=update_endpoint, json=temp_params, headers=SHEETY_HEADER)

