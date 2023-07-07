import nextcord
from nextcord.ext import commands
import asyncio

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"bot is online: {bot.user}")

@bot.command()
async def edit1(interaction: nextcord.Interaction, *, message: str):
    message = await interaction.send(message)
    asyncio.sleep(10)
    await message.edit(content="This message has been edited")

@bot.command()
async def edit_with_id(interaction: nextcord.Interaction, channelid: nextcord.TextChannel, msgid: int):
    if not channelid:
        interaction.send("please provide a channel id")
    elif not msgid:
        interaction.send("Please provide the message id")
    else:
        message_to_edit = await channel.fetch_message(msgid)
        await message_to_edit.edit(content="This message has been edited")

bot.run("TOKEN")
