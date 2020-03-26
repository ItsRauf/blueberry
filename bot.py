import discord
from discord.ext import commands
import json

f = open("config.json")
config = json.load(f)

client = commands.Bot(command_prefix=config["prefix"])


@client.event
async def on_ready():
    print("Connected to Discord")


@client.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def clean(ctx: commands.Context, amt=10):
    if ctx.channel.permissions_for(ctx.author).manage_messages:
        deleted = await ctx.channel.purge(limit=amt)
        await ctx.send(f"Cleaned {deleted} messages")


@client.command()
async def kick(ctx: commands.Context, member: discord.Member, *, reason=None):
    if ctx.channel.permissions_for(ctx.author).kick_members:
        try:
            await member.kick(reason=reason)
            if reason:
                await ctx.send(f"Kicked {member} ({member.id}) for `{reason}`")
            else:
                await ctx.send(f"Kicked {member} ({member.id})")
        except discord.HTTPException as err:
            await ctx.send(err.text)


@client.command()
async def ban(ctx: commands.Context, member: discord.Member, *, reason=None):
    if ctx.channel.permissions_for(ctx.author).ban_members:
        try:
            await member.ban(reason=reason)
            if reason:
                await ctx.send(f"Banned {member} ({member.id}) for `{reason}`")
            else:
                await ctx.send(f"Banned {member} ({member.id})")
        except discord.HTTPException as err:
            await ctx.send(err.text)


@client.command()
async def unban(ctx: commands.Context, id: int, *, reason=None):
    if ctx.channel.permissions_for(ctx.author).ban_members:
        bans = await ctx.guild.bans()
        for ban in bans:
            user = ban.user
            if user.id == id:
                try:
                    await ctx.guild.unban(user=user, reason=reason)
                    if reason:
                        await ctx.send(f"Unbanned {user} ({user.id}) for `{reason}`")
                    else:
                        await ctx.send(f"Unbanned {user} ({user.id})")
                except discord.HTTPException as err:
                    await ctx.send(err.text)

client.run(config["token"])
