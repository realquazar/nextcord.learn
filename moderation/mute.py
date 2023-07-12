import nextcord
from nextcord.ext import commands

intents=nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: nextcord.Member, duration: int, *, reason: str):
    muted_role = nextcord.utils.get(ctx.guild.roles, name="muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="muted")

    await member.add_roles(muted_role)
    await ctx.send(f"{member.mention} has been muted for {duration} because: {reason}
    
    await asyncio.sleep(duration)
    await member.edit(mute=True)

bot.run("TOKEN")
    
