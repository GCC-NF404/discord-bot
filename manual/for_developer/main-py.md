# `main.py` のマニュアル

## 概要
`main.py` は bot の実行部分をつかさどるファイルです。\
bot を起動する際はこのファイルを`nohup`などで実行します。

## 定数
- `BOT`　→　[`discord.ext.commands.Bot()`](https://discordpy.readthedocs.io/ja/latest/ext/commands/api.html?highlight=bot#discord.ext.commands.Bot) のインスタンスです。
- `CWD`　→　`main.py` が存在するディレクトリの絶対パスです。
- `COLOR`　→　bot が送信する埋め込み([`discord.Embed()`](https://discordpy.readthedocs.io/ja/latest/api.html?highlight=discord%20embed#discord.Embed))の`color`引数に渡す値です。(2020-10-12 現在、公式リファレンスが  ~~`colour`と誤字していますが`color`が正しい名称です~~ イギリス英語のなまり(?)のようです。お互いがお互いのエイリアスなので、引数を渡すときは`colour` でも `color` でも問題ありません)
- `TOKEN`　→　bot を起動するために必要な token です。

## 関数

***
### _on_ready()_
bot が起動した際に呼ばれるイベントです。\
起動時に行いたい操作がある場合はこの中に追記してください。

***
### _reload(ctx)_
`$reload`が実行されたときに呼ばれます。\
実行した人が「管理者」のロールを持っているときのみ cog をリロードします。

***
### _on_command_error(ctx, error)_
サーバー内でエラーが発生した際に呼ばれるイベントです。\
現在はエラーが発生した際にエラーメッセージを送信するプログラムが設定されています。\
エラーを受け取るためには `bot-log` という名前が付いたチャンネルがサーバー内に設置されている必要があります。