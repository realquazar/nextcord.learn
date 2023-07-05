'''
In this code we autoshard out discord bot.
Autosharding is a feature to split or create multiple instances of the discord bot to reduce workload of the bot. This is especially useful
for bots in many guilds/servers. Change shard_count on the number of guilds/servers the bot is in.

Refer to basic.py to understand the functionality as the code is almost the same
'''

import nextcord
from nextcord.ext import commands

bot = AutoShardedBot(shard_count=20, command_prefix=">", intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    print("Bot is online")
