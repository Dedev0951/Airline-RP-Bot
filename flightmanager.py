import discord
import json


async def hostflight(ctx, flight_number, dest, sched, terminal, gate):
    with open("flights.json", "w") as f:
        json.dump(
            {
                flight_number: {
                    "dest": dest,
                    "sched": sched,
                    "terminal": terminal,
                    "gate": gate,
                }
            },
            f,
        )
    await ctx.send(f"Flightplan was created! \nFlightnumber: {flight_number}")


async def flightinfo(ctx, arg):
    with open("flights.json", "r") as g:
        flights = json.load(g)
    j = flights[arg]
    destination = j["dest"]
    scheduled = j["sched"]
    terminal = j["terminal"]
    gate = j["gate"]
    flightembed = discord.Embed(title="Flightinformation", color=0x285ff4)
    flightembed.add_field(name="", value=f"`txt\n\
                    _________________________________\n\
                   | Flight | Dest | sched | T | Gt |\n\
                   |--------------------------------|\n\
                   | {arg} | {destination} | {scheduled}z | {terminal} | {gate} |\n\
                   ---------------------------------\n\
                   `", inline=False)
    await ctx.send(embed=flightembed)
