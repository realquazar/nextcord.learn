'''
In this code we delay or defer the message to send

Note: To send a message after it has been defered use "interaction.followup.send()" to send your next message
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f"Online: {bot.user}")

@bot.command()
async def defer_command(interaction: nextcord.Interaction):
    await interaction.response.defer()
    await asyncio.sleep(5)
    await interaction.followup.send("Next Message")

bot.run("TOKEN")
    
