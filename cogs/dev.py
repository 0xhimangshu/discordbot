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
from discord.ext import commands
import typing

class dev(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: typing.Optional[typing.Literal["~", "*", "^"]] = None) -> None:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

async def setup(bot):
    await bot.add_cog(dev(bot))
