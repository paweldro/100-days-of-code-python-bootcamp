import requests
from twilio.rest import Client
import os

my_city = os.environ.get("my_city")
api_key = os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
to_number = os.environ.get("to_number")

parameters_geo = {
    "q": my_city,
    "appid": api_key,
}

response_geo = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=parameters_geo)
response_geo.raise_for_status()
data_geo = response_geo.json()
parameters_weather = {
    "lat": data_geo[0]["lat"],
    "lon": data_geo[0]["lon"],
    "cnt": 4,
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters_weather)
response.raise_for_status()
data_weather = response.json()

will_rain = False
for x in data_weather["list"]:
    condition_code = x["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_='+13342768078',
            to=to_number
        )
    print(message.status)
