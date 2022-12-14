# -*- coding: utf-8 -*-
__author__ = "himangshu147-git"
__copyright__ = "Copyright 2022, himangshu"
__credits__ = ["himangshu147-git"]
__license__ = "MIT"
__version__ = "beta 0.1a"
__maintainer__ = "himangshu147-git"
__email__ = "backyardpy147@gmail.com"
__status__ = "development"

import discord
import datetime
import typing
from discord.ext import commands

class modaration(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.hybrid_command(name="clear")
    async def purge(self, ctx: commands.Context, amount: int=None):
        if amount == None:
            await ctx.channel.purge(limit=50)
            await ctx.send(f"Message deleted")
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"{amount} Message deleted")

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.is_owner()
    async def timeout(self, ctx: commands.Context, member: discord.Member, time: int, format: typing.Literal["sec", "min", "hour", "day"]):
        if format == "sec":
            await member.timeout(datetime.timedelta(days=0, seconds=time, minutes=0, hours=0))
        elif format == "min":
            await member.timeout(datetime.timedelta(days=0, seconds=0, minutes=time, hours=0))
        elif format == "hour":
            await member.timeout(datetime.timedelta(days=0, seconds=0, minutes=0, hours=time))
        elif format == "day":
            await member.timeout(datetime.timedelta(days=time, seconds=0, minutes=0, hours=0))
        else:
            await member.timeout(datetime.timedelta(days=0, seconds=60, minutes=0, hours=0))
        embed=discord.Embed(title=f"Sucessfully timeouted {member.name} for {time}{format}", color=discord.Color.red())
        embed.set_footer(text=f"timeouted by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(modaration(bot))
