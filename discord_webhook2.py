from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/704434829978239018/a6AKQJprSQ6qbdP07A0tJJdYT0GHgqWVSAPTFkQ0CU1SUO5IDE9vOk2Gcrz-skwlydvO', content='Webhook Message')
# create embed object for webhook
embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color=242424)

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()