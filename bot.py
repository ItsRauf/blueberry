import discord
from discord.ext import commands
import json

# Config File
f = open("config.json")
config = json.load(f)

client = commands.Bot(command_prefix=config["prefix"])


@client.event
async def on_ready():
    print("Connected to Discord")

client.run(config["token"])
