from discord.ext import commands
from helpers.randomFunctions import getStrings
from helpers.databaseFunctions import check_user

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("profile.py is ready")

    @commands.command(aliases = ["профиль"])
    async def profile(self, ctx):
        """показывает профиль в системе рпг"""
        
        player_id = str(ctx.message.author.id)
        player = check_user(player_id)
        
        if player:
            text = """id: {}
name: {}
money: {}""".format(player.get("id"), player.get("name"), player.get("money"))
        else:
            text = getStrings(str_id = "commands.profile.no")
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Profile(bot))