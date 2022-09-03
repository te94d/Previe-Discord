import discord
from discord.ext import commands

# checkマーク
UnicodeCheck = "\N{White Heavy Check Mark}"
# cancelマーク
UnicodeCancel = "\N{No Entry Sign}"
# downloadマーク
UnicodeDownload = "\N{Inbox Tray}"

class other_commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print("logged in as " + self.bot.user.name)
    print(self.bot.user.id)
    print('------')
    activity = discord.Activity(name='コマンド一覧は >help ', type=discord.ActivityType.playing)
    await self.bot.change_presence(activity=activity)

  @commands.command()
  async def help(self, ctx):
    await ctx.send("コマンド : 説明\n```>mp3 url : youtubeとtwitterの音声をmp3でDL\n>mp4 url : youtubeとtwitterの動画をmp4でDL\nDLが開始すると"+UnicodeDownload+"が付与されます\nDLが完了すると"+UnicodeCheck+"が付与されます```※DLしたファイルの2次配布は止めましょう")
  
