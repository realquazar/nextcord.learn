'''
In this code we send, edit and delete an ephemeral message
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"bot is online {bot.user}")

@bot.command()
async def send_ephemeral_message(ineraction: nextcord.Interaction):
    interaction.send("This is an ephemeral message", ephemeral=True)

@bot.command()
async def edit_ephemeral_message(ineraction: nextcord.Interaction):
    await interaction.send("Ephemeral Message", ephemeral=True)
    await interaction.edit_original_message(content="Edited ephemeral message")
    

@bot.command()
async def delete_ephemeral_message(ineraction: nextcord.Interaction):
    await interaction.send("Another ephemeral message", ephemeral=True)
    await interaction.delete_original_message()

bot.run("TOKEN")
