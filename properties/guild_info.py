'''
In this code we get the information of the guild/server
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def server_info(ctx):
    server = ctx.guild

    owner = server.owner
    region = server.region
    created_at = server.created_at.strftime("%Y-%m-%d %H:%M:%S")
    member_count = server.member_count
    verification_level = str(server.verification_level)

    info_message = (
        f"Server Name: {server.name}\n"
        f"Server ID: {server.id}\n"
        f"Owner: {owner}\n"
        f"Region: {region}\n"
        f"Created At: {created_at}\n"
        f"Member Count: {member_count}\n"
        f"Verification Level: {verification_level}\n"
    )

    await ctx.send(info_message)

bot.run("TOKEN")
