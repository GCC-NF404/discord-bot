import discord

class BotSystem():
    def is_admin(self,ctx):
        return ctx.author in [i for i in ctx.guild.members if i.top_role.id == discord.utils.get(ctx.guild.roles, name='管理者').id]