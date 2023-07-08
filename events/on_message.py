'''
Records each message sent by the user and displays it
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await message.channel.send(f'You said: {message.content}')

bot.run("TOKEN")
