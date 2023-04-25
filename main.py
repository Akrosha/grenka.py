import os
import re
import json
import asyncio
import discord

from time import time
from host import keep_alive
from datetime import datetime
from discord.ext import commands
from helpers.randomFunctions import similarList, getStrings, logger

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

prefix = ">"
adminId = "468719193798213654"

# либа бота
bot = commands.Bot(command_prefix=prefix, description="no desc", intents=intents, help_command=None)

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Jodin: Jawelin combustion"))
    print("woah", bot.user)

@bot.command()
async def load(ctx, extension):
    if str(ctx.message.author.id) != adminId:
        return
    try:
        await bot.load_extension(f"commands.{extension}")
        await ctx.message.reply(f"load module: commands.{extension}")
    except:
        await ctx.message.reply(f"module not exists: commands.{extension}")

@bot.command()
async def unload(ctx, extension):
    if str(ctx.message.author.id) != adminId:
        return
    try:
        await bot.unload_extension(f"commands.{extension}")
        await ctx.message.reply(f"unload module: commands.{extension}")
    except:
        await ctx.message.reply(f"module not exists: commands.{extension}")

@bot.command()
async def reload(ctx, extension):
    if str(ctx.message.author.id) != adminId:
        return
    try:
        await bot.unload_extension(f"commands.{extension}")
        await bot.load_extension(f"commands.{extension}")
        await ctx.message.reply(f"reload module: commands.{extension}")
    except:
        await ctx.message.reply(f"module not exists: commands.{extension}")

@bot.event
async def on_message(message): 
    text = "$t {time}\n$usr: {user}\n {userId}\n{ind}\n{content}\n{ind}\n{img}".format(
        time = datetime.fromtimestamp(time()).strftime("%d.%m.%Y %H:%M:%S"),
        user = message.author,
        userId = message.author.id,
        content = message.content,
        img = message.attachments,
        ind = "="*13
        )
    logger(text[:2000])
    
    if message.content.startswith(">"):
        all_commands = bot.all_commands
        cmd = message.content[1:].split()[0]
        if cmd not in all_commands.keys():
            simily = similarList(cmd, all_commands.keys())
            if simily:
                text = f"{cmd}: {getStrings(str_id = 'main.no_command')} - {simily}"
                await message.reply(text[:2000])
                return
    
    await bot.process_commands(message)

# мейн
asyncio.run(load_extensions())
while True:
    try:
        keep_alive()
        bot.run(os.getenv("token"))
    except discord.errors.HTTPException:
        print("blocked by 429: restart....")
        os.system("kill 1")
