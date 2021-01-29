import discord
import asyncio
from discord.ext import commands



class unload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, module_name = None):

        try:
            if module_name is None:
                embed = discord.Embed(title="Enter Module Name To Unload!", colour=0xff0000, timestamp=ctx.mesage.created_at)
                await ctx.send(embed=embed)


            else:
                self.bot.unload_extension(f"cogs.{module_name}")
                embed2 = discord.Embed(title=f"{module_name} Module Unloaded Successfully!", colour=0x00ff00, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
        except:
            embed3 = discord.Embed(title=f"Failed To Unload {module_name} Module!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)



def setup(bot):
    bot.add_cog(unload(bot))