import os
from discord.ext import commands
from discord import User, Embed

class Mk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("mk.py is ready")

    @commands.command(aliases = [])
    async def mk(self, ctx, server_id: int):
        """text"""
        
        if str(ctx.message.author.id) != os.getenv("adminId"):
            return
        
        guild = self.bot.get_guild(server_id)
        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
        secondText = f"https://discord.gg/{invite.code}"
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(Mk(bot))