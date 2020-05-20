from common import message_splitter
from dotenv import load_dotenv
import requests
import feedparser
import discord
from os import getenv


def royaa_news():
    print("[!] Received a message asking for Ro'yaa News")

    # We parse the response of the RSS URL and save it into response.
    royaa_rss_url = getenv("royaa_rss_url")
    response = feedparser.parse(royaa_rss_url)

    if response['status'] == 200:
        print('all ok')
    else:
        print('Unable to connect to Ro\'yaa news. Please try again later.')
        return

    # Get the logo
    royaa_logo = response['feed']['logo']

    # Get the title
    royaa_title = response['feed']['title']

    # Get the description (subtitle)
    royaa_desc = response['feed']['subtitle']

    # We create the embed object and fill it with the main data
    embed_royaa = discord.Embed(title=royaa_title, url="https://royanews.tv", color=0x000757)
    embed_royaa.set_footer(text=royaa_desc)
    embed_royaa.set_thumbnail(url=royaa_logo)

    # Set the image of the embed
    # Journal: Looks disgusting
    # embed_royaa.set_image(url=royaa_logo)

    # Save the first five pieces of news in 5 variables.
    news1 = response['entries'][0]  # title / summary / link / updated ('2020-05-08T17:58:59+03:00')
    news2 = response['entries'][1]
    news3 = response['entries'][2]
    news4 = response['entries'][3]
    news5 = response['entries'][4]
    news6 = response['entries'][5]

    # We create a string for each piece of news. The text takes the title and the link containing.. well.. the link.
    news_value1 = "[{0}]({1})".format(news1['title'], news1['link'])
    news_value2 = "[{0}]({1})".format(news2['title'], news2['link'])
    news_value3 = "[{0}]({1})".format(news3['title'], news3['link'])
    news_value4 = "[{0}]({1})".format(news4['title'], news4['link'])
    news_value5 = "[{0}]({1})".format(news5['title'], news5['link'])
    news_value6 = "[{0}]({1})".format(news6['title'], news6['link'])

    # We represent each field with a number and the previously made value string.
    embed_royaa.add_field(name="٣", value=news_value3, inline=True)
    embed_royaa.add_field(name="٢", value=news_value2, inline=True)
    embed_royaa.add_field(name="١", value=news_value1, inline=True)
    embed_royaa.add_field(name="٦", value=news_value6, inline=True)
    embed_royaa.add_field(name="٥", value=news_value5, inline=True)
    embed_royaa.add_field(name="٤", value=news_value4, inline=True)

    return embed_royaa
