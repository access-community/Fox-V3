import discord
from redbot.core import commands

from redbot.core.commands import Cog


class SCPFR(Cog):
    """Look up SCP articles. Warning: Some of them may be too creepy or gruesome."""

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def scpfr(self, ctx: commands.Context, num: int):
        """Look up SCP articles.

        Warning: Some of them may be too creepy or gruesome.
        Reminder: You must specify a number between 1 and 5999.
        """

        # Thanks Shigbeard and Redjumpman for helping me!

        if 0 < num <= 5999:
            msg = "http://fondationscp.wikidot.com/scp-{:03}".format(num)
            c = discord.Color.green()
        else:
            msg = "You must specify a number between 1 and 5999."
            c = discord.Color.red()

        if await ctx.embed_requested():
            await ctx.send(embed=discord.Embed(description=msg, color=c))
        else:
            await ctx.maybe_send_embed(msg)

    @commands.command()
    async def scpfrfr(self, ctx: commands.Context, joke: str):
        """Look up SCP-FRs.

        Reminder: Enter the correct name or else the resultant page will be invalid.
        Use 001, etc. in case of numbers less than 100.
        """

        msg = "http://fondationscp.wikidot.com/scp-{}-fr".format(joke)
        await ctx.maybe_send_embed(msg)


def setup(bot):
    bot.add_cog(SCPFR(bot))
