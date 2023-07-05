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

