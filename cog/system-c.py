import sys
sys.path.append(str(__file__)[:-16])

from discord.ext import commands
from components.bot_system import BotSystem
import os,sys,discord,logging,subprocess

BOTSYS = BotSystem()

class System(commands.Cog):
    def __init__(self,ctx):
        pass

    @commands.command()
    async def reboot(self,ctx):
        if BOTSYS.is_admin(ctx):
            channel = BOTSYS.is_exist_logch(ctx)
            if channel is not None:
                await ctx.send('```botを再起動します。```')
            subprocess.call('git','pull','origin','master')
            os.execl(sys.executable, 'python3', '-B', str(__file__)[:-16]+'/main.py')
        else:
            await ctx.send(BOTSYS.pError)

def setup(bot):
    bot.add_cog(System(bot))
    logging.info('コグ system のロードを終了しました。')