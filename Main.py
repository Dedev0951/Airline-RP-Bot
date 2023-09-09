import discord
from discord.ext import commands
import flightmanager

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def ALOV(ctx):
    AirlineEmbed = discord.Embed(title="Airline Overview", color=0x285ff4)
    AirlineEmbed.add_field(name="Lufthansa Group", value="Über den Wolken.", inline=False)
    AirlineEmbed.add_field(name="Ryanair", value="Low fares made simple.", inline=True)
    await ctx.send(embed=AirlineEmbed)


@bot.command()
async def hostflight(ctx, flightnumber, dest, sched, Terminal, Gate):
    await flightmanager.hostflight(ctx, flightnumber, dest, sched, Terminal, Gate)


@bot.command()
async def flightinfo(ctx, arg):
    await flightmanager.flightinfo(ctx, arg)

bot.run("Notyourproblem!")
