import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command(name='mute', description='Mutes a user for a given amount of time')
@commands.has_permissions(moderate_members=True)
async def mute(ctx, user: nextcord.Member, time, reason):
    timeSeconds = humanfriendly.parse_timespan(time)
    await ctx.send(f'{user} has been muted successfully.')
    await user.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=timeSeconds))
    await user.send(f'You have been muted in {ctx.guild.name} by {ctx.author} for {time} for {reason}')

bot.run("TOKEN")
    
