import os
import bs4
import random
import requests

from re import findall
from discord.ext import commands
from helpers.randomFunctions import getStrings

class TestMeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("testmeme.py is ready")

    @commands.command(aliases = ["tm"])
    async def testmeme(self, ctx):
        """показывает мемы"""
        
        if random.randint(0,100) > 1:
            try:
                quote = requests.get(f"https://safebooru.org/index.php?page=post&s=list&tags=meme+english_commentary&pid={random.randint(0,1024)}")
                parsed = bs4.BeautifulSoup(quote.text, "html.parser")
                select = parsed.findAll("img")
                images = [i["src"] for i in select if i["src"].startswith("https://")]
                link = random.choice(images)
                
                wish = findall("jpg\?[0-9]+", link)
                quote = requests.get(f"https://safebooru.org/index.php?page=post&s=view&id={wish[0][4:]}")
                parsed = bs4.BeautifulSoup(quote.text, "html.parser")
                select = parsed.findAll("img")
                images = [i["src"] for i in select if i["src"].startswith("https://")]
                text = random.choice(images)
            except:
                text = getStrings(str_id = "commands.meme.error").format(filler = random.choice(getStrings(str_id = "commands.meme.filler").split(";")))
        else:
            text = random.choice(getStrings(str_id = "commands.meme.legendary").split(";"))
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(TestMeme(bot))