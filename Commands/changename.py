# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout
from xml.dom import minidom

@commands.command(aliases=['change', 'changename'])
async def namechange(ctx, member, Passw, newName):
    try:
        APIURL = f'http://api.xgenstudios.com/?method=xgen.users.changeName&username={member}&password={Passw}&new_username={newName}'
        APIData = minidom.parseString(requests.get(APIURL, timeout=10).text)
        URLResp = APIData.getElementsByTagName('rsp')[0].attributes['stat'].value
        if URLResp == 'ok':
            await ctx.send(f"Successfully changed username from {member} to {newName}")
        else:
            errorMsg = APIData.getElementsByTagName('err')[0].attributes['msg'].value
            await ctx.send(errorMsg)
    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your requested timed out, try again.")
    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(namechange)

@namechange.error
async def namechange_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !namechange [current name] [password] [new name]")