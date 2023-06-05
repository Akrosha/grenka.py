from discord.ext import commands
from discord.ext.commands import UserConverter
from discord import Embed
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user, edit_nplayer

class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("pay.py is ready")

    @commands.command(aliases = ["выплатить"])
    async def pay(self, ctx, money: int, *user):
        """выплатить грибы другому"""
        
        meplayer = check_user(str(ctx.message.author.id))
        if not meplayer:
            text = getStrings(str_id = "commands.profile.no")
        
        if user:
            user = " ".join(user)
            try:
                user = await UserConverter().convert(ctx, user)
                player_id = str(user.id)
                name = "NaN"
            except:
                player_id = "NaN"
                name = user
        else:
            player_id = str(ctx.message.author.id)
            name = "NaN"
        
        player = check_user(player_id = player_id, name = name)
        
        if meplayer and (not player):
            text = getStrings(str_id = "commands.profile.otherno")
        
        money = abs(money)
        
        if meplayer and player and (money <= 0):
            text = getStrings(str_id = "commands.pay.zero")
        
        if meplayer and player and (money > meplayer["money"]):
            text = getStrings(str_id = "commands.pay.no")
        
        if meplayer and player and (meplayer.get("id") == player.get("id")):
            text = getStrings(str_id = "commands.pay.me")
        
        if meplayer and player and (money < meplayer["money"]) and (money > 0) and (meplayer.get("id") != player.get("id")):
            meplayer["money"] -= money
            player["money"] += money
            edit_nplayer(meplayer)
            edit_nplayer(player)
            text = getStrings(str_id = "commands.pay.yes").format(
                money = str(money),
                name = player.get("name")
                )
            secondText = getStrings(str_id = "commands.pay.tome").format(
                money = str(money),
                name = meplayer.get("name")
                )
            embed = Embed(description = secondText[:2000])
            user = await UserConverter().convert(ctx, player.get("id"))
            try:
                await user.send(embed = embed)
            except:
                ...
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Pay(bot))