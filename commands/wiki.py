from discord.ext import commands
import typing
import wikia


class WikiCommands(commands.Cog):

    def __init__(self, bot):
        self._bot = bot

##COMMANDS##
############

    @commands.command(name="wiki")
    async def search_wiki(self, ctx: commands.Context,
                          val: typing.Optional[int] = 1,
                          *, arg):

        if val <= 5:
            try:
                query = str(arg)
                search = wikia.search("thedivision", query)

                for i in range(val):
                    page = wikia.page("thedivision", search[i])
                    url = page.url.replace(' ', '_')
                    await ctx.send(f"<{url}>")
            except ValueError:
                await ctx.send("No results found")
        else:
            await ctx.send("Max of 5 results allowed.")


def setup(bot):
    bot.add_cog(WikiCommands(bot))
