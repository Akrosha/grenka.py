from discord.ext import commands
from helpers.randomFunctions import getStrings

class Pong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py is ready")

    @commands.command(aliases = ["понг"])
    async def pong(self, ctx):
        """пинг!"""
        text = getStrings(str_id = "commands.pong")
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Pong(bot))