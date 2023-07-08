'''
Records the user who removed their reaction along with the emoji and sends a message
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_reaction_remove(reaction, user):
    await reaction.message.channel.send(f'{user.name} removed their reaction of {reaction.emoji}!')

bot.run("TOKEN")
