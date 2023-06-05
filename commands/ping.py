from discord.ext import commands
from discord import Embed
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
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))