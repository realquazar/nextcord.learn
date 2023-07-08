import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await message.channel.send(f'You said: {message.content}')

bot.run("TOKEN")
