from discord_webhook import DiscordWebhook, DiscordEmbed
from os import getenv
from dotenv import load_dotenv

# load the .env file
load_dotenv(verbose=True)

# obtain the webhook URL
webhook_url = getenv("DiscordWebhookURL")

# prepare the webhook
webhook = DiscordWebhook(url=webhook_url,
                         content='Webhook Message')

# create embed object for webhook
embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color=242424)

# add embed object to webhook
webhook.add_embed(embed)

# send the response to discord
response = webhook.execute()