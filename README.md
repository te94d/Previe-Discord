# Previe-Discord.py
リファクタリング版 [Previe-Discord.js](https://github.com/te94d/Previe-Discord.js)
### Previeって？  
Preserve + Video = Previe（プレビィー）  
SNSプラットフォームの動画をローカルに保存してくれるBot
## 開発環境
![](https://img.shields.io/badge/python-v3.10.6-blue)
![](https://img.shields.io/badge/pip-v22.2.2-blue)
![](https://img.shields.io/badge/discord.py-v1.7.3-blue)
![](https://img.shields.io/badge/yt--dlp-v2022.8.8-blue) 
## ビルド
[python3](https://www.python.org/) をインストール
### パッケージのインストール
```
$ pip install -U discord
$ pip install yt-dlp
$ pip install python-dotenv
```
[ffmpeg](https://ffmpeg.org/) にアクセスしwindowsビルドのものをダウンロードする。  
ダウンロードしたファイルを解凍し、binフォルダの中にある`ffmpeg.exe`を`ytdl.py`と同じ階層に置いておく。  
`.env`ファイルを作成し`.env.sample`の中身を記述する。
```
discord_token = <token>
```
### 実行
```
$ python main.py
```
<!--## できること
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
-->