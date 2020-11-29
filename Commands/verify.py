# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout
from xml.dom import minidom

@commands.command(aliases=['email'])
async def verify(ctx, member, Passw, email):
    try:
        APIURL = f'http://api.xgenstudios.com/?method=xgen.users.addEmail&username={member}&password={Passw}&email={email}'
        APIData = minidom.parseString(requests.get(APIURL, timeout=10).text)
        URLResp = APIData.getElementsByTagName('rsp')[0].attributes['stat'].value
        if URLResp == 'ok':
            await ctx.send("A verification E-mail has been sent to you (this may take a few minutes to arrive). When you receive our E-mail, open it and click the link inside to verify your account and claim your 500 cred.")
        else:
            errorMsg = APIData.getElementsByTagName('err')[0].attributes['msg'].value
            await ctx.send("Your XGen Account is already verified.")
    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your requested timed out, try again.")
    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(verify)

@verify.error
async def verify_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !verify [name] [password] [email]")
