import discord
import json
from discord.ext import commands

class config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    
    async def prefix(self, ctx, *, prefix):
        """sets bot prefix, default prefix '?'"""
        with open('./config/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[ctx.guild.name] = prefix

        with open('./config/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}') 

    @commands.command()
    async def setchan(self, ctx, chan: discord.TextChannel, *, role: discord.Role):
        """sets welcome channel and role"""
        with open("./config/welcome.json", "r") as f:
            guilddata = json.load(f)

        if ctx.message.guild.name in guilddata:
            guilddata[ctx.message.guild.name].append({"chann": chan.id, "rol": role.id})
        else:
            guilddata[ctx.message.guild.name] = [{"chann": chan.id, "rol": role.id}]

        with open("./config/welcome.json", "w") as f:
            json.dump(guilddata, f, indent=4)

async def setup(bot):
    await bot.add_cog(config(bot))