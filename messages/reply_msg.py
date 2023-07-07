import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command()
async def reply_command(interaction: nextcord.Interaction):
    await interaction.reply("Hello")

bot.run("TOKEN")
