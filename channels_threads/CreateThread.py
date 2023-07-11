'''
In this code we create a thread
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user}')

@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_thread(ctx, channel: nextcord.TextChannel, thread_name: str):
    thread = await channel.create_thread(name=thread_name)
    await ctx.send(f"Created thread: {thread.mention}")
      
bot.run("TOKEN")
