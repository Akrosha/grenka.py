from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings

class Test_String(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("test_string.py is ready")

    @commands.command(aliases = ["ts", "t_s"])
    async def test_string(self, ctx, args):
        """выдает локализацию строки по id"""
        text = getStrings(str_id = args)
        if text == "NaN":
            text = getStrings(str_id = "commands.test_string.missing")
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Test_String(bot))