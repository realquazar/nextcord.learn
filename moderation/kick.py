'''
In this code we kick the member and use error handling for some errors
For more information about error handling refer to "on_command_error.py"
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: nextcord.Member, *, reason="No reason provided."):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked.")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a member to kick.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Member not found. Please mention a valid member.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick members.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have permission to kick members.")
    elif isinstance(error, nextcord.Forbidden):
        await ctx.send("I don't have permission to kick that member.")
    else:
        await ctx.send("An error occurred while executing the kick command.")

bot.run("TOKEN")
