from discord.ext import commands
from discord import User
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user
from helpers.rpgengineFunctions import get_level, get_experience, get_max_health

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("profile.py is ready")

    @commands.command(aliases = ["профиль"])
    async def profile(self, ctx, user: User = None):
        """показывает профиль в системе рпг"""
        
        if user:
            player_id = str(user.id)
        else:
            player_id = str(ctx.message.author.id)
        
        player = check_user(player_id)
        
        if player:
            level = get_level(player.get("experience"))
            dexperience = [get_experience(level), get_experience(level + 1)]
            
            text = getStrings(str_id = "commands.profile.yes").format(
                uid = player.get("id"),
                name = player.get("name"),
                money = player.get("money"),
                minHP = player.get("health"),
                maxHP = get_max_health(level),
                level = level + 1,
                minXP = player.get("experience") - dexperience[0],
                maxXP = dexperience[1] - dexperience[0],
                XP = player.get("experience")
                )
        else:
            if user:
                text = getStrings(str_id = "commands.profile.otherno")
            else:
                text = getStrings(str_id = "commands.profile.no")
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Profile(bot))