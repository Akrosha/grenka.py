raise SystemExit

import os
import re
import json
import asyncio
import discord
import requests

from time import time
from host import runapp
from datetime import datetime
from threading import Thread
from discord.ext import commands
from discord import Embed
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
        text = f"load module: commands.{extension}"
    except:
        text = f"module not exists: commands.{extension}"
    embed = Embed(description = text[:2000])
    await ctx.message.reply(embed = embed)

@bot.command()
async def unload(ctx, extension):
    if str(ctx.message.author.id) != adminId:
        return
    try:
        await bot.unload_extension(f"commands.{extension}")
        text = f"unload module: commands.{extension}"
    except:
        text = f"module not exists: commands.{extension}"
    embed = Embed(description = text[:2000])
    await ctx.message.reply(embed = embed)

@bot.command()
async def reload(ctx, extension):
    if str(ctx.message.author.id) != adminId:
        return
    try:
        await bot.unload_extension(f"commands.{extension}")
        await bot.load_extension(f"commands.{extension}")
        text = f"reload module: commands.{extension}"
    except:
        text = f"module not exists: commands.{extension}"
    embed = Embed(description = text[:2000])
    await ctx.message.reply(embed = embed)

@bot.command()
async def exit(ctx):
    if str(ctx.message.author.id) != adminId:
        return
    text = f"bye bye"
    embed = Embed(description = text[:2000])
    await ctx.message.reply(embed = embed)
    
    apiq = "https://grenkapy.akrosha.repl.co/killthisdashitsuka/"
    data = {
        "api_key": os.getenv("api_key")
    }
    requests.get(apiq, data = json.dumps(data))
    raise SystemExit

@bot.event
async def on_message(message):
    try:
        guild = message.guild.name
        gid = message.guild.id
    except:
        guild = None
        gid = None
    text = "$t {time}\n$usr: {user}\n {userId}\n$gid: {guild}\n {gid}\n{ind}\n{content}\n{ind}\n{raww}".format(
        time = datetime.fromtimestamp(time()).strftime("%d.%m.%Y %H:%M:%S"),
        user = message.author,
        userId = message.author.id,
        guild = guild,
        gid = gid,
        content = message.clean_content,
        raww = f"u{message.raw_mentions}\nc{message.raw_channel_mentions}\nr{message.raw_role_mentions}\na{message.attachments}\ne{[i.to_dict() for i in message.embeds]}",
        ind = "="*13
        )
    logger(text[:2000])
    
    if not message.content.startswith(">") or message.content.startswith("> "):
        return
    async with message.channel.typing():
        all_commands = bot.all_commands
        cmd = message.content[1:].split()[0]
        if cmd not in all_commands.keys():
            simily = similarList(cmd, all_commands.keys())
            if simily:
                text = f"{cmd}: {getStrings(str_id = 'main.no_command')} - {simily}"
                embed = Embed(description = text[:2000])
                await message.reply(embed = embed)
                return
        await bot.process_commands(message)

# мейн
asyncio.run(load_extensions())

def runbot():
    bot.run(os.getenv("token"))

tahread1 = Thread(target=runapp)
#tohread2 = Thread(target=runbot)

tahread1.start()
#tohread2.start()

runbot()
#runapp()


"""
while True:
    try:
        keep_alive()
        bot.run(os.getenv("token"))
    except discord.errors.HTTPException:
        print("blocked by 429: restart....")
        os.system("kill 1")
"""