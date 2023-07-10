import nextcord
from nextcord.ext import commands
from datetime import datetime

intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def timestamp(ctx, *, time):
    try:
        converted_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        timestamp = converted_time.timestamp()
        await ctx.send(f'Timestamp for {time}: {timestamp}')
    except ValueError:
        await ctx.send('Invalid time format. Please provide time in the format: YYYY-MM-DD HH:MM:SS')

bot.run("TOKEN")
