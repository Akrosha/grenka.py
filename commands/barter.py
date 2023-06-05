import json
from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings, showAsList
from helpers.databaseFunctions import check_user, edit_nplayer

class Barter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("barter.py is ready")

    @commands.command(aliases = ["обмен"])
    async def barter(self, ctx, item: str = "NaN", count: int = 1):
        """обмен в системе рпг"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if not player:
            text = getStrings(str_id = "commands.profile.no")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        if count <= 0:
            text = getStrings(str_id = "commands.barter.zero")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        with open("database/barter.json", "r") as file:
            loaded = json.load(file)
        
        if item.lower() in loaded:
            ibarter = loaded.get(item.lower())
        else:
            text_list = []
            for i in loaded:
                text_list.append(getStrings(str_id = "commands.barter.price").format(
                    first = getStrings(str_id = f"regular.{loaded.get(i).get('first')}"),
                    second = getStrings(str_id = f"regular.{loaded.get(i).get('second')}"),
                    price = loaded.get(i).get("price")
                    ))
            text = showAsList(text_list, name = getStrings(str_id = "commands.barter")) + "\n" + getStrings(str_id = "commands.barter.help")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        money = count*ibarter.get("price")
        if money > player.get(ibarter.get("second")):
            text = getStrings(str_id = "commands.barter.no").format(
                second = getStrings(str_id = f"regular.{ibarter.get('second')}")
                )
        else:
            player[ibarter.get("first")] += count
            player[ibarter.get("second")] -= money
            edit_nplayer(player)
            text = getStrings(str_id = "commands.barter.yes").format(
                first = getStrings(str_id = f"regular.{ibarter.get('first')}"),
                second = getStrings(str_id = f"regular.{ibarter.get('second')}"),
                count = count,
                money = money
                )
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Barter(bot))