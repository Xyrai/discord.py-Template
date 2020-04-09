from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        latency = int(self.bot.latency * 1000)
        await ctx.send(f'🏓 Pong! ({latency}ms)')


def setup(bot):
    bot.add_cog(General(bot))
