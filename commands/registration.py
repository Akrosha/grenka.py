from discord.ext import commands
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user, update_players

class Registration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("registration.py is ready")

    @commands.command(aliases = ["register", "reg", "регистрация", "регистр", "рег"])
    async def registration(self, ctx, args: str = None):
        """регистрация в системе rpg"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if args and not player:
            update_players({player_id: {"id": player_id, "name": args[:16], "money": 0, "bonus": 0, "health": 20, "experience": 0}})
            text = f"{getStrings(str_id = 'commands.registration.yes')}: {args[:16]}"
        elif not player:
            text = getStrings(str_id = "commands.registration.noname")
        else:
            text = f"{getStrings(str_id = 'commands.registration.no')}: {player['name']}"
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Registration(bot))