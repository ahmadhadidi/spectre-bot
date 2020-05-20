import logging
import requests
import discord
from common import message_splitter
from os import getenv


# This function for now is for testing purposes to see if OpenWeatherMaps works.
def weather(message):
    # TODO: See why logging doesn't work when I am running the program with or without debug in python
    logging.info("[!] Received a message containing weather")

    print("[+] Received a message containing weather!")

    APIKEY = getenv("OpenWeatherMapsApiKey")  # https://home.openweathermap.org/api_keys

    # remove !weather from the message
    city = message_splitter(message, True)

    # Resource: https://openweathermap.org/current#name
    unknown_city_url = getenv("OpenWeatherMapsURL")

    # We concatenate the url and the parameters
    complete_url = unknown_city_url + "q=" + city + "&appid=" + APIKEY + "&units=metric"

    # We send the request as a POST.
    r = requests.post(url=complete_url)

    # We save the response as a JSON object in the variable response.
    response = r.json()
    print("[+] Sent URL to OWM is: {0}".format(complete_url))

    # Check if the city inputted is correct
    if response['cod'] == 200:
        print(response) # city is correct so we expect the JSON object to contain weather data.
    else:
        print("City not found. Please make sure that your command is like this: \"-weather Amman\"")

    # TODO: The response gives us an icon, we can map the value of the icon to an emoji.
    # https://openweathermap.org/weather-conditions

    # Example Response
    # {
    #   'coord': {'lon': 35.95, 'lat': 31.96},
    #   'weather':
    #       [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
    #   'base': 'stations',
    #   'main':
    #       {
    #           'temp': 22.39, 'feels_like': 15.94, 'temp_min': 22, 'temp_max': 23, 'pressure': 1013, 'humidity': 33
    #       },
    #   'visibility': 10000,
    #   'wind':
    #       {
    #           'speed': 7.7, 'deg': 280
    #       },
    #   'clouds':
    #       {
    #           'all': 1
    #       },
    #   'dt': 1588349686,
    #   'sys':
    #       {
    #           'type': 1, 'id': 7520, 'country': 'JO', 'sunrise': 1588301403, 'sunset': 1588349778},
    #           'timezone': 10800, 'id': 250441, 'name': 'Amman', 'cod': 200
    #       }
    
    response_temp = response['main']['temp'] # 18.44
    response_humidity = response['main']['humidity'] #40 (we have to add %)
    response_city = response['name'] # Amman, Siegen
    response_weather = response['weather'][0]['main'] # Clear / Raining etc.
    response_desc = response['weather'][0]['description'] # clear sky
    
    # Join the weather and the temperature together
    title =  str(response_temp) + "° \t\t " + response_weather

    # Create an embed object and fill it with the data that we need
    embed_weather = discord.Embed(title=title, description=response_desc.title(), color=0x00ff00)
    embed_weather.add_field(name="Humidity", value=(str(response_humidity)+"%"), inline=True)
    embed_weather.add_field(name="City", value=response_city, inline=True)
    
    return embed_weather
