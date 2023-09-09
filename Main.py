import discord
from discord.ext import commands
import flightmanager

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def alov(ctx):
    airlineembed = discord.Embed(title="Airline Overview", color=0x285ff4)
    airlineembed.add_field(name="Lufthansa Group", value="Über den Wolken.", inline=False)
    airlineembed.add_field(name="Ryanair", value="Low fares made simple.", inline=True)
    await ctx.send(embed=airlineembed)


@bot.command()
async def hostflight(ctx, flightnumber, dest, sched, terminal, gate):
    await flightmanager.hostflight(ctx, flightnumber, dest, sched, terminal, gate)


@bot.command()
async def flightinfo(ctx, arg):
    await flightmanager.flightinfo(ctx, arg)


@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

bot.run("Notyourproblem!")
