# discord-bot
discord botをつくっていく随時機能追加していきたい
## できること
### ytdl.py
| コマンド | 説明 |
|:--------------|:-----------|
| >mp3 [url] | youtubeやtwitterの動画をmp3でDL |
| >mp4 [url] | youtubeやtwitterの動画をmp4でDL |
| >info [url] | youtubeとtwitterの動画のコンテンツ関連の情報を表示 |
| >codec [url] | youtubeの動画のコーデック関連の情報を表示 |
### otherCmd.py
| コマンド | 説明 |
|:--------------|:-----------|
| >help | 各コマンドの表示 |
| >rem [n] | 指定したメッセージ数を削除 |
## 開発環境
- python 3.10.6
- pip 22.2.2
- discord.py 1.7.3
- yt-dlp 2022.8.8
## インストール
```
$ pip install -U discord
$ pip install yt-dlp
$ pip install python-dotenv
```
ffmpegのページにアクセスしwindowsビルドのものをダウンロードする。  
ダウンロードしたファイルを解凍し、binフォルダの中にある"ffmpeg.exe"をytdl.pyファイルと同じ階層に置いておく。  
.envファイルを作成し、.env.sampleの中身を記述する。