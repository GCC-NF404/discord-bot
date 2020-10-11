from discord.ext import commands
import discord,json,logging

CWD = str(__file__)[:-12]

class Help(commands.Cog):
    def __init__(self):
        with open(CWD+'meta/help.json','r',encoding='utf-8') as f:
            self.help=json.load(f)
            
    # Embedを返す
    def gen_help(self,title,description):
        return discord.Embed(title=title,color=0xdddddd,description=description)

def setup(bot):
    bot.add_cog(Help(bot))