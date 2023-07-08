import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run("TOKEN")
