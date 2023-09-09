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
    Destination = j["dest"]
    scheduled = j["sched"]
    Terminal = j["terminal"]
    Gate = j["gate"]
    await ctx.send(f"```txt\n\
                    _________________________________\n\
                   | Flight | Dest | sched | T | Gt |\n\
                   |--------------------------------|\n\
                   | {arg} | {Destination} | {scheduled}z | {Terminal} | {Gate} |\n\
                   ---------------------------------\n\
                   ```")
