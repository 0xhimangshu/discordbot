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
from config import config
from discord.ext import commands
from discord.utils import setup_logging

class Bot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	async def on_ready(self):
		self.log.info(f"logged in as {self.user}")

	async def on_guild_join(self, guild):
		with open('./config/prefixes.json', 'r') as f:
			prefixes = json.load(f)
		prefixes[guild.name] = '?'
		
		with open('./config/prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent=4)

	async def on_guild_remove(self, guild):
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
		g_id = discord.Object(id=1050334900873592853)
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

	bot.log = logging.getLogger("client")
	
	for file in os.listdir("./cogs"):
		if file.endswith(".py"):
			try:
				await bot.load_extension("cogs." + file[:-3])
				print("cogs." + file[:-3])
			except:
				traceback.print_exc()
	
	setup_logging()
	await bot.start(os.getenv("token"))

asyncio.run(main())