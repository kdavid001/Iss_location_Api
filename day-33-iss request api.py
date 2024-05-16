import json
import time

import requests
from datetime import datetime
import smtplib

location = requests.get(url="http://api.open-notify.org/iss-now.json")
location = location.json()

# for covenant University
my_latitude = 6.524379
my_longitude = 3.379206

parameter = {
    "lng": my_longitude,
    "lat": my_latitude,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
results = response.json()
now = datetime.now()

# ISS Position
iss_latitude = float(location["iss_position"]["latitude"])
iss_longitude = float((location["iss_position"]["longitude"])
                      )

sunrise = int(results["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(results["results"]["sunset"].split("T")[1].split(":")[0])
now = now.hour

iss_string1 = str(iss_longitude)
iss_string2 = str(iss_latitude)


def iss_position():
    time.sleep(60)
    if (my_longitude - 5 <= iss_longitude <= my_longitude + 5) and (my_latitude - 5 <= iss_latitude <= my_latitude + 5):
        if now >= sunset or now <= sunrise:
            my_email = "feranmidavid427@gmail.com"
            password = 'mtoc rvfk mume umln'
            with open('message.txt', 'r') as file:
                file_contents = file.read()
            replacements = {
                'longitude': iss_string1,
                'latitude': iss_string2, }

            for old_text, new_text in replacements.items():
                file_contents = file_contents.replace(old_text, new_text)

            with open('message.txt', 'w') as file:
                file.write(file_contents)
            with open('message.txt', 'r') as message_file:
                message = message_file.read()
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="korededavid03@gmail.com",
                                    msg=f"Subject: Random Quote\n\n{message}")


iss_position()

# This code is currently not running you can run it on pythoneverywhere website
