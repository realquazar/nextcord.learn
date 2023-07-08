import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(welcome_channel_id)
    await welcome_channel.send(f'Welcome, {member.name}!')

bot.run("TOKEN")
