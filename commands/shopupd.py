import os
from discord.ext import commands
from discord import Embed
from helpers.databaseFunctions import update_shop

class Shopupd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("shopupd.py is ready")

    @commands.command(aliases = [])
    async def shopupd(self, ctx):
        """text"""
        
        if str(ctx.message.author.id) != os.getenv("adminId"):
            return
        
        update_shop()
        
        embed = Embed(
            description = "text"
            )
        
        await ctx.message.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Shopupd(bot))