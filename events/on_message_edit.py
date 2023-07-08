'''
Records the edited message content and displays the original message and the edited message
'''

import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_message_edit(before, after):
    await after.channel.send(f'A message was edited by {after.author}: {before.content} -> {after.content}')

bot.run("TOKEN")
