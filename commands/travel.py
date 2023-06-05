import json
from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings, showAsList
from helpers.databaseFunctions import check_user, get_location
from helpers.rpgengineFunctions import move_player

class Travel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("travel.py is ready")

    @commands.command(aliases = ["перейти"])
    async def travel(self, ctx, loca: str = "NaN"):
        """перемещение между локациями"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if not player:
            text = getStrings(str_id = "commands.profile.no")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        location = get_location(player.get("location"))
        paths = sorted(location.get("paths"))
        loaded = {str(i+1):paths[i] for i in range(len(paths))}
        
        if loca.lower() not in loaded:
            text_list = []
            for i in paths:
                text_list.append(getStrings(str_id = f"location.{i}"))
            text = showAsList(text_list, name = getStrings(str_id = "commands.travel")) + "\n" + getStrings(str_id = "commands.travel.help")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        loc_id = loaded.get(loca.lower())
        moved = move_player(player_id, loc_id)
        
        if moved:
            text = getStrings(str_id = "commands.travel.yes").format(
                location = getStrings(str_id = f"location.{loc_id}")
                )
        else:
            text = getStrings(str_id = "commands.travel.no").format(
                location = getStrings(str_id = f"location.{loc_id}")
                )
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Travel(bot))