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
            try:
                quote = requests.get(random.choice(getStrings(str_id = "commands.meme.origin").split(";")))
                parsed = bs4.BeautifulSoup(quote.text, "html.parser")
                select = parsed.findAll("img")
                images = [i["src"] for i in select if i["src"] != "https://i.pinimg.com/75x75_RS/59/0e/21/590e2138f7e9290441d9abb87d966a45.jpg"]
                text = random.choice(images)
            except:
                text = getStrings(str_id = "commands.meme.error").format(filler = random.choice(getStrings(str_id = "commands.meme.filler").split(";")))
        else:
            text = random.choice(getStrings(str_id = "commands.meme.legendary").split(";"))
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Meme(bot))


"""
            quote = requests.get('https://www.anekdot.ru/random/mem/')
            parsed = bs4.BeautifulSoup(quote.text, "html.parser")
            select = parsed.select('.text')
            try:
                text = random.choice(select).find("img").get("src")
            except:
                text = getStrings(str_id = "commands.meme.error").format(filler = random.choice(getStrings(str_id = "commands.meme.filler").split(";")))
"""