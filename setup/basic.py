'''
In this code we:
1) Declare the intents variable and set them to either default or all. Intents can also be enabled individually as shown below with 
intents.typing. For more information refer to the documentation: https://docs.nextcord.dev/en/stable/intents.html

2) Initialize the commands.Bot() class to a variable with a command prefix (>) and intents

3) Add an event (on_ready) to display a message when the bot is logged in

4) Create a command that greets the user who uses the command

5) Run the bot, replace TOKEN with your actual token set in the discord developer portal
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.typing = False

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def hello(interaction: nextcord.Interaction):
    await interaction.send(f"hello! {interaction.author}")

bot.run("TOKEN")
