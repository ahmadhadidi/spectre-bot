import requests
import discord
import os
from common import message_splitter


# This function replies with the corona virus statistics to the discord user
def corona(message):
    # Remove -corona from the message
    country = message_splitter(message, True)

    # Obtain the api url
    corona_url = os.getenv("corona_url")

    # Bind the corona logo URL
    corona_logo = "https://www.dresden.de/media/bilder/gesundheit/GA/Corona_CDC-AlissaEckert_23311.jpg"

    # Concatenate the country that the user requested with the api url
    corona_url = corona_url + country

    print('Corona URL is: {0}'.format(corona_url))

    # We send the request as a POST.
    r = requests.get(url=corona_url)

    # Check if the country inputted is correct
    if r.status_code == 200:
        print(r)  # city is correct so we expect the JSON object to contain weather data.
    else:
        print("Country not found. Please make sure that your command is like this: \"-corona Jordan\"")

    # We save the response as a JSON object in the variable response.
    response = r.json()

    # We get the last and the penultimate item in the response
    last_day = response[len(response) - 1]
    previous_day = response[len(response)-2]

    # Bind the data that we need into variables for the last day in the list
    last_day_date = last_day['Date'][:10]  # [:10] means get the first 10 chars
    last_day_confirmed = last_day['Confirmed']
    last_day_active = last_day['Active']
    last_day_deaths = last_day['Deaths']

    # Bind the data that we need into variables for the day before the last day in the list
    previous_day_date = previous_day['Date'][:10]  # [:10] means get the first 10 chars
    previous_day_confirmed = previous_day['Confirmed']
    previous_day_active = previous_day['Active']
    previous_day_deaths = previous_day['Deaths']

    # Calculate the difference between each variable (except date)
    diff_confirmed = last_day_confirmed - previous_day_confirmed
    diff_active = last_day_active - previous_day_active
    diff_deaths = last_day_deaths - previous_day_deaths

    # Prepare the string that goes into the value of each field to show the value and the difference
    val_last_day_confirmed = "{0} ({1})".format(last_day_confirmed, diff_confirmed)
    val_last_day_active = "{0} ({1})".format(last_day_active, diff_active)
    val_last_day_death = "{0} ({1})".format(last_day_deaths, diff_deaths)

    # Create an embed object and fill it with the data that we need
    embed_corona = discord.Embed(title="Corona Stats in {0}".format(country.title()), color=0xB03130)
    embed_corona.set_thumbnail(url=corona_logo)

    embed_corona.add_field(name="Yesterday", value=str(last_day_date), inline=False)
    embed_corona.add_field(name="Confirmed", value=val_last_day_confirmed, inline=True)
    embed_corona.add_field(name="Active", value=val_last_day_active, inline=True)
    embed_corona.add_field(name="Deaths", value=val_last_day_death, inline=True)

    embed_corona.add_field(name="Before Yesterday", value=str(previous_day_date), inline=False)
    embed_corona.add_field(name="Confirmed", value=str(previous_day_confirmed), inline=True)
    embed_corona.add_field(name="Active", value=str(previous_day_active), inline=True)
    embed_corona.add_field(name="Deaths", value=str(previous_day_deaths), inline=True)

    embed_corona.set_footer(text="Data from CovidAPI")

    # Journal: An attempt to scrape the moh.gov.jo corona website
    #          It is really unfriendly to scrape, so I used the
    #          CovidAPI instead.
    # extract the text attribute from the script element
    # variable_holder = script_holder[0].text
    # https://corona.moh.gov.jo/en
    # open dev console -> choose 'en' -> scroll to line # 507 -> have fun.
    # corona_page.xpath('//script/text()')

    return embed_corona
