'''
In this code we get all the information of the user
'''


import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def member_info(ctx: nextcord.commands.Context, member: nextcord.Member = None):
    if member is None:
        member = ctx.author

    member_roles = [role.name for role in member.roles]
    status = str(member.status)
    joined_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")

    info_message = (
        f"Name: {member.name}\n"
        f"ID: {member.id}\n"
        f"Is Bot: {member.bot}\n"
        f"Status: {status}\n"
        f"Top Role: {member.top_role.name}\n"
        f"Joined Server: {joined_at}\n"
        f"Nickname: {member.nick}\n"
        f"Roles: {', '.join(member_roles)}"
    )

    await ctx.send(info_message)

bot.run("TOKEN")
