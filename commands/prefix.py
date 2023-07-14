import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def hi(ctx):
    ctx.send("Hi")

bot.run("TOKEN")
