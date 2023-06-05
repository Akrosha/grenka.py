import os, json
from discord.ext import commands
from discord import Embed
from helpers.databaseFunctions import database, var_type

class Patch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("patch.py is ready")

    @commands.command(aliases = [])
    async def patch(self, ctx):
        """text"""
        
        if str(ctx.message.author.id) != os.getenv("adminId"):
            return
        
        for dataname in ["shop"]:
            with open(f"database/{dataname}.json", "r") as file:
                dataset = json.load(file)
            
            for dataone in dataset.values():
                keys = ", ".join([key for key in dataone.keys()])
                values = ", ".join([var_type(value) for value in dataone.values()])
                database.execute(f"INSERT INTO {dataname} ({keys}) VALUES ({values})")
        
        embed = Embed(
            description = "text"
            )
        
        await ctx.message.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Patch(bot))