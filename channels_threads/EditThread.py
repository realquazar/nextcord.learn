'''
In this code we edit a thread
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.channels = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user}')

@bot.command()
@commands.has_permissions(manage_channels=True)
async def edit_thread(ctx, thread: nextcord.Thread, new_name: str):
    await thread.edit(name=new_name)
    await ctx.send(f"Edited thread: {thread.name} to {new_name}")

bot.run("TOKEN")
