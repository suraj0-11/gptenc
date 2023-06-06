from telethon.sync import TelegramClient

from telethon import events

# Replace the values below with your own API credentials

api_id = '5168062'

api_hash = '04c049aa96d1cc87920b45b7fb43c0d0'

# Create a TelegramClient instance

client = TelegramClient('bot_session', api_id, api_hash)

# Initialize the bot

bot = client.start(bot_token='5843716104:AAFqDqKXcfHdpbh3WPgwfYZpXCIGKgRkDGk')
