from time import time
from discord.ext import commands
from helpers.randomFunctions import getStrings, trueRandom
from helpers.databaseFunctions import check_user, update_players

class Bonus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("bonus.py is ready")

    @commands.command(aliases = ["бонус"])
    async def bonus(self, ctx):
        """получить ежедневный бонус"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if player:
            bonus_time = player["bonus"] - int(time())
            if bonus_time < 0:
                bonus_time = int(time()) + 86400
                money = int(trueRandom(200, 700))
                
                player.update({"money": player["money"] + money, "bonus": bonus_time})
                update_players({player_id: player})
                text = f"{getStrings(str_id = 'commands.bonus.first')}: {money}{getStrings(str_id = 'commands.bonus.end')} <t:{player['bonus']}:F>"
            else:
                text = f"{getStrings(str_id = 'commands.bonus.second')}{getStrings(str_id = 'commands.bonus.end')} <t:{player['bonus']}:F>"
        else:
            text = getStrings(str_id = "commands.profile.no")
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Bonus(bot))