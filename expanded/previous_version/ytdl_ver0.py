import discord
import re
import os
import urllib.request
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
from tkinter import filedialog

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

# checkマーク
UnicodeEmoji = "\N{White Heavy Check Mark}"

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  msg = message.content
  if message.author.bot:
    return
    
  if msg == ">help":
    await message.channel.send("コマンド : 説明\n```>yt-mp3 url : youtubeの動画をmp3でDL\n>yt-mp4 url : youtubeの動画をmp4でDL\n>tw-mp3 url : twitterの動画をmp3でDL\n>tw-mp4 url : twitterの動画をmp4でDL```※DLしたファイルの2次配布は止めましょう")
  
  #youtube mp3
  if msg.startswith(">yt-mp3") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp3でダウンロードを開始します")
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp3", ".mp3")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        initialfile = "youtube", # 名前の初期値
        defaultextension = "mp3"
        )
      print(filename)
      ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
      await message.add_reaction(UnicodeEmoji)
    else:
      await message.channel.send("urlが有効ではありません")
  
  #youtube mp4
  if msg.startswith(">yt-mp4") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp4でダウンロードを開始します")
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp4", ".mp4")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        initialfile = "youtube", # 名前の初期値
        defaultextension = "mp4"
        )
      print(filename)
      ydl_opts = {
        'format': 'best',
        'outtmpl': filename,
        }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
      await message.add_reaction(UnicodeEmoji)
    else:
      await message.channel.send("urlが有効ではありません")

#twitter mp3
  if msg.startswith(">tw-mp3") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp3でダウンロードを開始します")
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp3", ".mp3")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        initialfile = "twitter", # 名前の初期値
        defaultextension = "mp3"
        )
      print(filename)
      ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
      await message.add_reaction(UnicodeEmoji)
    else:
      await message.channel.send("urlが有効ではありません")
  
  #twitter mp4
  if msg.startswith(">tw-mp4") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp4でダウンロードを開始します")
      filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("mp4", ".mp4")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        initialfile = "twitter", # 名前の初期値
        defaultextension = "mp4"
        )
      print(filename)
      ydl_opts = {
        'format': 'best',
        'outtmpl': filename,
        }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
      await message.add_reaction(UnicodeEmoji)
    else:
      await message.channel.send("urlが有効ではありません")

load_dotenv()
discord_token = os.getenv('discord_token')
client.run(discord_token)