import nextcord
from nextcord.ext import commands
from datetime import datetime, timedelta
import humanfriendly

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
        read_time = humanfriendly.parse_timespan(time) 
        end_time = nextcord.utils.utcnow().timestamp() + read_time
    except ValueError:
        await ctx.send(f"Ends in <t:{int(end_time)}:R> <t:{int(end_time)}:T> ")

bot.run("TOKEN")
