from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import trueRandom, getStrings

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("random.py is ready")

    @commands.command(aliases = ["rand", "r", "рандом", "ранд", "р"])
    async def random(self, ctx, *args):
        """выдает случайное число"""
        if len(args) == 1:
            try:
                text = trueRandom(two = int(args[0]))
            except:
                text = getStrings(str_id = "commands.random.1args")
        elif len(args) == 2:
            try:
                text = trueRandom(one = int(args[0]),two = int(args[1]))
            except:
                text = getStrings(str_id = "commands.random.2args")
        elif len(args) > 2:
            try:
                text = trueRandom(one = int(args[0]),two = int(args[1]),c = int(args[2]))
            except:
                text = getStrings(str_id = "commands.random.3args")
        else:
            text = trueRandom()
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Random(bot))