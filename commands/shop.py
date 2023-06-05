import json
from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings, showAsList
from helpers.databaseFunctions import check_user, edit_nplayer, get_shop
from helpers.rpgengineFunctions import add_item

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("shop.py is ready")

    @commands.command(aliases = ["магазин"])
    async def shop(self, ctx, item: str = "NaN", count: int = 1):
        """магазин предметов в системе рпг"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if not player:
            text = getStrings(str_id = "commands.profile.no")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        if count <= 0:
            text = getStrings(str_id = "commands.shop.zero")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        loaded = get_shop()
        
        if item.lower() in loaded:
            ishop = loaded.get(item.lower())
        else:
            text_list = []
            for i in loaded:
                text_list.append(getStrings(str_id = "commands.shop.price").format(
                    first = getStrings(str_id = f"item.{loaded.get(i).get('item')}"),
                    second = getStrings(str_id = f"regular.money"),
                    price = loaded.get(i).get("price")
                    ))
            text = showAsList(text_list, name = getStrings(str_id = "commands.shop"), iterator = 10) + "\n" + getStrings(str_id = "commands.shop.help")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        money = count*ishop.get("price")
        if money > player.get("money"):
            text = getStrings(str_id = "commands.shop.no").format(
                second = getStrings(str_id = f"regular.money")
                )
        else:
            add_item(user_id = player_id, species = ishop.get('item'), count = count)
            player["money"] -= money
            edit_nplayer(player)
            text = getStrings(str_id = "commands.shop.yes").format(
                first = getStrings(str_id = f"item.{ishop.get('item')}"),
                second = getStrings(str_id = f"regular.money"),
                count = count,
                money = money
                )
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Shop(bot))