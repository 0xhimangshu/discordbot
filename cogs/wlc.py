import json
import discord
from discord.ext import commands

class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        with open("./config/welcome.json", "r")as f:
            guilddata = json.load(f)
        channel = self.bot.get_channel(guilddata[member.guild.name][0]["chann"])
        embed=discord.Embed(title=f"Welcome to {member.guild.name}", description=f"{member.mention} thanks for joining")
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text="have a nice stay", icon_url=member.guild.icon)
        await channel.send(embed=embed)
        arole = discord.utils.get(member.guild.roles, id=guilddata[member.guild.name][0]["rol"])
        await member.add_roles(arole)
        
async def setup(bot):
    await bot.add_cog(welcome(bot))