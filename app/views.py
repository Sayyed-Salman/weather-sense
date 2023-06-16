from flask import render_template, request, redirect, url_for, flash, make_response, render_template_string
from flask import Blueprint
from .weather_stuff import get_weather, get_cityname_from_coordinates


home = Blueprint('home', __name__)

coordinates = {}


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/location', methods=['POST'])
def receive_location():
    location_data = request.get_json()
    latitude = location_data['latitude']
    longitude = location_data['longitude']

    city = get_cityname_from_coordinates(latitude, longitude)
    coordinates[city] = f"{latitude}, {longitude}"
    response = make_response('OK', 200)
    return response


@home.route('/weather/<coordinates>')
def show_weather(coordinates):
    latitude, longitude = coordinates.split(",")
    city_name = get_cityname_from_coordinates(latitude, longitude)
    curr_weather = get_weather(latitude, longitude)
    return render_template('showWeather.html', current_weather=curr_weather, cityname=city_name)


@home.route('/share')
def share_tweet():
    city_name = "Berlin"
    tweet = f"https://twitter.com/intent/tweet?text=Check%20out%20the%20weather%20in%20{city_name}%20here:%20{url_for('home.show_weather', coordinates='52.5200,13.4050', _external=True)}"

    newtweet = f"https://twitter.com/intent/tweet?text=Stay%20ahead%20of%20the%20weather%20with%20WeatherSense%21%20Get%20real-time%20updates%20and%20accurate%20forecasts%20for%20your%20location.%20Try%20it%20now%20and%20be%20weather-savvy%21%20%F0%9F%8C%A4%20{url_for('home.show_weather', coordinates='52.5200,13.4050', _external=True)}"

    return redirect(newtweet)
