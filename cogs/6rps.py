import discord
from discord.ext import commands
import random

list1 = ["rock", "paper", "scissor"]


class cog_6(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, *, choice):

        if ctx.channel.id != 961092222776922143:
            return

        if choice not in list1:
            await ctx.message.delete()
            return

        random_choice = random.choice(list1)

        if choice == random_choice:
            c = "Game Tied"

        elif (
            choice == "rock"
            and random_choice == "scissor"
            or choice == "scissor"
            and random_choice == "paper"
            or choice == "paper"
            and random_choice == "rock"
        ):
            c = f"{ctx.author.mention} Won!!"

        else:
            c = "Heron Won"

        embed = discord.Embed(
            title="Rock Paper Scissor!!",
            description=f"**{ctx.author}** : {choice}\n**Heron** : {random_choice} ",
        )
        embed.add_field(name="Result", value=c)
        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(cog_6(client))
