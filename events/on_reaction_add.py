'''
Records the user who reacted along with the emoji that they have interacted with and sends a message
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user.name} reacted with {reaction.emoji}!')

bot.run("TOKEN")
