# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.


import flight_search, flight_data, data_manager, notification_manager

datamanager = data_manager.DataManager()
flightsearch = flight_search.FlightSearch()
flightdata = flight_data.FlightData()
notifier = notification_manager.NotificationManager()

for item in datamanager.format_wish_data():
    flightdata.flight_data.extend(flightsearch.search_flight(item["start"], item["stop"], item["max_price"]))

print(flightdata.flight_data)

for item in flightdata.flight_data:
    notifier.send_notification(item)


