import requests
import flight_data
from pprint import pprint
import datetime

AMADEUS_FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/shopping/flight-offers"

AMADEUS_TOKEN = "[YOUR_TOKEN_HERE]"

AMADEUS_CITY_CODE_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

AMADEUS_HEADER = {
    "Authorization": f"Bearer {AMADEUS_TOKEN}"
}


class FlightSearch:

    def get_city_code(self, city):
        city_code_params = {
            "keyword": city,
            "max": 1
        }
        response = requests.get(url=AMADEUS_CITY_CODE_ENDPOINT, params=city_code_params, headers=AMADEUS_HEADER)
        return (response.json())['data'][0]['iataCode']

    def search_flight(self, start, stop, max_price):
        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        i = 0
        to_return = []
        while i < 4:
            begin = datetime.datetime.now()
            check = begin + datetime.timedelta(days=i)
            date = check.strftime("%Y-%m-%d")
            search_params = {
                "originLocationCode": start,
                "destinationLocationCode": stop,
                "departureDate": date,
                "adults": 1,
                "maxPrice": max_price,
                "max": 1,
                "nonStop": True
            }
            response = requests.get(url=endpoint, params=search_params, headers=AMADEUS_HEADER)
            try:
                temp = len(response.json()["data"])
            except:
                pass
            else:
                if temp != 0:
                    temp1 = {
                        "from": (response.json())["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                        "to": (response.json())["data"][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                        "departure": date,
                        "arrival": ((response.json())["data"][0]["itineraries"][0]["segments"][0]["arrival"]["at"].split("T"))[0],
                        "price": (response.json())["data"][0]["price"]["total"]
                    }
                    to_return.append(temp1)
                i += 1

        return to_return





