# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout
from xml.dom import minidom

@commands.command(aliases=['createacc', 'make'])
async def create(ctx, Username, Password, Color=None):
    try:
        if Color == None:
            Color = "113000150"
        
        PostData = {"username": Username, "userpass": Password, "usercol": Color, "action": "create"}
        URLData = requests.post("http://www.xgenstudios.com/stickarena/stick_arena.php", data=PostData, timeout=10).text
 
        if "success" in URLData:
            await ctx.send("Successfully created '" + Username + "'")
        else:
            await ctx.send("Could not create: '" + Username + "'")
        
    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your request timed out, try again.")
    except Exception as Error:
        print(Error)

# Make the command load & work
def setup(bot):
    bot.add_command(create)

@create.error
async def create_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !create [username] [password] [color optionally]")

