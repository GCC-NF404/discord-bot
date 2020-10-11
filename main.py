from discord.ext import commands
import discord
import logging

BOT = commands.Bot(command_prefix='$')
CWD = str(__file__)[:-7] # DISCORD-BOT ディレクトリの絶対パス(末尾に/を含む)

with open(CWD+'meta/admin.txt','r') as f:
    ADMINS = f.read().split('\n')

with open(CWD+'meta/token.txt','r') as f:
    TOKEN = f.read()

@BOT.event
async def on_ready():
    logging.info('botが起動しました')

BOT.run(TOKEN)