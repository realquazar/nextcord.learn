'''
In the "images" "txtfile" functions we send 2 types of files a txt and png file which are stored locally on the system
In the "accept_file" function we accept the file from the user input and display the same file with the bot
'''


import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online: {bot.user}")

@bot.command()
async def images(interaction: nextcord.Interaction):
    interaction.send("This is an image file", file=nextcord.File("path/to/file.png")

@bot.command()
async def txtfile(interaction: nextcord.Interaction):
    interaction.send("This is a txt file", file=nextcord.File("path/to/file.txt"))

@bot.command()
async def accept_file(interaction: nextcord.Interaction, file: nextcord.File):
    interaction.send("Accepting a file from the user and displaying it", file=file)

bot.run("TOKEN")
