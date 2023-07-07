'''
In this program, we create to commands to send the message hello using ctx and interaction
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    print(f"Bot is online {bot.user}")

@bot.command()
async def sayhelloctx(ctx):
    ctx.send("hello")

@bot.command()
async def sayhellointeraction(interaction: nextcord.Interaction):
    interaction.send("hello")

bot.run("TOKEN")
