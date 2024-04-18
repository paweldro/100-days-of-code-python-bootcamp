import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 80.513982  # Your latitude
MY_LONG = 55.109476  # Your longitude


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    return hour_now >= sunset or hour_now <= sunrise


def is_iss_over_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5


my_email = "your@mail.com"
password = "yourpassword"

while True:
    time.sleep(60)
    if is_night() and is_iss_over_me():
        with smtplib.SMTP("your-smtp") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="addressee@mail.com",
                                msg="Subject:Look up!\n\nThe ISS is above you in the sky.")
