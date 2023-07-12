import nextcord
from nextcord import commands

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online: {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid argument.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Command is on cooldown. Please try again later.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have permission to perform this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the required role to use this command.")
    elif isinstance(error, commands.BotMissingRole):
        await ctx.send("I don't have the required role to perform this command.")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send("This command cannot be used in a private message.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("Only the bot owner can use this command.")
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send("You don't have any of the required roles to use this command.")
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("This command is currently disabled.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("An error occurred while executing the command.")
    elif isinstance(error, commands.CommandError):
        await ctx.send("An error occurred while executing the command.")
    elif isinstance(error, nextcord.errors.Forbidden):
        await ctx.send("I don't have permission to perform this action.")
    elif isinstance(error, nextcord.errors.HTTPException):
        await ctx.send("An HTTP exception occurred.")
    elif isinstance(error, nextcord.errors.NotFound):
        await ctx.send("The requested resource was not found.")
    elif isinstance(error, nextcord.errors.DiscordServerError):
        await ctx.send("An error occurred on the Discord server.")
    elif isinstance(error, nextcord.errors.ConnectionClosed):
        await ctx.send("The connection to Discord was closed.")
    else:
        print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
