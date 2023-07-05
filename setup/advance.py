'''
In this code we:
1) Subclass commands.Bot() in a class called NewBot()

2) Prefix and intents are defined as the required arguments in the NewBot class in the init() method

3) super().init() inherits the commands.Bot() class with the necessary arguments: prefix and intents

4) intents is defined and the instance of the NewBot() class is created which takes 2 arguments: prefix (as a string) and intents

5) The bot fetches the token from the .env file with the load_dotenv() function and is run, .env files are secure and can only be accessed 
by the creator to ensure privacy
'''

import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class NewBot(commands.Bot):
    def __init__(self, prefix, intents):
        super().__init__(command_prefix=prfix, intents=intents)

    async def on_ready(self):
        print(f"Bot logged in as {self.user.name}")

intents = nextcord.Intents.default()
token = os.getenv("BOT_TOKEN")
bot = NewBot(prefix=">", intents=intents)

bot.run(token)

