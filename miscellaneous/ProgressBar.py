'''
In this code we create a progress bar
'''

import nextcord
from nextcord.ext import commands
import asyncio

intents = nextcord.Intents.default()

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command(name='bar', description="Progress Bar")
async def prog(ctx, total=40):    
    progress = 0
    bar_length = 40    
    bar = ''
    message = await ctx.send(f'{bar}Loading...')
    while progress <= total:
        filled = int(bar_length * (progress / total))
        bar = f'`{"█" * filled}{"░" * (bar_length - filled)}`'
                  
        await message.edit(content=f'{bar}')        
        progress += 8
        await asyncio.sleep(0.2)


bot.run("TOKEN")
