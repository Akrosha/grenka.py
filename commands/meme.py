import bs4
import random
import requests

from discord.ext import commands
from helpers.randomFunctions import getStrings

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("meme.py is ready")

    @commands.command(aliases = ["мем"])
    async def meme(self, ctx):
        """показывает мемы"""
        
        if random.randint(0,100) > 1:
            quote = requests.get('https://www.anekdot.ru/random/mem/')
            parsed = bs4.BeautifulSoup(quote.text, "html.parser")
            select = parsed.select('.text')
            try:
                text = random.choice(select).find("img").get("src")
            except:
                text = getStrings(str_id = "commands.meme.error")
        else:
            text = "https://media.discordapp.net/attachments/468809945882689547/1089064511060836362/fgsfds.png"
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Meme(bot))