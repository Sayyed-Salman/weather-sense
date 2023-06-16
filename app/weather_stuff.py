import requests
import geopy
from datetime import datetime

weather_codes = {
    0: 'Clear sky',
    1: 'Mainly clear',
    2: 'Partly cloudy',
    3: 'Overcast',
    45: 'Fog and depositing rime fog',
    48: 'Fog and depositing rime fog',
    51: 'Drizzle: Light intensity',
    53: 'Drizzle: Moderate intensity',
    55: 'Drizzle: Dense intensity',
    56: 'Freezing Drizzle: Light intensity',
    57: 'Freezing Drizzle: Dense intensity',
    61: 'Rain: Slight intensity',
    63: 'Rain: Moderate intensity',
    65: 'Rain: Heavy intensity',
    66: 'Freezing Rain: Light intensity',
    67: 'Freezing Rain: Heavy intensity',
    71: 'Snowfall: Slight intensity',
    73: 'Snowfall: Moderate intensity',
    75: 'Snowfall: Heavy intensity',
    77: 'Snow grains',
    80: 'Rain showers: Slight intensity',
    81: 'Rain showers: Moderate intensity',
    82: 'Rain showers: Violent intensity',
    85: 'Snow showers: Slight intensity',
    86: 'Snow showers: Heavy intensity',
    95: 'Thunderstorm: Slight intensity',
    96: 'Thunderstorm: Slight hail',
    99: 'Thunderstorm: Heavy hail'
}

emoji_mapping = {
    'Clear sky': '☀️',
    'Mainly clear': '🌤️',
    'Partly cloudy': '⛅',
    'Overcast': '☁️',
    'Fog and depositing rime fog': '🌫️',
    'Drizzle: Light intensity': '🌦️',
    'Drizzle: Moderate intensity': '🌦️',
    'Drizzle: Dense intensity': '🌧️',
    'Freezing Drizzle: Light intensity': '🌧️❄️',
    'Freezing Drizzle: Dense intensity': '🌧️❄️',
    'Rain: Slight intensity': '🌧️',
    'Rain: Moderate intensity': '🌧️',
    'Rain: Heavy intensity': '🌧️☔',
    'Freezing Rain: Light intensity': '🌧️❄️☔',
    'Freezing Rain: Heavy intensity': '🌧️❄️☔',
    'Snowfall: Slight intensity': '🌨️',
    'Snowfall: Moderate intensity': '🌨️',
    'Snowfall: Heavy intensity': '🌨️❄️',
    'Snow grains': '🌨️',
    'Rain showers: Slight intensity': '🌧️',
    'Rain showers: Moderate intensity': '🌧️',
    'Rain showers: Violent intensity': '⛈️',
    'Snow showers: Slight intensity': '🌨️',
    'Snow showers: Heavy intensity': '🌨️❄️',
    'Thunderstorm: Slight intensity': '⛈️',
    'Thunderstorm: Slight hail': '⛈️',
    'Thunderstorm: Heavy hail': '⛈️'
}

emoji_representation = {
    0: "☀️",
    1: "🌤️",
    2: "⛅",
    3: "☁️",
    45: "🌫️",
    48: "🌫️",
    51: "🌦️",
    53: "🌦️",
    55: "🌧️",
    56: "🌧️❄️",
    57: "🌧️❄️",
    61: "🌧️",
    63: "🌧️",
    65: "🌧️☔",
    66: "🌧️❄️☔",
    67: "🌧️❄️☔",
    71: "🌨️",
    73: "🌨️",
    75: "🌨️❄️",
    77: "🌨️",
    80: "🌧️",
    81: "🌧️",
    82: "⛈️",
    85: "🌨️",
    86: "🌨️❄️",
    95: "⛈️",
    96: "⛈️",
    99: "⛈️",
}

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"


def convert_timestamp(timestamp):
    """Return the timestamp in a readable format."""
    date_time_obj = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M")
    hours_minutes = date_time_obj.strftime("%H:%M")
    date_ = date_time_obj.strftime("%d/%m/%Y")
    return {"hours_minutes": hours_minutes, "date": date_}


def get_weather(latitude, longitude):
    """Return the weather."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m,weathercode&forecast_days=3"

    response = requests.get(url)
    data = response.json()

    # list of timestamps
    raw_time_stamp = data['hourly']["time"]
    time_stamp = [convert_timestamp(timestamp) for timestamp in raw_time_stamp]
    temperature = data['hourly']['temperature_2m']
    weather_code_ = data['hourly']['weathercode']
    weather_description = [get_description(code) for code in weather_code_]
    emojis = [emoji_representation[code] for code in weather_code_]

    curr_weather = zip(time_stamp, temperature, weather_description, emojis)

    return curr_weather


def get_local_timezone_from_coordinates(latitude, longitude):
    pass


def get_description(weather_code):
    """Return the description of the weather code."""
    return weather_codes[weather_code]


def get_cityname_from_coordinates(latitude, longitude) -> str:
    """Return the city name from the coordinates."""
    geolocator = geopy.Nominatim(user_agent="weather_app")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    city = location.raw['address']['city']
    print(city)
    return city
