import os, json, requests
from re import findall
from discord.ext import commands
from deep_translator import GoogleTranslator

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("chat.py is ready")

    @commands.command(aliases = ["чат", "ч", "c"])
    async def chat(self, ctx, *args):
        """початимся?"""
        try:
            text = GoogleTranslator(source="auto",target="en").translate(" ".join(args))
        except:
            text = GoogleTranslator(source="auto",target="en").translate("апыавы")
        
        r = requests.get(f"{os.getenv('chatapi')}&uid={str(ctx.message.author.id)}&msg={text}").text
        r = json.loads(r)
        
        text = GoogleTranslator(source="auto",target="ru").translate(r.get("cnt","NaN"))
        wish = findall("<@[0-9]+>", text)
        for i in wish:
            text = text.replace(i, "NaN")
        
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Chat(bot))