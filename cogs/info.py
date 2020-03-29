import discord
from discord.ext import commands


class info(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx: commands.Context):
        """Check if the bot is alive"""
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")


def setup(client: commands.Bot):
    client.add_cog(info(client))
