'''
In this code we delete a role
'''

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user}')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx, user: nextcord.Member, role_name):
    role = nextcord.utils.get(ctx.guild.roles, name=role_name)
    
    if role:
        await user.remove_roles(role)
        await ctx.send(f"Removed the {role_name} role from {user.mention}")
    else:
        await ctx.send("Role not found.")
      
bot.run("TOKEN")
