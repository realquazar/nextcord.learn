import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.online)
    print(f"Bot is online {bot.user}")

@bot.command()
async def set_dnd(ctx):
    bot.change_presence(status=nextcord.Status.dnd)
    ctx.send("Bot's status: Do Not Disturn")

@bot.command()
async def set_idle(ctx):
    bot.change_presence(status=nextcord.Status.idle)
    ctx.send("Bot's status: Idle")

@bot.command()
async def set_offline(ctx):
    bot.change_presence(status=nextcord.Status.offline)
    ctx.send("Bot's status: Offline")

@bot.command()
async def set_streaming(ctx):
    await bot.change_presence(
        status=nextcord.Status.online,
        activity=nextcord.Streaming(name='My Stream', url='https://www.twitch.tv/your_channel')
    )
    ctx.send("Bot's status: Streaming")

@bot.command()
async def set_gaming(ctx):
    await bot.change_presence(
        status=nextcord.Status.online,
        activity=nextcord.Game(name='Game')
    )
    await ctx.send("Bot's status: Gaming")      
      
bot.run("TOKEN")
