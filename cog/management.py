from discord.ext import commands
import discord,logging

COLOR = 0xdddddd

class Management(commands.Cog):
    def __init__(self,ctx):
        pass

    @commands.command()
    async def rolecheck(self,ctx):
        guild = ctx.guild
        role_admin = discord.utils.get(guild.roles, name='管理者').id
        role_stu = discord.utils.get(guild.roles, name='部員').id
        role_tea = discord.utils.get(guild.roles, name='先生').id
        member = []
        for i in guild.members:
            if not i.top_role.id in [role_admin,role_stu,role_tea] and not i.bot:
                member.append(i.name)
        if member!=[]:
            embed = discord.Embed(title='適切なロールが付与されていないメンバー',description='```'+'\n'.join(['・'+i for i in member])+'```',color=COLOR)
        else:
            embed = discord.Embed(title='適切なロールが付与されていないメンバー',description='```現在、ロールが付与されていないメンバーはいません。```',color=COLOR)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Management(bot))
    logging.info('コグ management のロードを終了しました。')