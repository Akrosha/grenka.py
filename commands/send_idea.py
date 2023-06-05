import os
from discord.ext import commands
from discord import User, Embed
from helpers.randomFunctions import getStrings, showAsList, logger
from helpers.databaseFunctions import get_ideas

class SendIdea(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("send_idea.py is ready")

    @commands.command(aliases = ["idea", "отправить_идею", "идея"])
    async def send_idea(self, ctx, *args):
        """отправить идею для бота"""
        
        if args:
            text = f"@ImRinoske\nNEW IDEA:\n" + " ".join(args)
            logger(text[:2000])
        
            text = getStrings(str_id = "commands.send_idea.ok")
        else:
            textList = []
            ideas = get_ideas()
            for idea in ideas.values():
                textList.append(getStrings(str_id = "commands.send_idea.idea").format(
                    id = idea.get("id"),
                    idea = idea.get("idea"),
                    comment = idea.get("comment")
                    ))
            text = showAsList(textList, name = getStrings(str_id = "commands.send_idea"), iterator = 10)
        embed = Embed(description = text[:2000])
        await ctx.message.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(SendIdea(bot))