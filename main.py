import discord
from dotenv import load_dotenv
from rasa_nlu_api import query_rasa
from weather import weather
from royaa_news import royaa_news
from fuel_prices import fuel
from corona import corona
from os import getenv


# load the .env file
load_dotenv(verbose=True)

# obtain the discord bot token and save it into a variable
token = getenv("DiscordBotToken")

# bind the client object into the variable client
client = discord.Client()

# once the bot is ready it will say this message in the console
@client.event
async def on_ready():
    print('Ready to talk to bot')


# this is where the magic happens, on_message is like a listener for each
# message someone sends into discord
@client.event
async def on_message(message):

    # for debugging, we can see what the user said here
    print(f"{message.author}, {message.content}")

    # Enable rudimentary commands to display the API calls.
    if str(message.content).startswith('-'):

        # Check the news via an RSS parser
        if str(message.content).startswith('-news'):
            news = royaa_news()
            await message.channel.send(embed=news)

        # Check the weather via JSON, requires a city with the message, 
        # e.g., -weather frankfurt
        if str(message.content).startswith('-weather'):
            weather_response = weather(message.content)
            await message.channel.send(embed=weather_response)

        # Check the fuel prices in Jordan by webscraping
        if str(message.content).startswith('-fuel'):
            fuel_response = fuel(message.content)
            await message.channel.send(embed=fuel_response)

        # Check the corona cases, requires a country, e.g., -corona sweden
        if str(message.content).startswith('-corona'):
            corona_response = corona(message.content)
            await message.channel.send(embed=corona_response)

    # Make Rasa calls by writing a message that starts with '!'
    # To run rasa, do `python .\rasa_folder\run_rasa.py` 
    # with venv enabled, in terminal of course.
    if str(message.content).startswith('!'):
        checkMessage = query_rasa(message.content, True)
        
        # This if statement prevents rasa from talking with itsself.
        # It is not necessary since we have startswith('!') but
        # we might need it later on.
        if message.author == client.user:
            return

        # Send the message from rasa to discord
        await message.channel.send(checkMessage)

client.run(token)
