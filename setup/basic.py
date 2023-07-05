import nextcord
from nextcord.ext import commands

# Declare the intents variable and set them to either default or all. Intents can also be enabled individually as shown below with intents.typing
# For more information refer to the documentation: https://docs.nextcord.dev/en/stable/intents.html
intents = nextcord.Intents.default()
intents.typing = False

# Initialize the commands.Bot() class to a variable with a command prefix (>) and intents
bot = commands.Bot(command_prefix=">", intents=intents)


# An event to display a message when the bot is logged in
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

# A command that greets the user who uses the command
@bot.command()
async def hello(interaction: nextcord.Interaction):
    await interaction.send(f"hello! {interaction.author}")

# Run the bot, replace TOKEN with your actual token set in the discord developer portal
bot.run("TOKEN")
