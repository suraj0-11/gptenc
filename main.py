from telethon import TelegramClient, events

from init import bot
from compressor import compress_file


@bot.on(events.NewMessage(pattern='/start'))

async def start(event):

    await event.respond('Welcome to the File Compressor Bot!')

@bot.on(events.NewMessage(pattern='/help'))

async def help(event):

    await event.respond('Usage:\n'

                        '/crf - Set Constant Rate Factor (CRF)\n'

                        '/codec - Set codec\n'

                        '/preset - Set preset\n'

                        '/quality - Set quality\n'

                        '/compress - Compress the file')

@bot.on(events.NewMessage(pattern='/crf'))

async def set_crf(event):

    # Your code to set CRF

    # Retrieve value from event.text and set the CRF value

@bot.on(events.NewMessage(pattern='/codec'))

async def set_codec(event):

    # Your code to set codec

    # Retrieve value from event.text and set the codec

@bot.on(events.NewMessage(pattern='/preset'))

async def set_preset(event):

    # Your code to set preset

    # Retrieve value from event.text and set the preset

@bot.on(events.NewMessage(pattern='/quality'))

async def set_quality(event):

    # Your code to set quality

    # Retrieve value from event.text and set the quality

@bot.on(events.NewMessage(pattern='/compress'))

async def compress_file(event):

    # Your code to compress the file

    # Retrieve the file from the event message, compress it based on the settings,

    # and send the compressed file as a reply

if __name__ == '__main__':

    bot.run_until_disconnected()

