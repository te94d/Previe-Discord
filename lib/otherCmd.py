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
    embed = discord.Embed()
    embed.color = 0x8ED1E0
    embed.title = 'Commands'
    embed.description = 'Previeで使用できるコマンド一覧'
    embed.set_author(name='Previe', url='https://github.com/te94d/Previe-Discord',
      icon_url=self.bot.user.avatar_url)
    #embed.set_image(
    #  url = 'https://'
    #)
    embed.add_field(name='DLコマンド', value='```>mp3 [url] : youtubeとtwitterの音声をmp3でDL``````>mp4 [url] : youtubeとtwitterの動画をmp4でDL```\nDLが開始すると'+UnicodeDownload+'が付与されます\nDLが完了すると'+UnicodeCheck+'が付与されます\n※DLしたファイルの2次配布は止めましょう\n', inline=False)
    embed.add_field(name='動画の詳細表示', value='```>info [url] : youtubeとtwitterの動画のコンテンツ関連の情報を表示``````>codec [url] : youtubeの動画のコーデック関連の情報を表示```', inline=False)
    embed.add_field(name='管理用コマンド', value='```>rem [削除したいメッセージ数] : 指定したメッセージ数を削除```', inline=False)
    embed.set_footer(text="vertion 1.2", icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def rem(self, ctx, target:int):
    channel = ctx.message.channel
    deleted = await channel.purge(limit=target)
    await ctx.send(f"{len(deleted)}件のメッセージを削除しました！")
