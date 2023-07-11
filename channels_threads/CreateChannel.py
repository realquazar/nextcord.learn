'''
In this code we create a channel
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
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    category = ctx.channel.category
    channel = await guild.create_text_channel(channel_name, category=category)
    await ctx.send(f"Created channel: {channel.mention}")


bot.run("TOKEN")
