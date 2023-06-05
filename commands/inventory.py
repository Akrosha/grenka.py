import json
from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings, showAsList
from helpers.databaseFunctions import check_user, get_player_inv
from helpers.rpgengineFunctions import use_item

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("inventory.py is ready")

    @commands.command(aliases = ["inv", "инвентарь", "инв"])
    async def inventory(self, ctx, action: int = None, var: int = 1, count: int = 1):
        """инвентарь в системе рпг"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if not player:
            text = getStrings(str_id = "commands.profile.no")
            embed = Embed(description = text[:2000])
            await ctx.message.reply(embed = embed)
            return text
        
        items = get_player_inv(player_id)
        items = sorted(items.values(),key=lambda x: x["item_id"], reverse=False)
        
        if action == 1:
            itemsList = []
            for it in items:
                name = getStrings(str_id = f"item.{it.get('species')}")
                count = it.get("count")
                itemsList.append(f"[{name}]x{count}")
            text = showAsList(itemsList, getStrings(str_id = "commands.inventory.items"), page = var)
        elif action == 2:
            try:
                it = items[var-1]
                name = getStrings(str_id = f"item.{it.get('species')}")
                extra = use_item(it.get("item_id"))
                text = getStrings(str_id = "commands.inventory.use").format(
                    name = name,
                    x = "x1",
                    extra = extra)
            except:
                text = getStrings(str_id = "commands.inventory.noitem").format(var)
        else:
            actions_list = getStrings(str_id = "commands.inventory.actions_list").split(";")
            list_name = getStrings(str_id = "commands.inventory.actions")
            text = showAsList(actions_list, list_name, iterator = len(actions_list))
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Inventory(bot))