import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_message_delete(message):
    await message.channel.send(f'A message was deleted: {message.content}')

bot.run("TOKEN")
