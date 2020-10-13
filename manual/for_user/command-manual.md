# コマンドマニュアルへようこそ！
このドキュメントでは、当 bot のコマンドと使いかたについて解説します。

## コマンドの書き方
当 bot のコマンドは `$` をコマンドの先頭に付けて書きます。\
たとえば、helpコマンドを実行したい場合は以下の例のようにチャットに打ち込んでみましょう！\
`$` マークと `help` の間にスペースは入れずに入力してください。\
また、コマンドにオプションがある場合は**半角スペース**に続けてオプションを入力します。\
\
▼オプションがない場合の書き方の例
```
$help
```
▼オプションがある場合の書き方の例
```
$help rolecheck
```

## ヘルプを表示するコマンド
bot のヘルプを表示します。コマンドの使いかたが分からなくなった時は積極的に使ってみましょう。

### 文法
```
$help [調べたいコマンド]
```
`$rolecheck` コマンドについて調べたい場合は以下のように入力します
```
$help rolecheck
```

## サーバーを管理するコマンド
サーバーの管理を行うために使うコマンドです。一般のユーザーには必要のない機能かもしれません。\
一部の機能は実行時に管理者権限(discordのロールとは無関係)を必要とします。
***

### _$rolecheck_ 
「管理者」「部員」「先生」のどのロールにも所属していないユーザーの一覧を表示します。\
新入部員など、権限をつけていないユーザーを発見するために使用します。
#### 文法
オプションはありません。
```
$rolecheck
```