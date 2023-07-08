'''
Notifies who left the server
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_member_remove(member):
    goodbye_channel = bot.get_channel(goodbye_channel_id)
    await goodbye_channel.send(f'Goodbye, {member.name}!')

bot.run("TOKEN")
