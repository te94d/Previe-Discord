import discord
import re
import urllib.request
from yt_dlp import YoutubeDL

discord_token = 'MTAwNjQ0MzY0ODY2MzE2NzAyNg.GEjAQB.wrUwTZhxQb6gBmDkQ3AAvqGus3dQUeAvGTXBYI' # Discordbotのアクセストークン

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
    await message.channel.send("コマンド : 説明\n```>yt-mp3 url : youtubeの動画をmp3でDL\n>yt-mp4 url : youtubeの動画をmp4でDL\n>tw-mp3 url : twitterの動画をmp3でDL\n>tw-mp4 url : twitterの動画をmp4でDL```")
  
  #youtube mp3
  if msg.startswith(">yt-mp3") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp3でダウンロード中\n" + url)
      ydl_opts = {
                  'format': 'bestaudio/best',
                  'outtmpl':'/download/%(title)s.mp3',
                  }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
    else:
      await message.channel.send("urlが有効ではありません")
  
  #youtube mp4
  if msg.startswith(">yt-mp4") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp4でダウンロード中\n" + url)
      ydl_opts = {
                  'format': 'best',
                  'outtmpl':'/download/%(title)s.mp4',
                  }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
    else:
      await message.channel.send("urlが有効ではありません")

#twitter mp3
  if msg.startswith(">tw-mp3") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp3でダウンロード中\n" + url)
      ydl_opts = {
                  'format': 'bestaudio/best',
                  'outtmpl':'/download/%(title)s.mp3',
                  }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
    else:
      await message.channel.send("urlが有効ではありません")
  
  #twitter mp4
  if msg.startswith(">tw-mp4") == True:
    url = re.sub(r'.', '', msg, count = 8)
    if check_url(url) == True:
      await message.channel.send("mp4でダウンロード中\n" + url)
      ydl_opts = {
                  'format': 'best',
                  'outtmpl':'/download/%(title)s.mp4',
                  }
      with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      await message.channel.send("ダウンロードが完了しました")
    else:
      await message.channel.send("urlが有効ではありません")

client.run(discord_token)