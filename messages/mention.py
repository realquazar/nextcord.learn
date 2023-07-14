'''
In this code we look through how to mention users, channels and roles by their id's
For more information visit: https://discord.com/developers/docs/reference#message-formatting
'''

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@bot.command()
async def mention(ctx, user_id: int, channel_id: int, role_id: int):
    user = await bot.fetch_user(user_id)
    channel = bot.get_channel(channel_id)
    role = ctx.guild.get_role(role_id)
    
    if user is not None:
        user_mention = user.mention
    else:
        user_mention = f"<@{user_id}>"

    if channel is not None:
        channel_mention = channel.mention
    else:
        channel_mention = f"<#{channel_id}>"

    if role is not None:
        role_mention = role.mention
    else:
        role_mention = f"<@&{role_id}>"

    await ctx.send(f"Mentioning user: {user_mention}")
    await ctx.send(f"Mentioning channel: {channel_mention}")
    await ctx.send(f"Mentioning role: {role_mention}")

bot.run("TOKEN")
