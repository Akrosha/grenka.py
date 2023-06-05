from discord.ext import commands
from discord.ext.commands import UserConverter
from discord import Embed
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
    async def profile(self, ctx, *user):
        """показывает профиль в системе рпг"""
        
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
        
        if player:
            level = get_level(player.get("experience"))
            dexperience = [get_experience(level), get_experience(level + 1)]
            
            text = getStrings(str_id = "commands.profile.yes").format(
                uid = player.get("id"),
                name = player.get("name"),
                location = getStrings(str_id = f"location.{player.get('location')}"),
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
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Profile(bot))