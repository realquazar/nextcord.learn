'''
In this code we delete a thread
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
async def delete_thread(ctx, thread: nextcord.Thread):
    await thread.delete()
    await ctx.send(f"Deleted thread: {thread.name}")

bot.run("TOKEN")
