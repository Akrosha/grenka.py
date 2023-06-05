import os
from discord.ext import commands
from discord import Embed
from helpers.databaseFunctions import database

class Dexec(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("dexec.py is ready")

    @commands.command(aliases = [])
    async def dexec(self, ctx, *args):
        """text"""
        
        if str(ctx.message.author.id) != os.getenv("adminId"):
            return
        
        r = database.execute(" ".join(args), fetchall = True)
        
        embed = Embed(
            description = r
            )
        
        await ctx.message.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Dexec(bot))