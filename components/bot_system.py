import discord

class BotSystem():
    def __init__(self):
        self.pError = '```[権限エラー] todo:reload を実行する権限が有りません```'   
    
    def is_exist_logch(self,ctx):
        return discord.utils.get(ctx.guild.channels, name='bot-log')

    def is_admin(self,ctx):
        return ctx.author in [i for i in ctx.guild.members if i.top_role.id == discord.utils.get(ctx.guild.roles, name='管理者').id]