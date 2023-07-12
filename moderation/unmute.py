import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command(name='unmute', description='Unmutes a user')
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, user: nextcord.Member, reason):
    await ctx.send(f'{user} has been unmuted successfully.')
    await user.edit(timeout=None)
    await user.send(f'You have been unmuted in {ctx.guild.name} by {ctx.author} for {reason}')

bot.run("TOKEN")
    
