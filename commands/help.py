from discord.ext import commands
import discord
from util.config.config_handler import Config

class HelpCommand(commands.Cog):

    def __init__(self, bot):
        self.config = Config()
        self.bot = bot

    @commands.group(name="help", aliases=["?", "h"], invoke_without_command=1)
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(
                        title="Help",
                        type="rich")\
                        .add_field(name="Legend", inline=False,
                                   value=f"{self.config.prefix}cmd <optional> [required]")\
                        .add_field(name="wiki <#> [query]", inline=False,
                                   value="Search the TD2 wiki")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
