import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def ARPB(ctx, arg):
    if arg == "AirlineOverview":
        AirlineEmbed = discord.Embed(title="Airline Overview", color=0x285ff4)
        AirlineEmbed.add_field(name="Lufthansa Group", value="Über den Wolken.", inline=False)
        AirlineEmbed.add_field(name="Ryanair", value="Low fares made simple.", inline=True)
        await ctx.send(embed=AirlineEmbed)
    else:
        await ctx.send("Error")


bot.run("WonttellyouthatxD")
