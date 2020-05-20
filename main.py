import discord
from dotenv import load_dotenv
from rasa_nlu_api import query_rasa
from weather import weather
from royaa_news import royaa_news
from fuel_prices import fuel
from corona import corona

token = 'NzAzNDA1MjU3MDgyMDExNjcw.XqtJIA.QOzgLwTxL1_ES04o8z5EWU9Y5Nw'
client = discord.Client()

load_dotenv(verbose=True)

@client.event
async def on_ready():
    print('Ready to talk to bot')


@client.event
async def on_message(message):

    print(f"{message.author}, {message.content}")

    # Enable rudimentary commands to display the API calls.
    if str(message.content).startswith('-'):

        if str(message.content).startswith('-news'):
            news = royaa_news()
            await message.channel.send(embed=news)

        if str(message.content).startswith('-weather'):
            weather_response = weather(message.content)
            await message.channel.send(embed=weather_response)

        if str(message.content).startswith('-fuel'):
            fuel_response = fuel(message.content)
            await message.channel.send(embed=fuel_response)

        if str(message.content).startswith('-corona'):
            corona_response = corona(message.content)
            await message.channel.send(embed=corona_response)

    # Make Rasa calls by writing a message that starts with '!'
    if str(message.content).startswith('!'):
        checkMessage = query_rasa(message.content, True)
        if message.author == client.user:
            return

        # check confidence here
        await message.channel.send(checkMessage)

client.run(token)
