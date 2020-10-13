from discord.ext import commands
import os,discord,logging

BOT = commands.Bot(command_prefix='$',help_command=None,intents=discord.Intents.all())
CWD = str(__file__)[:-7]
COLOR = 0xdddddd
with open(CWD+'meta/admin.txt','r',encoding='utf-8') as f: ADMINS = f.read().split('\n')
with open(CWD+'meta/token.txt','r',encoding='utf-8') as f: TOKEN = f.read()

def load_cogs(cog_dir):
    logging.info('コグの読み込みを開始します。')
    cogs = os.listdir(cog_dir+'cog')
    for cog in cogs:
        if cog[len(cog)-3:]=='.py':
            BOT.load_extension('cog.'+str(cog[:-3]))
    logging.info('コグの読み込みが完了しました。')

@BOT.event
async def on_ready(): logging.info('botが起動しました。')

@BOT.event
async def on_command_error(ctx,error):
    channel = discord.utils.get(ctx.guild.channels, name='bot-log')
    embed = discord.Embed(title='エラー情報', description='', color=COLOR)
    embed.add_field(name='該当コマンド', value='```'+str(ctx.message.content)+'```', inline=False)
    embed.add_field(name='該当チャンネル', value='```'+str(ctx.message.channel)+'```')
    embed.add_field(name='発生エラー', value='```'+str(error)+'```', inline=False)
    if channel is not None:
        await channel.send(embed=embed)

load_cogs(CWD)
BOT.run(TOKEN)