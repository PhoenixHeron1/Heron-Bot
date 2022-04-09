import discord
from discord.ext import commands


class cog_7(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        if ctx.channel.id != 956455479440195625:
            return

        await ctx.reply(f"Help Requested by {ctx.author.mention} ")

        embed = discord.Embed(title="Help Section", description="Bot prefix is {.}")
        embed.add_field(name="1).ping", value="Returns Pong", inline=False)
        embed.add_field(name="2) .calc <problem>", value="Returns Answer", inline=False)
        embed.add_field(
            name="3) .rps <rock/paper/scissor>**",
            value="Let's see who wins",
            inline=False,
        )

        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(cog_7(client))
