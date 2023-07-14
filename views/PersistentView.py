'''
In this code we display a persistent view by specifying timeout=None and adding the view in the on_ready event
'''


import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, Select, View

class ButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Click here", style=nextcord.ButtonStyle.blurple)
    async def button_callback(self, interaction: nextcord.Interaction, button: nextcord.ui.Button):
        user_id = interaction.user.id
        await interaction.send(f"Hello! <@{user_id}>")

    @nextcord.ui.select(placeholder="Select an option", options=[
        nextcord.SelectOption(label="Option 1", value="option_1"),
        nextcord.SelectOption(label="Option 2", value="option_2"),
        nextcord.SelectOption(label="Option 3", value="option_3")
    ])
    async def dropdown_callback(self, select: nextcord.ui.Select, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"You selected: {select.values[0]}")

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    bot.add_view(ButtonView())

@bot.command()
async def show_button(ctx):
    view = ButtonView()
    await ctx.send("Click me", view=view)

bot.run("TOKEN")
