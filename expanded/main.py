import discord
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
from otherCmd import other_commands
from ytdl import ytdl_commands

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')

bot.add_cog(other_commands(bot))
bot.add_cog(ytdl_commands(bot))

load_dotenv()
discord_token = os.getenv('discord_token')
bot.run(discord_token)
