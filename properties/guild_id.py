'''
In this code we get the guild id of the user who interacted or ran the command
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def get_guild_id(ctx: nextcord.commands.Context):
    guild_id = ctx.guild.id
    await ctx.send(f"Guild ID: {guild_id}")

bot.run("TOKEN")
