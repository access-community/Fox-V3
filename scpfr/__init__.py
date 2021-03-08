from .scpfr import SCPFR


def setup(bot):
    bot.add_cog(SCPFR(bot))
