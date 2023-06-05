from discord.ext import commands
from discord import Embed
from time import time

class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("time.py is ready")

    @commands.command(aliases = ["время"])
    async def time(self, ctx):
        """показывает время"""
        text = f"<t:{int(time())}:F>"
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Time(bot))