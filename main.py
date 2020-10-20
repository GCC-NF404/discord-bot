from discord.ext import commands
from components.system import BotSystem
import os,discord,logging

BOT = commands.Bot(command_prefix='$',help_command=None,intents=discord.Intents.all())
BOTSYS = BotSystem()
CWD = str(__file__)[:-7]
COLOR = 0xdddddd
TOKEN = os.environ.get('TOKEN')

cogs = os.listdir(CWD + '/cog')
for cog in cogs:
    if(cog[len(cog)-3:] == '.py'):
        BOT.load_extension('cog.' + str(cog[:-3]))

@BOT.event
async def on_ready(): logging.info('botが起動しました。')

@BOT.command()
async def reload(ctx):
    if BOTSYS.is_admin(ctx):
        cogs = os.listdir(CWD + 'cog')
        allcogs = ''
        for cog in cogs:
            if(cog[len(cog)-3:] == '.py'):
                BOT.reload_extension('cog.' + str(cog[:-3]))
                allcogs = allcogs + ( 'cog.' + str(cog[:-3]) + '\n')
        em = discord.Embed(color=0xff7f1e)
        em.add_field(name='再読込されたコグ一覧',value=allcogs)
        await ctx.send(embed=em)
    else:
        await ctx.send('```[権限エラー] todo:reload を実行する権限が有りません```')

@BOT.event
async def on_command_error(ctx,error):
    channel = discord.utils.get(ctx.guild.channels, name='bot-log')
    embed = discord.Embed(title='エラー情報', description='', color=COLOR)
    embed.add_field(name='該当コマンド', value='```'+str(ctx.message.content)+'```', inline=False)
    embed.add_field(name='該当チャンネル', value='```'+str(ctx.message.channel)+'```')
    embed.add_field(name='発生エラー', value='```'+str(error)+'```', inline=False)
    if channel is not None:
        await channel.send(embed=embed)

BOT.run(TOKEN)