import discord
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
import lib

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')

bot.add_cog(lib.otherCmd.other_commands(bot))
bot.add_cog(lib.ytdl.ytdl_commands(bot))

load_dotenv()
discord_token = os.getenv('discord_token')
bot.run(discord_token)
