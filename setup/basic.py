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
