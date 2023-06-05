import os
from discord.ext import commands
from discord import User, Embed
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user, edit_nplayer
from helpers.rpgengineFunctions import add_item

class Gi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("gi.py is ready")

    @commands.command(aliases = [])
    async def gi(self, ctx, user: User, species: str = None, count: int = 1):
        """выплатить грибы другому"""
        
        if str(ctx.message.author.id) != os.getenv("adminId"):
            return
        
        if user:
            player_id = str(user.id)
        else:
            player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if player and species:
            add_item(user_id = player_id, species = species, count = count)
            text = getStrings(str_id = "commands.pong")
        elif player:
            if user:
                text = getStrings(str_id = "commands.profile.otherno")
            else:
                text = getStrings(str_id = "commands.profile.no")
        else:
            text = getStrings(str_id = "commands.ping")
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Gi(bot))