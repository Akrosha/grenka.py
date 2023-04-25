from discord.ext import commands
from helpers.randomFunctions import getStrings, showAsList
from os import listdir

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is ready")

    @commands.command(aliases = ["commands", "команды", "помощь", "хелп", "?"])
    async def help(self, ctx, *args):
        """помощь по командам"""
        hidden = getStrings(str_id = "commands.help.hidden").split(";")
        
        all_commands = self.bot.all_commands
        noalias = []
        for command in all_commands.values():
            if (command.name in noalias) or (command.name in hidden):
                pass
            else:
                noalias.append(command.name)
        
        text_list = [f"{name} - {getStrings(str_id = f'commands.{name}.info')} [{'; '.join(all_commands.get(name).aliases)}]" for name in noalias]
        
        if len(args) > 0:
            try:
                text = showAsList(text_list, name = getStrings(str_id = "commands.help"), page = int(args[0]))
            except:
                command = all_commands.get(args[0])
                if command:
                    text = f"{command.name} - {getStrings(str_id = f'commands.{command.name}.info')} [{'; '.join(command.aliases)}]"
                else:
                    text = f"{args[0]}: {getStrings(str_id = f'commands.help.void')}"
        else:
            text = showAsList(text_list, name = getStrings(str_id = "commands.help"))
        await ctx.message.reply(text[:2000])

async def setup(bot):
    await bot.add_cog(Help(bot))
