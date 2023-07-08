import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online: {bot.user}")

@bot.command()
async def channel_message(interaction: nextcord.Interaction):
    channel_id = 123456789
    channel = bot.get_channel(channel_id)
    await channel.send("Hello")

bot.run("TOKEN")
