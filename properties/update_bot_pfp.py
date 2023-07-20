'''
In this code we change the bots existing profile picture
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def changeimg(interaction: nextcord.Interaction):
    with open('botpfp.png', 'rb') as image:
        await bot.user.edit(avatar=image.read())
        await interaction.send("Set new pfp")

bot.run("TOKEN")
