from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings, showAsList
from helpers.databaseFunctions import really_all
from helpers.rpgengineFunctions import get_level, get_experience

class Top(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("top.py is ready")

    @commands.command(aliases = ["топ"])
    async def top(self, ctx, item: str = None, page: int = 1):
        """топы игроков"""
        
        if item == "1":
            top = sorted(really_all().values(),key=lambda x: x["money"], reverse=True)
            topList = [f"{pl.get('name')}:\n\t{pl.get('money')}:mushroom:" for pl in top]
            text = showAsList(topList, name = getStrings(str_id = "commands.top").format(getStrings(str_id = "regular.money")), page = page, iterator = 10)
        elif item == "2":
            top = sorted(really_all().values(),key=lambda x: x["experience"], reverse=True)
            topList = []
            for pl in top:
                XP = pl.get("experience")
                level = get_level(XP)
                dexperience = [get_experience(level), get_experience(level + 1)]
                minXP = pl.get("experience") - dexperience[0]
                maxXP = dexperience[1] - dexperience[0]
                topList.append(f"{pl.get('name')}:\n\t{level+1} :arrow_up: {minXP}/{maxXP} ({XP}) :sparkles:")
            text = showAsList(topList, name = getStrings(str_id = "commands.top").format(getStrings(str_id = "regular.experience")), page = page, iterator = 10)
        else:
            topList = [getStrings(str_id = "regular.money"),getStrings(str_id = "regular.experience")]
            text = showAsList(topList, name = getStrings(str_id = "commands.top2")) + "\n" + getStrings(str_id = "commands.top.help")
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Top(bot))