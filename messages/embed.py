'''
In this code we send two embeds and use the following attributes
- set_image
- set_author
- add_field
- set_thumbnail
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command()
async def embed_properties(interaction: nextcord.Interaction, title: str, *, description: str):
    embed1 = nextcord.Embed(title=title, description=description, color=0x1abc9c)
    embed1.set_image(url="link_of_image")
    embed1.set_author(name=interaction.author, icon_url=interaction.author.avatar.url)
    embed1.add_field(name="Name", value="Value")
    embed1.set_thumbnail(url="your_link")
    await interaction.send(embed=embed1)

@bot.command()
async def other_embed(interaction: nextcord.Interaction):  
    embed2 = nextcord.Embed(title=title, description=description, color=nextcord.Color.random())
    await interaction.send(embed=embed2)

bot.run("TOKEN")
