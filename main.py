from discord.ext import commands
import os,discord,logging


# 定数の定義

BOT = commands.Bot(command_prefix='$',help_command=None)
CWD = str(__file__)[:-7] # DISCORD-BOT ディレクトリの絶対パス(末尾に/を含む)

with open(CWD+'meta/admin.txt','r',encoding='utf-8') as f:
    ADMINS = f.read().split('\n')

with open(CWD+'meta/token.txt','r',encoding='utf-8') as f:
    TOKEN = f.read()

# コグを自動で取得する。システム関連は後々systemクラスとかで別ファイルに分けるかもしれない。
def load_cogs(cwd):
    cogs = os.listdir(CWD+'cog')
    for cog in cogs:
        if cog[len(cog)-3:]=='.py':
            BOT.load_extension('cog.'+str(cog[:-3]))

# botのイベント

@BOT.event
async def on_ready():
    logging.info('botが起動しました')

# botの実行

load_cogs(CWD)
BOT.run(TOKEN)