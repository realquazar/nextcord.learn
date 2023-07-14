'''
In this code we create slash command "hi" which can be seen in all servers/guilds and hi2 which can only be seen in specific guilds
specified in the "guild_ids" parameter
'''


import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">",  intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    
@bot.slash_command(name="hi", description="Say hi")
async def say_hi(interaction: nextcord.Interaction):
    await interaction.send("Hi")

@bot.slash_command(name="hi2", description="Say hi in guild", guild_ids=[GUILD1, GUILD2])
async def say_hi2(interaction: nextcord.Interaction):
    await interaction.send("Hi2")


bot.run("TOKEN")

