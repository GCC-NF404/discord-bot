from discord.ext import commands
import discord,json,logging

CWD = str(__file__)[:-11]
#with open(CWD+'meta/embed.json','r',encoding='utf-8') as f:
#    j = json.load(f)
COLOR = 0xdddddd

class Help(commands.Cog):
    def __init__(self,ctx):
        with open(CWD+'meta/help.json','r',encoding='utf-8') as f:
            self.help=json.load(f)
            
    # Embedを返す
    def gen_help(self,title,description):
        return discord.Embed(title=title,color=COLOR,description=description)
    
    @commands.command()
    async def help(self,ctx,*args):
        if len(args) and args[0]!='help':
            if args[0] in self.help.keys():
                await ctx.send(embed=self.genHelp('ヘルプ:'+args[0],self.help[args[0]]))
            else:
                await ctx.send(embed=self.genHelp('[エラー]','コマンド`'+args[0]+'`のヘルプは存在しません'))
        else:
            embed = discord.Embed(title='ヘルプ',description='接頭辞「$」の後に各コマンドを入力して使用します。\n各コマンドの詳細は「$help [コマンド]」で確認する事が出来ます。',color=COLOR)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))