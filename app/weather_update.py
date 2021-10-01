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

    if x["cod"] != "404":
        y = x["main"]
        temp_kelvin = y["temp"]
        temp_celcius = round(float(temp_kelvin) - 273.15, 2)
        feels_like_kelvin = y["feels_like"]
        feels_like_celcius = round(float(feels_like_kelvin) - 273.15, 2)
        z = x["weather"]
        weather_description = z[0]["description"]

        #the title that will be displayed with the notification
        weather_title = str("The weather in " + city + ":")

        #the content that will be displayed on the notification
        weather_content = str(" Temperature: " + str(temp_celcius) +
                "\n Feels like: " + str(feels_like_celcius) +
                "\n Description: " + str(weather_description) )

        #making the dictionary
        weather_data = {"title":"","content":""}
        weather_data.update({"title": weather_title})
        weather_data.update({"content": weather_content } )

        #returning the dictionary
        return weather_data

if __name__ == "__main__":
    print(get_weather())
