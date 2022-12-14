# -*- coding: utf-8 -*-
__author__ = "himangshu147-git"
__copyright__ = "Copyright 2022, himangshu"
__credits__ = ["himangshu147-git"]
__license__ = "MIT"
__version__ = "beta 0.1a"
__maintainer__ = "himangshu147-git"
__email__ = "backyardpy147@gmail.com"
__status__ = "development"

import asyncio
import json
import logging
import os
import traceback
import discord
import datetime
from config import config
from discord.ext import commands
from discord.utils import setup_logging

from bot_token import token #create a file called token.py and add this `token="your token"`

botlog = config.logging.getLogger('bot')
logger = logging.getLogger("client")
hdlr = logging.StreamHandler()
frmt = logging.Formatter('[{asctime}] [{levelname:<7}] {name}: {message}', "%Y-%m-%d %H:%M:%S", style='{')
hdlr.setFormatter(frmt)
logger.addFilter(hdlr)

class RemoveNoise(logging.Filter):
    def __init__(self):
        super().__init__(name='discord.state')

    def filter(self, record):
        if record.levelname == 'WARNING' and 'referencing an unknown' in record.msg:
            return False
        return True

class Bot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	async def setup_logging():
		logging.getLogger('discord').setLevel(logging.INFO)
		logging.getLogger('discord.http').setLevel(logging.WARNING)
		logging.getLogger('discord.state').addFilter(RemoveNoise())
		log = logging.getLogger()
		log.setLevel(logging.INFO)
		handler = logging.StreamHandler()
		dt_fmt = "%Y-%m-%d %H:%M:%S"
		fmt = logging.Formatter('[{asctime}] [{levelname:<7}] {name}: {message}', dt_fmt, style='{')
		handler.setFormatter(fmt)
		log.addHandler(handler)

	async def on_ready(self):
		botlog.info(f"logged in as {self.user}")

	async def on_guild_join(self, guild):
		channel= self.get_channel(1046376513509003274)
		embed=discord.Embed(title=f"Joined a guild", description="added default prefix to config")
		embed.add_field(name="Guild Name", value=f"{guild.name}")
		embed.color = discord.Color.green()
		embed.timestamp = datetime.datetime.utcnow()
		await channel.send(embed=embed)
		with open('./config/prefixes.json', 'r') as f:
			prefixes = json.load(f)
		prefixes[guild.name] = '?'
		
		with open('./config/prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent=4)

	async def on_guild_remove(self, guild):
		channel= self.get_channel(1046376513509003274)
		embed=discord.Embed(title=f"Leaved a guild", description="removed guild data from config")
		embed.color = discord.Color.red()
		embed.add_field(name="Guild Name", value=f"{guild.name}")
		embed.timestamp = datetime.datetime.utcnow()
		await channel.send(embed=embed)
		with open("./config/welcome.json") as f:
			data = json.load(f)
		del data[guild.name]
		with open('./config/welcome.json', 'w') as f:
			json.dump(data, f, indent=4)
		with open("./config/prefixes.json") as f:
			data = json.load(f)
		del data[guild.name]
		with open('./config/prefixes.json', 'w') as f:
			json.dump(data, f, indent=4)

	async def setup_hook(self):
		g_id = discord.Object(id=1043123587235729478)
		self.tree.copy_global_to(guild=g_id)
		await self.tree.sync(guild=g_id)
		
def get_prefix(bot, message):
    with open('./config/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[message.guild.name]

async def main():
	bot = Bot(command_prefix=get_prefix,
	          intents=discord.Intents.all(),
			  activity=discord.Activity(type=discord.ActivityType.playing, name="beta 0.1a"),
	          case_insensitive = True)
	
	for file in os.listdir("./cogs"):
		if file.endswith(".py"):
			try:
				await bot.load_extension("cogs." + file[:-3])
				botlog.info("loaded cogs." + file[:-3])
			except:
				traceback.print_exc()
	
	setup_logging()
	await bot.start(token)

asyncio.run(main())