'''
In this code we get the profile of the member and set it as the thumbnail and image in an embed with the icon set as the user's pfp as well
'''


import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def get_pfp(ctx, member: nextcord.Member = None):
    if member is None:
        member = ctx.author

    pfp_url = member.avatar_url
    embed = nextcord.Embed(title="Profile picture", description="pfp of the user", color=0x99aab5)
    embed.set_thumbnail(url=pfp_url)
    embed.set_image(url=pfp_url)
    embed.set_author(name=ctx.author, icon_url=pfp_url)  
    await ctx.send(f"{member.mention}'s profile picture:", embed=embed)
    

bot.run("TOKEN")
