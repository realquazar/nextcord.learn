'''
In this code we create options for out slash command "hi"

Note:
Slash Options can be made optional by setting "required=False" in the parameter of SlashOption()
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">",  intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    
@bot.slash_command(name="hi", description="Say hi", number: int = SlashOption(name="picker", choices={"one": 1, "two": 2, "three": 3}))
async def say_hi(interaction: nextcord.Interaction):
    await interaction.send("Hi")


bot.run("TOKEN")
