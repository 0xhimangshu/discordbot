# -*- coding: utf-8 -*-
__author__ = "himangshu147-git"
__copyright__ = "Copyright 2022, himangshu"
__credits__ = ["himangshu147-git"]
__license__ = "MIT"
__version__ = "beta 0.1a"
__maintainer__ = "himangshu147-git"
__email__ = "backyardpy147@gmail.com"
__status__ = "development"

from discord.ext import commands

class modaration(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.hybrid_command(name="clear")
    async def purge(self, ctx: commands.Context, amount: int=None):
        if amount == None:
            await ctx.channel.purge(limit=50)
            await ctx.send(f"50 message deleted")
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"{amount} message deleted")

async def setup(bot):
    await bot.add_cog(modaration(bot))
