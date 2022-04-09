import discord
from discord.ext import commands


class cog_12(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, user: discord.Member, *, message=None):
        embed = discord.Embed(title=message)
        await user.send(embed=embed)


def setup(client):
    client.add_cog(cog_12(client))
