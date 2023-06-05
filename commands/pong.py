from discord.ext import commands
from discord import Embed
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
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Pong(bot))