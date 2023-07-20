'''
In this code we display all the roles of the member by looping through "ctx.author.roles" or "member.roles" stored as the roles variable
in this code with the help of list comprehension
'''


import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def get_roles(ctx, member: nextcord.Member = None):
    if member is None:
        member = ctx.author

    roles = member.roles
    role_names = [role.name for role in roles]

    await ctx.send(f"{member.mention} has the following roles: {', '.join(role_names)}")

bot.run("TOKEN")
