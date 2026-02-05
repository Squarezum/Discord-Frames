import discord
import random
import logging
import os
import pathlib

from dotenv import load_dotenv
from discord.ext import commands



load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='mgs.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# The bot's prefix (duh)
bot = commands.Bot(command_prefix='!', intents=intents)

# Prints this out when the bot is online
@bot.event
async def on_ready():
    print(f"Kept you waiting, huh?")

# The main command, change pathlib.Path('frames') to the folder you're using
@bot.command()
async def frame(ctx):
    folder = pathlib.Path('frames')
    frames = [x for x in folder.iterdir()
              if x.is_file() and x.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.webp')]
    if not frames:
        return await ctx.send("Eeerm there's nothing in the folder I'm using")
    frame_chosen = random.choice(frames)
    await ctx.send(f"Frame {frame_chosen.stem} out of {len(frames)}", file=discord.File(str(frame_chosen), filename=frame_chosen.name))

bot.run(token, log_handler=handler, log_level=logging.DEBUG)