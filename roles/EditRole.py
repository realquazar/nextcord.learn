'''
In this code we edit a role
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
async def edit_role(ctx, role_name, new_name):
    role = nextcord.utils.get(ctx.guild.roles, name=role_name)
    
    if role:
        await role.edit(name=new_name)
        await ctx.send(f"Edited the {role_name} role to {new_name}")
    else:
        await ctx.send("Role not found")
      
bot.run("TOKEN")
