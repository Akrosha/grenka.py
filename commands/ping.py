from discord.ext import commands
from helpers.randomFunctions import getStrings

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py is ready")

    @commands.command(aliases = ["пинг", ">"])
    async def ping(self, ctx):
        """понг!"""
        text = getStrings(str_id = "commands.ping")
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Ping(bot))