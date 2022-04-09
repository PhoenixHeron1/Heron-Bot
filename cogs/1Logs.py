import discord
from discord.ext import commands


class cog_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    # For Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            activity=discord.Game(name="Watching Pheonix's Server")
        )
        print(
            f"{self.client.user} is up and running!! \nAverage latency of {round(self.client.latency)*1000}ms "
        )

    @commands.Cog.listener()
    async def on_member_join(self, member):

        # await self.client.get_channel(956266369320624128).send(f"{member.mention} has joined the server")
        embed = discord.Embed(
            title="New Member Joined!! :tada: ",
            description=f"{member.mention} just landed on the server. Welcome them on the server :comet:",
        )
        await self.client.get_channel(956266369320624128).send(embed=embed)

    # For commands
    @commands.command()
    @commands.cooldown(rate=2, per=30)
    async def ping(self, ctx):
        if ctx.channel.id != 956455479440195625:
            return
        await ctx.reply(f"{ctx.message.author.mention} Pong!! :ping_pong:")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in [self.client.user.id, 961676784196255846]:
            return
        embed = discord.Embed(
            title=f"New Message from {message.author.mention}",
            description=f"**Message** : {message.content} ",
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await self.client.get_channel(960849393664274462).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id in [self.client.user.id, 961676784196255846]:
            return
        embed = discord.Embed(
            title=f"Message Deleted from {message.channel}",
            description=f"**Message Deleted** : {message.content}",
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await self.client.get_channel(960849393664274462).send(embed=embed)


def setup(client):
    client.add_cog(cog_1(client))
