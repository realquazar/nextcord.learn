'''
In this code we add and delete reactions
'''


import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.reactions = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def add_reaction(ctx):
    message = await ctx.send('React to this message!')
    
    await message.add_reaction('👍')

@bot.command()
async def delete_reaction(ctx):
    message = await ctx.send('React to this message!')
    
    reaction = '👍'
    await message.add_reaction(reaction)
    
    for user in await reaction.users().flatten():
        if user == bot.user:
            await message.remove_reaction(reaction, bot.user)

@bot.command()
async def clear_reactions(ctx):
    message = await ctx.send('React to this message!')
    
    reactions = ['👍', '🛠', '🎉']
    for reaction in reactions:
        await message.add_reaction(reaction)
    
    async for reaction in message.reactions:
        await message.clear_reaction(reaction)

bot.run("TOKEN")
