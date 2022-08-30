import discord
import re
import urllib.request
from discord.ext import commands
from yt_dlp import YoutubeDL
from tkinter import filedialog

class extensions(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  # urlチェック関数
  def check_url(url):
    flag = True
    if re.match(r"^https?:\/\/", url):
      try:
        f = urllib.request.urlopen(url)
        f.close()
        if ("youtube" in url) == True or ("youtu.be" in url) == True or ("twitter" in url) == True:
          flag = True
        else:
          flag = False
      except urllib.request.HTTPError:
        flag = False
      return flag
    else:
      flag = False
      return flag

  @commands.Cog.listener()
  async def on_ready(self):
    print("logged in as " + self.bot.user.name)
    print(self.bot.user.id)
    print('------')
    activity = discord.Activity(name='コマンド一覧は >help ', type=discord.ActivityType.playing)
    await self.bot.change_presence(activity=activity)

  @commands.command()
  async def help(self, ctx):
    await ctx.send("コマンド : 説明\n```>mp3 url : youtubeとtwitterの動画をmp3でDL\n>mp4 url : youtubeとtwitterの動画をmp4でDL\nDLが開始すると"+UnicodeDownload+"が付与されます\nDLが完了すると"+UnicodeCheck+"が付与されます```※DLしたファイルの2次配布は止めましょう")

  @commands.command()
  async def mp3(self, ctx, url):
    if check_url(url) == True:
      msg = await ctx.send("mp3でダウンロード")
      await msg.add_reaction(UnicodeDownload)
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp3", ".mp3")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        initialfile = "tmp", # 名前の初期値
        defaultextension = "mp3"
        )
      print(filename)
      ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await msg.add_reaction(UnicodeCheck)
    else:
      await ctx.send("urlが有効ではありません")

  @commands.command()
  async def mp4(self, ctx, url):
    if check_url(url) == True:
      msg = await ctx.send("mp4でダウンロード")
      await msg.add_reaction(UnicodeDownload)
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp4", ".mp4")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        initialfile = "tmp", # 名前の初期値
        defaultextension = "mp4"
        )
      print(filename)
      ydl_opts = {
        'format': 'best',
        'outtmpl': filename,
        }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await msg.add_reaction(UnicodeCheck)
    else:
      await ctx.send("urlが有効ではありません")