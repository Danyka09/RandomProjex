#import functions_framework
import requests
import os
#weather
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def nasa():
    #gets images,explanation and title from a nasa api
    try:
        nasa_api = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        nasa_json = nasa_api.json()
        image_url = nasa_json.get('url')
        explanation_text = nasa_json.get('explanation')
        title = nasa_json.get('title')
        return image_url, explanation_text, title
    except Exception as e:
        return  "https://as2.ftcdn.net/v2/jpg/02/51/95/53/1000_F_251955356_FAQH0U1y1TZw3ZcdPGybwUkH90a3VAhb.jpg", f"API is unavailable because {e}", "Nasa probably got hit by a meteor"

def cat_facts():
    #gets cat facts
    try:
        cat_facts_api = requests.get("https://meowfacts.herokuapp.com/")
        cat_facts_json = cat_facts_api.json()
        return cat_facts_json['data'][0]
    except Exception as e:
        return f"The api is currently down :( /n Error code:{e}"

def fox_pics():
    #gets pictures of foxes
    try:
        fox_pics_api = requests.get("https://randomfox.ca/floof/")
        fox_pics_json = fox_pics_api.json()
        fox_pic =  fox_pics_json.get('image')
        return fox_pic
    except Exception as e:
        return f"No foxes right now :( /n Error code:{e}"

def weather():
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.5939,
        "longitude": 20.6745,
        "hourly": ["temperature_2m", "apparent_temperature", "precipitation"],
        "current": ["is_day", "weather_code"],
        "timezone": "Europe/Berlin",
        "forecast_days": 1,
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    # Process current data. The order of variables needs to be the same as requested.
    current = response.Current()
    current_is_day = current.Variables(0).Value()
    current_weather_code = current.Variables(1).Value()

    print(f"\nCurrent time: {current.Time()}")
    print(f"Current is_day: {current_is_day}")
    print(f"Current weather_code: {current_weather_code}")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_apparent_temperature = hourly.Variables(1).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time() + response.UtcOffsetSeconds(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd() + response.UtcOffsetSeconds(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )}

    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["apparent_temperature"] = hourly_apparent_temperature
    hourly_data["precipitation"] = hourly_precipitation

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    print("\nHourly data\n", hourly_dataframe)

    filename = weather_icon.get(current_weather_code, "/0.png")
    icon_url = f"{github_url}{filename}"
    return hourly_temperature_2m[7], hourly_temperature_2m[10], icon_url

#def weather_test():

def email():
    #email looks and sending
    image_url, explanation_text, title = nasa()
    cat_fact = cat_facts()
    fox = fox_pics()
    weather_temp7, weather_temp10, icon_url = weather()
    HOST = "smtp.gmail.com"
    PORT = 587

    FROM_EMAIL = "dsebo09@gmail.com"
    TO_EMAIL = "dsebo09@gmail.com"
    PASSWORD = os.getenv('GOOGLE_PW')

    message = MIMEMultipart("alternative")
    message['Subject'] = "Daily Report"
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL

    html = f"""
    <html>
        <body>
            <h1>Daily Report</h1>
            <h2>NASA Image: {title}</h2>
            <img src="{image_url}" alt="NASA APOD" style="max-width: 100%; border-radius: 10px;">
            <p> {explanation_text}
            <h2> Cat fact:</h2>
            <p>{cat_fact}</p>
            <h2> FOX!!! </h2>
            <img src="{fox}">
            <table border="2">
                <tr>
                    <td>{weather_temp7:.2f}°C</td>
                    <td>{weather_temp10:.2f}°C</td>
                    <td>
                        <img src="{icon_url}" alt="Weather icon" style="width: 50px; height: auto;">
                    </td>
                </tr>
            </table>
            <p></p>
        </body>
    </html>
    """

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

#this delete when put on google
email()
#@functions_framework.http
#def handler(request):
#    try:
#        email()
#        return "Email sent successfully!", 200
#    except Exception as e:
#        return f"Error: {str(e)}", 500