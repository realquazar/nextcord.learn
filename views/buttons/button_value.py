import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button, TextInput

class InputView(nextcord.ui.View):
    def __init__(self, number):
        super.__init__()
        self.number = number

        @nextcord.ui.Button(label="Calculate Square", style=nextcord.ButtonStyle.danger)
        async def calculate(self, interaction: nextcord.Interaction, button: nextcord.ui.Button):
            if self.number is not None:
                squared_number = self.number ** 2
                await interaction.send(f"Square of {self.number} is = {squared_number}")

            else:
                await interaction.send("Please input a number")

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def button_command(ctx):
    value = 12
    view = InputView(value)
    await ctx.send(view=view)

bot.run("TOKEN")              
