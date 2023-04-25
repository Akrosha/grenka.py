import os
from discord.ext import commands
from discord import User

class Send(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("send.py is ready")

    @commands.command(aliases = [])
    async def send(self, ctx, user: User, *args):
        """text"""
        
        if str(ctx.message.author.id) != os.getenv("adminId"):
            return

        secondText = " ".join(args)
        await user.send(secondText[:2000])

async def setup(bot):
    await bot.add_cog(Send(bot))