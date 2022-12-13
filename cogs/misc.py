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
import requests
import psutil
import pkg_resources
from discord.ext import commands

repo = 'backyard-Py/project'

r = requests.get('https://api.github.com/repos/{0}/commits?per_page=1'.format(repo))

commit= r.json()

latest_commits = commit

for commit in latest_commits:
    sha = commit["commit"]["tree"]["sha"]
    author = commit["commit"]["committer"]["name"]

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="stats")
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def _about(self, ctx: commands.Context):
        """Statistics of Krypton.."""
        version = pkg_resources.get_distribution("discord.py").version
        total_memory = psutil.virtual_memory().total >> 20
        used_memory = psutil.virtual_memory().used >> 20
        cpu_used = str(psutil.cpu_percent())
        total_members = sum(g.member_count for g in self.bot.guilds)
        cached_members = len(self.bot.users)
        embed = discord.Embed(description=None)
        embed.title = "Krypton Bot"
        embed.url = "https://discord.gg/v3fHbbhE"
        embed.colour = 0x2f3136
        guild_value = len(self.bot.guilds)
        embed.add_field(name=f"Latest Changes", value=f"[`{sha[:6]}`](https://github.com/backyard-Py/project/commit/master)\n**commited by:** [`{author}`](https://github.com/{author})")
        embed.add_field(name="Servers", value=f"`{guild_value:,}` total")
        embed.add_field(name="Members", value=f"`{total_members:,}` Total\n`{cached_members:,}` cached")
        embed.add_field(
            name="Stats",
            value=f"Ping: `{round(self.bot.latency * 1000, 2)}ms`",
        )
        embed.add_field(name="System", value=f"**RAM**: `{used_memory}/{total_memory} MB`\n**CPU used:** `{cpu_used}%`"),
        embed.set_footer(text=f"Made with discord.py v{version}", icon_url="http://i.imgur.com/5BFecvA.png")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(misc(bot))