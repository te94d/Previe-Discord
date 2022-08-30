import discord
from discord.ext import commands

class test(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("logged in as " + self.bot.user.name)
    print(self.bot.user.id)  # ID
    print('------')
    activity = discord.Activity(name='コマンド一覧は >help ', type=discord.ActivityType.playing)
    await self.bot.change_presence(activity=activity)
  
  