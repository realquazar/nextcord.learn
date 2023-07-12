import nextcord
from nextcord import commands

intents = nextcord.Intents.default()
intents.members= True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command()
async def ban(ctx, member: nextcord.Member, *, reason: str):
    if reason:
        await member.ban(reason=reason)

    else:
        await member.ban(reason="None")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Error: You don't have the necessary permissions to ban")

    elif isinstance(error, commands.BadArgument):
        await ctx.send("Error: User not found")

    else:
        await ctx.send("An error occured")

bot.run("TOKEN")


