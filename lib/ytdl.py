import discord
import re
import urllib.request
from discord.ext import commands
from yt_dlp import YoutubeDL
from tkinter import filedialog

# checkマーク
UnicodeCheck = "\N{White Heavy Check Mark}"
# cancelマーク
UnicodeCancel = "\N{No Entry Sign}"
# downloadマーク
UnicodeDownload = "\N{Inbox Tray}"

# urlチェック関数
def check_url(url):
  flag = []
  if re.match(r"^https?:\/\/", url):
    try:
      f = urllib.request.urlopen(url)
      f.close()
      if ("youtube" in url) or ("youtu.be" in url):
        flag = [True, 1]
      elif ("twitter" in url):
        flag = [True, 2]
      else:
        flag = [False]
    except urllib.request.HTTPError:
      flag = [False]
    return flag
  else:
    flag = [False]
    return flag

# video meta
def video_meta(url):
  ydl_opts = {} 
  with YoutubeDL(ydl_opts) as ydl: 
    meta = ydl.extract_info(url, download= False) 
    return meta

class ytdl_commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def mp3(self, ctx, url):
    if check_url(url)[0] == True:
      msg = await ctx.send("mp3でダウンロード")
      await msg.add_reaction(UnicodeDownload)
      meta = video_meta(url)
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp3", ".mp3"),("aac", ".aac"),("wav", ".wav"),("m4a", ".m4a")], # ファイルフィルタ
        initialdir = "./", # ディレクトリ
        initialfile = meta['title'], # title
        defaultextension = "mp3"
        )
      print(filename)
      if filename:
        ydl_opts = {
          'format': 'bestaudio/best',
          'outtmpl': filename,
          }
        with YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
        await msg.add_reaction(UnicodeCheck)        
      else:
        await msg.add_reaction(UnicodeCancel) 
    else:
      await ctx.send("urlが有効ではありません\nこのコマンドではyoutubeかtwitterの音声をダウンロードできます")

  @commands.command()
  async def mp4(self, ctx, url):
    if check_url(url)[0] == True:
      msg = await ctx.send("mp4でダウンロード")
      await msg.add_reaction(UnicodeDownload)
      meta = video_meta(url)
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp4", ".mp4"),("webm", ".webm"),("flv", ".flv")], # ファイルフィルタ
        initialdir = "./", # ディレクトリ
        initialfile = meta['title'], # title
        defaultextension = "mp4"
        )
      print(filename)
      if filename:
        ydl_opts = {
          'format': 'best',
          'outtmpl': filename,
          }
        with YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
        await msg.add_reaction(UnicodeCheck)
      else:
        await msg.add_reaction(UnicodeCancel)
    else:
      await ctx.send("urlが有効ではありません\nこのコマンドではyoutubeかtwitterの動画をダウンロードできます")

  @commands.command()
  async def info(self, ctx, url):
    if check_url(url)[1] == 1:
      meta = video_meta(url)
      embed = discord.Embed()
      embed.color = 0xFFBF11
      embed.title = 'Contents Information'
      embed.description = 'コンテンツ関連の情報'
      embed.set_author(name='MP94',
        icon_url=self.bot.user.avatar_url)
      embed.set_image(
        url = meta['thumbnail']
      )
      embed.add_field(name='Title', value='```'+meta['title']+'```', inline=False)
      embed.add_field(name='Channel', value='```'+meta['uploader']+'```', inline=False)
      embed.add_field(name='Views', value='```'+str(meta['view_count'])+'```')
      embed.add_field(name='Likes', value='```'+str(meta['like_count'])+'```')
      embed.add_field(name='Upload Date', value='```'+str(meta['upload_date'])+'```', inline=False)
      embed.add_field(name='Video ID', value='```'+meta['id']+'```', inline=False)
      embed.add_field(name='URL', value='```'+url+'```', inline=False)
      await ctx.send(embed=embed)
    elif check_url(url)[1] == 2:
      meta = video_meta(url)
      title = meta['title'].split()
      embed = discord.Embed()
      embed.color = 0xFFBF11
      embed.title = 'Contents Information'
      embed.description = 'コンテンツ関連の情報'
      embed.set_author(name='MP94',
        icon_url=self.bot.user.avatar_url)
      embed.set_image(
        url = meta['thumbnail']
      )
      embed.add_field(name='Title', value='```'+title[2]+'```', inline=False)
      embed.add_field(name='Account', value='```'+meta['uploader']+'```', inline=False)
      embed.add_field(name='Likes', value='```'+str(meta['like_count'])+'```')
      embed.add_field(name='Upload Date', value='```'+str(meta['upload_date'])+'```')
      embed.add_field(name='Video ID', value='```'+meta['id']+'```', inline=False)
      embed.add_field(name='URL', value='```'+url+'```', inline=False)
      await ctx.send(embed=embed)
    else:     
      await ctx.send("urlが有効ではありません")