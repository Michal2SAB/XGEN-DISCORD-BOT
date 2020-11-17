# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout
from xml.dom import minidom
from PIL import Image, ImageDraw, ImageFont
import os

@commands.command(aliases=['bbhstats', 'bbh', 'statsboxhead', 'boxheadstats'])
async def statsbbh(ctx, *, member):
    try:
        APIURL = 'http://api.xgenstudios.com/?method=xgen.boxhead.users.stats&username=' + member
        APIData = minidom.parseString(requests.get(APIURL, timeout=10).text)
        URLResp = APIData.getElementsByTagName('rsp')[0].attributes['stat'].value

        if URLResp == 'ok':
            RankTag = APIData.getElementsByTagName('rank')[0]
            WinsTag = APIData.getElementsByTagName('wins')[0]
            LossesTag = APIData.getElementsByTagName('losses')[0]
            KillsTag = APIData.getElementsByTagName('kills')[0]
            DeathsTag = APIData.getElementsByTagName('deaths')[0]
            BountyTag = APIData.getElementsByTagName('bountyPoints')[0]

            Rank = RankTag.childNodes[0].nodeValue
            Wins = WinsTag.childNodes[0].nodeValue
            Losses = LossesTag.childNodes[0].nodeValue
            Kills = KillsTag.childNodes[0].nodeValue
            Deaths = DeathsTag.childNodes[0].nodeValue
            Bounty = BountyTag.childNodes[0].nodeValue

            UserId = int(APIData.getElementsByTagName('user')[0].attributes['id'].value)

            UserNew1 = ('Yes' if UserId > 33000000 else 'No')
            UserNew = ('Yes' if UserId > 40000000 else 'No')
            UserOld = ('Yes' if UserId < 20000000 else 'No')
      
            MostWanted = ('Yes' if int(Rank) < 101 else 'No')
            Rounds = int(Wins) + int(Losses)
    
            font = ImageFont.truetype('Resources/Roboto-Regular.ttf', 25)
            font2 = ImageFont.truetype('Resources/Roboto-Regular.ttf', 16)
            font3 = ImageFont.truetype('Resources/Roboto-Regular.ttf', 34)
    
            img = Image.open('Resources/bbhsig.png')
            d = ImageDraw.Draw(img)
    
            d.text((8,104), "Bounty Points", fill=(255,255,255), font=font)
            icon = Image.open("Resources/bounty.PNG")

            img.paste(icon, (8,64))
    
            if MostWanted == 'Yes':
                d.text((8,13), member.capitalize(), fill=(164,0,0), font=font3)
            else:
                d.text((8,13), member.capitalize(), fill=(255,255,255), font=font3)
      
            d.text((50,60), Bounty, fill=(255,0,0), font=font3)
            d.text((200,70), "Ranked:", fill=(255,255,255), font=font)
            d.text((200,104), f"#{Rank}", fill=(255,255,255), font=font)
            d.text((330,20), f"Kills: {Kills}", fill=(255,255,255), font=font2)
            d.text((330,40), f"Deaths: {Deaths}", fill=(255,255,255), font=font2)
            
            if Kills == "0" and Deaths == "0":
                kdr = "NaN"
            elif Kills > "0" and Deaths == "0":
                kdr = Kills + ".00"
            elif Kills == "0" and Deaths > "0":
                kdr = "0.00"
            else:
                kdr = int(Kills) / int(Deaths)
                kdr = round(kdr, 2)
            
            d.text((330,60), f"K/D: {kdr}", fill=(255,255,255), font=font2)

            d.text((330,80), f"Wins: {Wins}", fill=(255,255,255), font=font2)
            d.text((330,100), f"Rounds: {str(Rounds)}", fill=(255,255,255), font=font2)
      
            if Wins == "0" and Losses == "0":
                wlr = "NaN"
            elif Wins > "0" and Losses == "0":
                wlr = Wins + ".00"
            elif Wins == "0" and Losses > "0":
                wlr = "NaN"
            else:
                wlr = int(Wins) / int(Losses)
                wlr = round(wlr, 2)
            
            d.text((330,120), f"W/L: {wlr}", fill=(255,255,255), font=font2)
        
            img1 = img.save(member + '.png')
            await ctx.message.channel.send(file=discord.File(member + '.png'))
            img.close()
            os.remove(member + '.png')
        else:
            return await ctx.send(f"User '{member}' doesn't exist!")

    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your request timed out, try again.")
    except Exception as e:
        print(e)
        pass

# Make the command load & work
def setup(bot):
    bot.add_command(statsbbh)

@statsbbh.error
async def statsbbh_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !statsbbh [username]")