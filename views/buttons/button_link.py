'''
In this code we create a button which redirects you to a link 
'''

import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button

class MyView(View):
    def __init__(self):
        super().__init__()
        
    @nextcord.ui.button(label='OpenAI Website', style=nextcord.ButtonStyle.link, url='https://link_here')
    async def openai_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        pass

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def start(ctx):
    view = MyView()
    await ctx.send('Click the link button:', view=view)

bot.run("TOKEN")
