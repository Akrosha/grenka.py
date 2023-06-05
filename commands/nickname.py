from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user, edit_nplayer, database

class Nickname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("nickname.py is ready")

    @commands.command(aliases = ["nick", "никнейм", "ник"])
    async def nickname(self, ctx, *args):
        """смена ника в системе rpg"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        name = " ".join(args)[:16]
        
        if args and player:
            if database.execute(f"SELECT name FROM users WHERE name = '{name}'") or (name == "NaN"):
                text = getStrings(str_id = "commands.nickname.exist")
            else:
                edit_nplayer({"id": player_id, "name": name})
                text = f"{getStrings(str_id = 'commands.nickname.yes')}: {name}"
        elif player:
            text = getStrings(str_id = "commands.nickname.noname")
        else:
            text = getStrings(str_id = 'commands.profile.no')
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Nickname(bot))