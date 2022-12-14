import discord
from discord.ext import commands 


        
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        
async def setup(bot):
    await bot.add_cog(Music(bot))