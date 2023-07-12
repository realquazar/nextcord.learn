'''
In this code we unban the user
Note: If you're using interaction replace "ctx.guild.unban" with "interaction.guild.unban"
and "ctx.send" to "interaction.send"
'''


import nextcord
from nextcord import commands

intents = nextcord.Intents.default()
intents.members= True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int, reason=None):
    try:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user.name}")
    except(commands.UserNotFound, nextcord.NotFound):
        await ctx.send("Error: User not found")
    except:
        await ctx.send("An error occurred")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to unban")

    else:
      await ctx.send("An error occurred")
      
bot.run("TOKEN")

