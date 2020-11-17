# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout
from xml.dom import minidom

@commands.command(aliases=['premiums'])
async def prems(ctx, *, account):
    AccountName = account
    try:
        APIURL = 'http://api.xgenstudios.com/?method=xgen.users.items.list&game_id=boxhead&username=' + account
        APISTATS = 'http://api.xgenstudios.com/?method=xgen.stickarena.stats.get&username=' + account
      
        APIData = minidom.parseString(requests.get(APIURL, timeout=10).text)
        APIUserData = minidom.parseString(requests.get(APISTATS, timeout=10).text)
        Username = APIUserData.getElementsByTagName('user')[0].attributes['username'].value
      
        URLResp = APIData.getElementsByTagName('rsp')[0].attributes['stat'].value
        StatsResp = APIUserData.getElementsByTagName('rsp')[0].attributes['stat'].value
        if StatsResp == 'ok':
            if Username != '':
                AccountName = Username
  
        Number = 0
        PremsList = []

        if URLResp == 'ok':
            NameTag = APIData.getElementsByTagName('name')
            if len(NameTag) == 0:
                await ctx.send(AccountName + " is broke, the account doesn't have any premium items.")
            else:
                for Name in NameTag:
                    NameTag = APIData.getElementsByTagName('name')[Number]
                    PremsTag = NameTag.childNodes[0].nodeValue
                    PremsList.append(PremsTag)
                    Number += 1
                embed=discord.Embed(title=AccountName + "'s Premium Items (Boxhead)", description="\n".join(PremsList), color=0x24262B)
                await ctx.send(embed=embed)

    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your request timed out, try again.")
    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(prems)

@prems.error
async def prems_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !prems [account]")
