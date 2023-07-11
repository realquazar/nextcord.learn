'''
In this code we delete a channel
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
async def delete_channel(ctx, channel: nextcord.TextChannel):
    await channel.delete()
    await ctx.send(f"Deleted channel: {channel.name}")

bot.run("TOKEN")
