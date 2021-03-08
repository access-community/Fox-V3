from .scp-fr import SCPFR


def setup(bot):
    bot.add_cog(SCPFR(bot))
