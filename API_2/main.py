import functools

import numpy as np
import requests
import os
from datetime import date
from pathlib import Path
#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#weather
import requests_cache
from retry_requests import retry
import openmeteo_requests
import pandas as pd
#AI USAGE: json nested dictionaries after 2h; path error resolved with an r (though it worked fine without too); html variables is like half, i read it out of documentation i just asked ai cause i thought there was a way but there wasnt so i did the other way;
github_url = "https://raw.githubusercontent.com/Danyka09/weather-icons_meshosk/refs/heads/main/icons/png/"
weather_icon = {
# Standard WMO Weather interpretation codes
    0: "0.png",   # Clear sky
    1: "1.png",   # Mainly clear
    2: "2.png",   # Partly cloudy
    3: "3.png",   # Overcast
    45: "45.png", # Fog
    48: "48.png", # Depositing rime fog
    51: "51.png", # Drizzle: Light intensity
    53: "53.png", # Drizzle: Moderate intensity
    55: "55.png", # Drizzle: Dense intensity
    61: "61.png", # Rain: Slight intensity
    63: "63.png", # Rain: Moderate intensity
    65: "65.png", # Rain: Heavy intensity
    71: "71.png", # Snow fall: Slight intensity
    73: "73.png", # Snow fall: Moderate intensity
    75: "75.png", # Snow fall: Heavy intensity
    80: "80.png", # Rain showers: Slight
    81: "81.png", # Rain showers: Moderate
    82: "82.png", # Rain showers: Violent
    95: "95.png", # Thunderstorm: Slight or moderate
    96: "96.png", # Thunderstorm with slight hail
    99: "99.png"  # Thunderstorm with heavy hail
}

def error_handling(basefn):
    @functools.wraps(basefn)
    def wrapper(*args, **kwargs): # the args and the kwargs are for the parameters just in case
        try:
            result = basefn(*args, **kwargs) # we put it into a variable and return it
            print(f"The {basefn} ran successfully!")
            return result
        except Exception as e:
            print(f"Error CODE: {e}")
    return wrapper # DONT PUT THE () HERE

@error_handling
def spacex_api():
    spacex_api = requests.get("https://api.spacexdata.com/v5/launches/latest")
    spacex_json = spacex_api.json()
    spacex_img = spacex_json['links']['patch']['small']
    spacex_landing = spacex_json['cores'][0]['landing_success']
    spacex_video = spacex_json['links']['webcast']

    if spacex_landing == True:
        spacex_landing_message = "The rocket had landed successfully! 😀"
    else:
        spacex_landing_message = "The rocket had not landed successfully. 🙁"

    return spacex_img, spacex_landing_message, spacex_video
    #if it returns{dic [list {dic we need to do the index of the list  print(json.dumps(spacex_json, indent=4))
    #if we wanna use the json module instead
        # test_txt = spacex_api.text
        # test_json = json.loads(test_txt)
        # print(test_json)

@error_handling
def iss_api():
    iss_api = requests.get("http://api.open-notify.org/iss-now.json")
    iss_json = iss_api.json()
    iss_longitude = iss_json['iss_position']['longitude']
    iss_latitude = iss_json['iss_position']['latitude']
    return iss_longitude, iss_latitude

@error_handling
def currency_api():
    currency_api = requests.get("https://open.er-api.com/v6/latest/USD")
    currency_json = currency_api.json()
    # the exchange rates from USD
    usd_eur = currency_json['rates']['EUR'] #REMEMBER THIS FOR THE REST OF FUCKING TIME; NESTED DICTIONARIES JSON, ALSO STRINGS!
    usd_czk = currency_json['rates']['CZK']
    usd_huf = currency_json['rates']['HUF']
    # the logic to make it from EUR
    eur_usd = 1/usd_eur
    eur_czk = usd_czk*eur_usd
    eur_huf = usd_huf*eur_usd
    # making it be 2 decimal places
    usd = f"{eur_usd:.2f}"
    czk = f"{eur_czk:.2f}"
    huf = f"{eur_huf:.2f}"
    # print(f"USD to EUR:{usd_eur}; to CZK:{usd_czk}; to HUF:{usd_huf}\nEUR to USD:{eur_usd}; to CZK:{eur_czk}, to HUF:{eur_huf}")
    return usd, czk, huf

# okay so [] is for REACHING/GRABBING stuff. no matter whether its a list, ()-touple (indexes); or dic. if i wanna go nested we first go into the parent one with the first [] and the one within that with another [] and so on
# () this is for actions or orders; also tuples
# {} making dic. or sets(sets are unique items only no duplicates and unordered so no index)

@error_handling
def weather_api():
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.5939,
        "longitude": 20.6745,
        "hourly": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "precipitation", "weather_code"],
        "timezone": "Europe/Berlin",
        "forecast_days": 1,
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    # print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    # print(f"Elevation: {response.Elevation()} m asl")
    # print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
    # print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
    hourly_apparent_temperature = hourly.Variables(2).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(3).ValuesAsNumpy()
    hourly_weather_code = hourly.Variables(4).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        end =  pd.to_datetime(hourly.TimeEnd() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}

    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
    hourly_data["apparent_temperature"] = hourly_apparent_temperature
    hourly_data["precipitation"] = hourly_precipitation
    hourly_data["weather_code"] = hourly_weather_code

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    # print("\nHourly data\n", hourly_dataframe)
    # print(hourly_precipitation)
    # print(hourly_relative_humidity_2m)
    # print(hourly_apparent_temperature)
    # print(hourly_temperature_2m)
    # print(hourly_weather_code)

    ######################## so like this stuff is unnecesary but atleast i learnt
    # temp = []
    # feel_temp = []
    # precitipation = []
    # humidity = []
    # code = []
    #
    # for x in hourly_temperature_2m: # x is each item in the list and after in is the actual list so x is index 0, 1, 2 etc after every loop. and then we convert to a float and append it to a new list thats outside the loop the store the data
    #     tempature = float(x)
    #     temp.append(tempature) # can also do temp.append(float(x))
    #
    # for x in hourly_apparent_temperature:
    #     tempature = float(x)
    #     feel_temp.append(tempature)
    #
    # for x in hourly_precipitation:
    #     y = float(x)
    #     precitipation.append(y)
    #
    # for x in hourly_relative_humidity_2m:
    #     y = float(x)
    #     humidity.append(y)
    #
    # for x in hourly_weather_code:
    #     y = int(x)
    #     code.append(y)

    #basically what the ai did first time but no i got it myself (claude helped with understanding loops but this is me 🦾 (also with .mean)
    row_07_09 = [float(np.mean(hourly_temperature_2m[7:10])),
                 float(np.mean(hourly_apparent_temperature[7:10])),
                 float(np.mean(hourly_precipitation[7:10])),
                 float(np.mean(hourly_relative_humidity_2m[7:10])),
                 github_url + weather_icon[hourly_weather_code[8]]]

    row_10_13 = [float(np.mean(hourly_temperature_2m[10:14])), # ALT + J for multiple select
                 float(np.mean(hourly_apparent_temperature[10:14])),
                 float(np.mean(hourly_precipitation[10:14])),
                 float(np.mean(hourly_relative_humidity_2m[10:14])),
                 f"{github_url}{weather_icon[int(hourly_weather_code[12])]}"]

    row_14_16 = [float(np.mean(hourly_temperature_2m[14:17])),
                 float(np.mean(hourly_apparent_temperature[14:17])),
                 float(np.mean(hourly_precipitation[14:17])),
                 float(np.mean(hourly_relative_humidity_2m[14:17])),
                 f"{github_url}{weather_icon[hourly_weather_code[15]]}"]

    row_17_20 = [float(np.mean(hourly_temperature_2m[17:21])),
                 float(np.mean(hourly_apparent_temperature[17:21])),
                 float(np.mean(hourly_precipitation[17:21])),
                 float(np.mean(hourly_relative_humidity_2m[17:21])),
                 github_url + weather_icon[hourly_weather_code[18]]]

    return row_07_09, row_10_13, row_14_16, row_17_20

@error_handling
def email():
    spacex_img = spacex_api()[0]
    spacex_landing_message = spacex_api()[1]
    spacex_video = spacex_api()[2]

    w7, w10, w14, w17 = weather_api()

    iss_longitude, iss_latitude = iss_api()

    usd, czk, huf = currency_api()

    HOST = "smtp.gmail.com"
    PORT = 587

    FROM_EMAIL = "dsebo09@gmail.com"
    TO_EMAIL = "dsebo09@gmail.com"
    PASSWORD = os.getenv("GOOGLE_PW")

    message = MIMEMultipart("alternative")
    message['Subject'] = f"{date.today()}"
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL

    html_path= Path(r"C:\Users\dsebo\Desktop\Google Backup\coding\python\RandomProjex\API_2\html.html")

    #use r so that it treats it as plain text cause \ mean stuff in python like \n ...
    html = (html_path.read_text()).format(img = spacex_img, message = spacex_landing_message, video = spacex_video, long = iss_longitude, lat = iss_latitude, usd = usd, czk = czk, huf = huf, w7 = w7, w10 = w10, w14 = w14, w17 = w17)
    # since we are reading the html from outside we cant use an f string, so we use .format() and add the variables as an argument and in the html it still goes in the {curly brackets}, this has the benefit of being able to change the var to something more simple ig.      to format the decimals we just do it in the html file directly

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

email()