#In this code, we add the extension jishaku to help for logging with nextcord

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    await bot.add_extension("jishaku")
    print("Bot is online {bot.user}")

bot.run("TOKEN")
  


        
