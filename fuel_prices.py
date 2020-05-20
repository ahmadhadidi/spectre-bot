from lxml import html
import requests
import discord
import os


def fuel(message):
    # bind the url of the website
    url = os.getenv("mgc_gas_url")

    # get the url and save it into a variable
    mgc_page = requests.get(url)

    # parse the content into an html file and save it into a variable
    page = html.fromstring(mgc_page.content)

    # Bind the icon url of mgc into a variable
    icon_url = "https://mgc-gas.com/images/images/footer-logo.png"
    
    # select the first column of the table to get the fuel label
    # resource: https://docs.python-guide.org/scenarios/scrape/
    fuel_label = page.xpath('//td[@class="fuel-prices-history-table-first-td"]')

    # select the second column of the table to get the fuel price
    prices_value = page.xpath('//td[@class="fuel-prices-history-table-td"]')

    # bind fuel labels into variables
    gas90_label = fuel_label[0].text
    gas95_label = fuel_label[1].text
    gas98_label = fuel_label[2].text
    diesel_label = fuel_label[3].text

    # bind fuel prices into variables
    gas90_price = prices_value[0].text
    gas95_price = prices_value[1].text
    gas98_price = prices_value[2].text
    diesel_price = prices_value[3].text

    # create an embed object for mgc
    embed_fuel = discord.Embed(title="Manaseer Oil & Gas", url=url, color=0x000757)
    embed_fuel.set_footer(text="Jordan Modern Oil & Fuel Services Co. Ltd.")
    embed_fuel.set_thumbnail(url=icon_url)

    # add the fuel labels and prices as fields
    embed_fuel.add_field(name=gas90_label, value=gas90_price, inline=True)
    embed_fuel.add_field(name=gas95_label, value=gas95_price, inline=True)
    embed_fuel.add_field(name=gas98_label, value=gas98_price, inline=True)
    embed_fuel.add_field(name=diesel_label, value=diesel_price, inline=True)

    # return the embed object
    return embed_fuel
