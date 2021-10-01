"""uses the OpenWeatherMap api to get weather"""

import json
import requests

def get_weather() -> dict :
    """Uses the OpenWeatherMap Api to get the weather from a certain city

    returns the tempertur in celcius,
    what it feels like,
    and a description"""

    #opening the config file
    with open("config.json","r") as f:
        json_file = json.load(f)

    #getting the components to construct the url
    weather_section = json_file["weather"]
    weather_key = weather_section["api-key"]
    base_url = weather_section["base_url"]
    city = weather_section["city"]

    complete_url = base_url + "appid=" + weather_key + "&q=" + city
    response = requests.get(complete_url)

    #making the restful api call
    x = response.json()
    return x


if __name__ == "__main__":
    print(get_weather())
