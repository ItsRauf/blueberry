import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def clean(self, ctx: commands.Context, amt=10):
        """Bulk delete messages in a channel"""
        if ctx.channel.permissions_for(ctx.author).manage_messages:
            deleted = await ctx.channel.purge(limit=amt)
            await ctx.send(f"Cleaned {deleted} messages")

    @commands.command()
    @commands.guild_only()
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        """Kick a user from the server"""
        if ctx.channel.permissions_for(ctx.author).kick_members:
            try:
                await member.kick(reason=reason)
                if reason:
                    await ctx.send(f"Kicked {member} ({member.id}) for `{reason}`")
                else:
                    await ctx.send(f"Kicked {member} ({member.id})")
            except discord.HTTPException as err:
                await ctx.send(err.text)

    @commands.command()
    @commands.guild_only()
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        """Ban a user from the server"""
        if ctx.channel.permissions_for(ctx.author).ban_members:
            try:
                await member.ban(reason=reason)
                if reason:
                    await ctx.send(f"Banned {member} ({member.id}) for `{reason}`")
                else:
                    await ctx.send(f"Banned {member} ({member.id})")
            except discord.HTTPException as err:
                await ctx.send(err.text)

    @commands.command()
    @commands.guild_only()
    async def unban(self, ctx: commands.Context, id: int, *, reason=None):
        """Unban a user from the server"""
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


def setup(client: commands.Bot):
    client.add_cog(moderation(client))
