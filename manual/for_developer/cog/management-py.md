# `management.py` のマニュアル

## 概要

`management.py` はユーザー管理コマンドを提供する
[ `discord.ext.commands.Cog()` ](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=cog#discord.ext.commands.Cog) 
のサブクラスです。\
`main.py` の `_load_cogs(cog_dir)_` 内にある
[ `BOT.load_extension()` ](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension)
によって読み取られることで、BOT インスタンス の追加コマンドとして動作します。

## 定数

- `COLOR`　→　bot が送信する埋め込み([`discord.Embed()`](https://discordpy.readthedocs.io/ja/latest/api.html?highlight=discord%20embed#discord.Embed))の`color`引数に渡す値です。

## クラス `Management(commands.Cog)`

***
### _\_\_init\_\_(self, ctx)_
`Management` クラスのコンストラクターです。現在は何も設定されていません。(`pass`)

***
### _rolecheck(self, ctx)_
`$rolecheck` コマンドが実行されたときに呼び出されます。\
「管理者」「部員」「先生」のいずれのロールにも所属していないユーザーを探し、チャットに結果を送信します。

## 関数

***
### _setup(bot)_
`Management` クラスを BOT インスタンスに格納するために必要な関数です。\
`main.py` の `load_cogs(cog_dir)` 内にある
[ `BOT.load_extension()` ](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension)
によって呼ばれます。