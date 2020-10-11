from discord.ext import commands
import os,discord,logging

BOT = commands.Bot(command_prefix='$')
CWD = str(__file__)[:-7] # DISCORD-BOT ディレクトリの絶対パス(末尾に/を含む)

with open(CWD+'meta/admin.txt','r') as f:
    ADMINS = f.read().split('\n')

with open(CWD+'meta/token.txt','r') as f:
    TOKEN = f.read()

def load_cogs(cwd):
    cogs = os.listdir(CWD+'cog')
    for cog in cogs:
        if cog[len(cog)-3:]=='.py':
            BOT.load_extension('cog.'+str(cog[:-3]))

@BOT.event
async def on_ready():
    logging.info('botが起動しました')

load_cogs(CWD)
BOT.run(TOKEN)