'''
In this code we:
1) Create a main command, "main"
2) Create a sub command of the main command "sub"
3) Create a sub command of the sub command "sub" called "sub_sub"

'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.slash_command(guild_ids=[TESTING_GUILD_ID])
async def main_command(interaction: nextcord.Interaction):    
    await interaction.send("Main")

@main_command.subcommand(description="Subcommand 1")
async def sub(interaction: nextcord.Interaction):
    await interaction.send("Subcommand 1")

@sub1.subcommand(description="Subcommand 1")
async def sub_sub(interaction: nextcord.Interaction):
    await interaction.send("Subcommand of subcommand 1")

bot.run("TOKEN")
