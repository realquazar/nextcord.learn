'''
In this code we create a blurple button by:
1) Inherriting from nextcord.ui.View
2) Creating the button with its callback "button_callback"
3) In the callback we return the id of the user and send a message which says hello and mentions the user who pressed the button
4) we create a command to display the button called "show_button"
5) We create an instance of the class ButtonView()
6) we send the message passing in the view as the instance of the class ButtonView()

Note:
Style accepts 6 values:
           Values                     Color
-----------------------------------------------           
1) nextcord.ButtonStyle.primary     (blurple)
2) nextcord.ButtonStyle.blurple     (blurple)
3) nextcord.ButtonStyle.secondary   (gray)
4) nextcord.ButtonStyle.link        (gray)
5) nextcord.ButtonStyle.success     (green)
6) nextcord.ButtonStyle.danger      (red)
'''


import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View

class ButtonView(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label="Click here", style=nextcord.ButtonStyle.blurple)
    async def button_callback(self, interaction: nextcord.Interaction, button: nextcord.ui.Button):
        user_id = interaction.user.id
        await interaction.send(f"Hello! <@{user_id}>")

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def show_button(ctx):
    view = ButtonView()
    await ctx.send("click me", view=view)

bot.run("TOKEN")
  
  
                        
