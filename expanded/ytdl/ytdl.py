import discord
import re
import urllib.request


discord_token = 'MTAwNjQ0MzY0ODY2MzE2NzAyNg.GAfOzN.NmwHUSCzqssnNFFqzs5sIwtZkCSYCuT8g5vu8Q' # Discordbotのアクセストークン
youtube_url = 'https://www.youtube.com/watch?v=FIw-HUP7XK0' # youtubeのURLを指定

# urlチェック関数
def check_url(url):
  flag = True
  if re.match(r"^https?:\/\/", url):
    try:
      f = urllib.request.urlopen(url)
      f.close()
      if ("youtube" in url) == True or ("youtu.be" in url) == True:
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
    
  if msg == "!cmd":
    await message.channel.send("!dl url\nyoutubeの動画をDL")
  
  if msg.startswith("!dl") == True:
    url = re.sub(r'.', '', msg, count = 4)
    if check_url(url) == True:
      await message.channel.send("downloadします\n" + url)
    else:
      await message.channel.send("urlが有効ではありません")

client.run(discord_token)