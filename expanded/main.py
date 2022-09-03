import discord
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
from otherCmd import extensions
from ytdl import extensions

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')

bot.add_cog(extensions(bot))

load_dotenv()
discord_token = os.getenv('discord_token')
bot.run(discord_token)
