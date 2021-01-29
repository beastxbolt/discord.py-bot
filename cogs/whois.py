import discord
import asyncio
from discord.ext import commands


class whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def whois(self, ctx, member:discord.Member):

        if not member:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

            embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_author(name="User Info: ")
            embed.add_field(name="ID:", value=member.id, inline=False)
            embed.add_field(name="User Name:",value=member.display_name, inline=False)
            embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
            embed.add_field(name="Current Status:", value=str(member.status).title(), inline=False)
            embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
            embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
            embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
            embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=False)
            embed.add_field(name="Top Role:", value=member.top_role, inline=False)
            embed.add_field(name="Bot?:", value=member.bot, inline=False)
            await ctx.send(embed=embed)
            return



def setup(bot):
    bot.add_cog(whois(bot))