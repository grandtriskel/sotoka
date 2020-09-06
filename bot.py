import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import imdb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create bot object with $ as prefix
bot = commands.Bot(command_prefix="$")

# ping command
@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command()
async def watch(ctx, *args):
    ia = imdb.IMDb()
    response = ""
    movies = ia.search_movie(" ".join(args[:]))
    videospider_template = "https://videospider.stream/personal?key=F0l11HGLIM4oHOyI&video_id="
    if not movies:
        await channel.send("Can't find that one. Try another!")
    else:
        await ctx.channel.send(videospider_template + movies[0].movieID)

bot.run(TOKEN)
