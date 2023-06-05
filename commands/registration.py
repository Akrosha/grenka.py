from discord.ext import commands
from discord import Embed
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user, add_nplayer, database

class Registration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("registration.py is ready")

    @commands.command(aliases = ["register", "reg", "регистрация", "регистр", "рег"])
    async def registration(self, ctx, *args):
        """регистрация в системе rpg"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        name = " ".join(args)[:16]
        
        if args and not player:
            if database.execute(f"SELECT name FROM users WHERE name = '{name}'") or (name == "NaN"):
                text = getStrings(str_id = "commands.nickname.exist")
            else:
                add_nplayer({"id": player_id, "name": name, "money": 0, "bonus": 0, "health": 20, "experience": 0, "location": "start_glade"})
                text = f"{getStrings(str_id = 'commands.registration.yes')}: {name}"
        elif not player:
            text = getStrings(str_id = "commands.registration.noname")
        else:
            text = f"{getStrings(str_id = 'commands.registration.no')}: {player['name']}"
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Registration(bot))