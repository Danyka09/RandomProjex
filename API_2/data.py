import requests
import os
from datetime import date
#weather
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email():
    HOST = "smtp.gmail.com"
    PORT = 587

    FROM_EMAIL = ""
    TO_EMAIL = ""
    PASSWORD = ""

    message = MIMEMultipart("alternative")
    message['Subject'] = ""
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL

html=

    html_part =  MIMEText(html, 'html')
    message.attach(html_part)
    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
    smtp.quit()

github_url = "https://raw.githubusercontent.com/Danyka09/weather-icons_meshosk/refs/heads/main/icons/png"
weather_icon = {
# Standard WMO Weather interpretation codes
    0: "/0.png",   # Clear sky
    1: "/1.png",   # Mainly clear
    2: "/2.png",   # Partly cloudy
    3: "/3.png",   # Overcast
    45: "/45.png", # Fog
    48: "/48.png", # Depositing rime fog
    51: "/51.png", # Drizzle: Light intensity
    53: "/53.png", # Drizzle: Moderate intensity
    55: "/55.png", # Drizzle: Dense intensity
    61: "/61.png", # Rain: Slight intensity
    63: "/63.png", # Rain: Moderate intensity
    65: "/65.png", # Rain: Heavy intensity
    71: "/71.png", # Snow fall: Slight intensity
    73: "/73.png", # Snow fall: Moderate intensity
    75: "/75.png", # Snow fall: Heavy intensity
    80: "/80.png", # Rain showers: Slight
    81: "/81.png", # Rain showers: Moderate
    82: "/82.png", # Rain showers: Violent
    95: "/95.png", # Thunderstorm: Slight or moderate
    96: "/96.png", # Thunderstorm with slight hail
    99: "/99.png"  # Thunderstorm with heavy hail
}
#import functions_framework

# https://open-meteo.com/en/docs
# https://open.er-api.com/v6/latest/USD - make it reverse so its eur per usd, czk and huf
# https://github.com/r-spacex/SpaceX-API/tree/master/docs#rspacex-api-docs
# http://api.open-notify.org/iss-now.json - geopy