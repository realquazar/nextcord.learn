'''
In this code, we add the extension jishaku to help for logging with nextcord
To install jishaku use: 
  Mac/linux: pip3 install jishaku
  Windows: pip install jishaku

To run jishaku in your server use
>jsk sync

Note: replace ">" with your prefix command
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    await bot.add_extension("jishaku")
    print("Bot is online {bot.user}")

bot.run("TOKEN")
  


        
