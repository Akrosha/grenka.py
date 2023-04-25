from discord.ext import commands
from discord import User
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user, update_players

class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("pay.py is ready")

    @commands.command(aliases = ["выплатить"])
    async def pay(self, ctx, user: User, money: int):
        """выплатить грибы другому"""
        
        meplayer = check_user(str(ctx.message.author.id))
        if not meplayer:
            text = getStrings(str_id = "commands.profile.no")
        
        player = check_user(str(user.id))
        if meplayer and (not player):
            text = getStrings(str_id = "commands.profile.otherno")
        
        if meplayer and player and (money <= 0):
            text = getStrings(str_id = "commands.pay.zero")
        
        if meplayer and player and (money > meplayer["money"]):
            text = getStrings(str_id = "commands.pay.no")
        
        if meplayer and player and (meplayer.get("id") == player.get("id")):
            text = getStrings(str_id = "commands.pay.me")
        
        if meplayer and player and (money < meplayer["money"]) and (money > 0) and (meplayer.get("id") != player.get("id")):
            meplayer["money"] -= money
            player["money"] += money
            update_players({meplayer.get("id"):meplayer})
            update_players({player.get("id"):player})
            text = getStrings(str_id = "commands.pay.yes").format(
                money = str(money),
                name = player.get("name")
                )
            secondText = getStrings(str_id = "commands.pay.tome").format(
                money = str(money),
                name = meplayer.get("name")
                )
            await user.send(secondText[:2000])
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Pay(bot))