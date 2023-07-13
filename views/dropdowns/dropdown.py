'''
In this code we create a dropdown by:
1) Inherriting from nextcord.ui.Select (or subclassing), then we create the options with "nextcord.SelectOption()"

2) Specifying the placeholder, minimum and maximum value to be selected (in this case it is one which means that the user 
can only select 1 item from the dropdown

3) Create the callback inside the dropdown class. The callback sends the item the user has selected. This is done by accessing it by
"self.values[0]"

4) Create the view by inherriting from "nextcord.ui.View" and adding the dropdown class in there with "self.add_item()"

5) Create the command to display the dropdown
'''


import nextcord
from nextcord.ext import commands

class Planets(nextcord.ui.Select):
    def __init__(self):
        options = [
          nextcord.SelectOption(label="Mercury", description="The 1st planet from the sun", emoji="🔴"),
          nextcord.SelectOption(label="Earth", description="The 3rd planet from the sun", emoji="🌎"),
          nextcord.SelectOption(label="Saturn", description="The 6th planet from the sun", emoji="🪐")
        ]

    super().__init__(
        placeholder="Choose your planet",
        min_value=1,
        max_value=1,
        options=options
    )

    async def callback(interaction: nextcord.Interaction):
        interaction.send(f"Selected value: {self.values[0]}")
    

class PlanetsView(nextcord.ui.View)
    def __init__(self):
        super().__init__()
        self.add_item(Planets())

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot is online {bot.user}")

@bot.command()
async def display_dropdown(interaction: nextcord.Interaction):
    view = PlanetsView()
    await interaction.send("Choose the planet", view=view)

bot.run("TOKEN")
