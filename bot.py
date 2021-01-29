import discord
import asyncio
from discord.ext import commands

prefix = "+"
bot = commands.Bot(command_prefix = prefix)

TOKEN = "BOT TOKEN HERE"


@bot.event
async def on_ready():
    print("Subscribe the channel :)")


@bot.command()
async def ping(ctx):
    await ctx.send("PONG!")





bot.run(TOKEN)
