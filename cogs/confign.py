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
import json
from discord.ext import commands

class config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def prefix(self, ctx: commands.Context, *, prefix):
        """sets bot prefix, default prefix '?'"""
        with open('./config/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[ctx.guild.name] = prefix

        with open('./config/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}') 

    @commands.hybrid_command()
    async def setchan(self, ctx: commands.Context, chan: discord.TextChannel, *, role: discord.Role):
        """sets welcome channel and role"""
        with open("./config/welcome.json", "r") as f:
            guilddata = json.load(f)

        if ctx.message.guild.name in guilddata:
            guilddata[ctx.message.guild.name].append({"chann": chan.id, "rol": role.id})
        else:
            guilddata[ctx.message.guild.name] = [{"chann": chan.id, "rol": role.id}]

        with open("./config/welcome.json", "w") as f:
            json.dump(guilddata, f, indent=4)
        await ctx.send(f"Welcome channel set to : <#{chan.id}> \nWelcome role set to {role.mention}")


async def setup(bot):
    await bot.add_cog(config(bot))