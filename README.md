# iroiroBot
discord.py v2.0.0a でのBotサンプル集
カテゴリごとにCogに分けてあります  
1つのサーバーでのみ使用する想定でスラッシュコマンドなどはギルド指定してあります

## 使い方
* discord botアカウントを作成
* Botの設定画面でトークンを取得
* その下のPresence Intentはオンに設定してください
* OAuth2設定 > URL Generatorで Botを選択、以下をチェックして生成
    * Read Messages/View Channels
    * Send Messages
* 生成したURLから使用するサーバーに招待

* 一部のCogを使用しない場合は、`app.py`のCog読み込み部分をコメントアウトしてください。  

* settings.py.template を参考に settings.pyを作ってください。  
※settings.pyの設定について、Cogをコメントアウトしている場合はそのCog用の設定値は不要になります。


* discord.py 2.0.0aのインストール

```
pip install git+https://github.com/Rapptz/discord.py
```

* 起動はapp.pyを実行してください

```
python app.py
```

* discordのサーバー設定 > 連携サービス からbotが持っているコマンドを確認・権限の変更ができます

## デバッグ
スラッシュコマンドを実装していると反映されなかったりすることがあります  
クライアント再起動でなおることもあります  
それでもダメだった場合は以下を試してみてください
```
pythono reset_commands.py
```
なお、スラッシュコマンドは対象ギルドを指定しないとグローバルコマンドになって反映に時間がかかります(このサンプルではすべてギルド指定してあります)

## サンプルの機能一覧
* `basic_command.py` 指定プレフィックス('!'など)で始まる文字列に反応する
* `basic_listener.py` on_messageで特定の言葉に反応する
* `images.py` 画像を返す(スラッシュコマンド)
* `list_reactions.py` 右クリックしたメッセージのリアクションを一覧にして指定のURLにポストする
* `omikuji.py` おみくじ(スラッシュコマンド)
* `random_from_vc.py` 呼び出した人の接続しているボイスチャンネルからランダムに人を選んで返す
* `vc_log.py` ボイスチャンネル接続ログを指定のチャンネルに書き込む