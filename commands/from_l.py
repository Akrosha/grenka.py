from re import findall
from discord.ext import commands
from discord import Embed

class FromL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("from_l.py is ready")

    @commands.command(aliases = [])
    async def from_l(self, ctx, *args):
        """text"""
        
        raw_text = []
        for i in " ".join(args):
            try:
                raw_text.append(chr(int(str(ord(i)), 8)))
            except:
                raw_text.append("")
        text = "".join(raw_text)
        
        wish = findall("<@[0-9]+>", text)
        for i in wish:
            text = text.replace(i, "NaN")
        
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(FromL(bot))