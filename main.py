import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import module

load_dotenv()

my_secret = os.getenv("token")  # grabbing token
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents = intents, help_command=None)

@client.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Successfully Reloaded! :white_check_mark: ")
    
@reload.error
async def reload_error(ctx, error):
    if isinstance(error,  commands.MissingPermissions):
        embed = discord.Embed(
            title = "Insufficient Permissions",
            color = 0x465722,
            description = "Either you dont have permissions to reload cogs"
        )
        await ctx.send(embed = embed)
        
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title = "Cog needs to be attached",
            description = "Command is : .reload <cog name>"
        )
        await ctx.send(embed = embed)
        
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

module.clear("""
            Welcome to Heron Bot! This bot is currently under development and it is bound to get delayed!
						Made by : Phoenix
""")
client.run(my_secret)