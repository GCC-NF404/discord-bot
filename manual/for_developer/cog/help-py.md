# `cog/help.py` のマニュアル

## 概要
`help.py` はヘルプコマンドを提供する
[ `discord.ext.commands.Cog()` ](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=cog#discord.ext.commands.Cog) 
のサブクラスです。\
`main.py` の `_load_cogs(cog_dir)_` 内にある
[ `BOT.load_extension()` ](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension)
によって読み取られることで、BOT インスタンス の追加コマンドとして動作します。

## 定数
- `CWD`　→　`main.py` が存在するディレクトリの絶対パスです。
- `COLOR`　→　bot が送信する埋め込み([`discord.Embed()`](https://discordpy.readthedocs.io/ja/latest/api.html?highlight=discord%20embed#discord.Embed))の`color`引数に渡す値です。

## クラス Help(commands.Cog)

### _インスタンス変数_
- `self.help`　→　ヘルプコマンドが実行された際にチャットに送信する定型文の表です。

***
### _\_\_init(self, ctx)\_\__
`Help` クラスのコンストラクターです。

***
### _gen_help(self, title, description)_
`$help` コマンドの実行結果を埋め込み
([`discord.Embed()`](https://discordpy.readthedocs.io/ja/latest/api.html?highlight=discord%20embed#discord.Embed))
形式で返します。

***
### _help(self, ctx, *args)_
`$help` コマンドが実行されたときに呼び出されます。\
オプション(任意のコマンド名)が与えられた場合はそのコマンドのヘルプ定型文を `self.help` から探し、存在するコマンドである場合は該当のヘルプを、そうでない場合はエラー文をチャットに返信します。

## 関数

***
### _setup(bot)_
`Help` クラスを BOT インスタンスに格納するために必要な関数です。\
`main.py` の `load_cogs(cog_dir)` 内にある
[ `BOT.load_extension()` ](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension)
によって呼ばれます。