import discord
import asyncio
from discord.ext import commands



class humans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def humans(self, ctx):

        embed = discord.Embed(title=f"There are {len([member for member in ctx.guild.members if not member.bot])} humans alive in {ctx.guild.name}", colour=0xffff00, timestamp=ctx.message.created_at)
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    


def setup(bot):
    bot.add_cog(humans(bot))