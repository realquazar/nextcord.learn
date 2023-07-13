import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online: {bot.user}")

@bot.command()
async def purge(interaction: nextcord.Interaction, limit: int):
    await interaction.channel.purge(limit=limit)

bot.run("TOKEN")
