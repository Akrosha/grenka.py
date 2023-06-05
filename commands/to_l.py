from discord.ext import commands
from discord import Embed

class ToL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("to_l.py is ready")

    @commands.command(aliases = [])
    async def to_l(self, ctx, *args):
        """text"""
        
        raw_text = []
        for i in " ".join(args):
            try:
                raw_text.append(chr(int(oct(ord(i))[2:])))
            except:
                raw_text.append("")
        text = "".join(raw_text)
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(ToL(bot))