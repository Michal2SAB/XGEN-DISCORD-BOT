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

# Handling stats command
@commands.command()
async def stats(ctx, member):
    try:
        # Apis that will be used to lookup user info
        APIURL = 'http://api.xgenstudios.com/?method=xgen.stickarena.stats.get&username=' + member
        APIURLBBH = 'http://api.xgenstudios.com/?method=xgen.boxhead.users.stats&username=' + member
        APIURLGENERAL = 'http://api.xgenstudios.com/?method=xgen.stats.get&username=' + member

        # Looking up stats with the first api (stickarena)
        APIData = minidom.parseString(requests.get(APIURL, timeout=10).text)

        # Extracting the response & username
        URLResp = APIData.getElementsByTagName('rsp')[0].attributes['stat'].value
        Username = APIData.getElementsByTagName('user')[0].attributes['username'].value
        newText = ''

        if URLResp == 'ok': # If success
            if Username != '': # If the account exists on stickarena
                StatTag = APIData.getElementsByTagName('stat') # Accessing account stats

                # Extracting the account stats
                Wins = StatTag[0].firstChild.nodeValue
                Losses = StatTag[1].firstChild.nodeValue
                Kills = StatTag[2].firstChild.nodeValue
                Deaths = StatTag[3].firstChild.nodeValue
                Rounds = StatTag[4].firstChild.nodeValue

                # Checking if has labpass and/or is banned/moderator
                Ballistick = StatTag[5].firstChild.nodeValue
                UserStatus = int(APIData.getElementsByTagName('user')[0].attributes['perms'].value)

                BanCheck = ('Yes' if UserStatus < 0 else 'No')
                ModCheck = ('Yes' if UserStatus > 0 else 'No')
                LabpassCheck = ('Yes' if Ballistick == '1' else 'No')

                # Extracting the account's ID number
                UserId = int(APIData.getElementsByTagName('user')[0].attributes['id'].value)

                # Determining whether the account is old, new, or very new (Based on the account's ID)
                UserNew1 = ('Yes' if UserId > 33000000 else 'No')
                UserNew = ('Yes' if UserId > 40000000 else 'No')
                UserOld = ('Yes' if UserId < 20000000 else 'No')

                # Specifying fonts/sizes that will be used for the stats text
                font = ImageFont.truetype('Resources/Roboto-Regular.ttf', 25)
                font2 = ImageFont.truetype('Resources/Roboto-Regular.ttf', 22)
                font3 = ImageFont.truetype('Resources/saFont.ttf', 17)

                # Loading some cool background for the generated stats picture
                img = Image.open('Resources/background.png')

                # Generating our beautiful stats picture
                d = ImageDraw.Draw(img)

                # Account username text
                d.text((291,11), Username, fill=(0,0,0), font=font)
                d.text((289,9), Username, fill=(255,255,255), font=font)
                d.text((290,10), Username, fill=(166,124,0), font=font)

                # Kills text
                d.text((208,67), f"Kills: {Kills}", fill=(255,255,255), font=font2)
                d.text((209,68), f"Kills: {Kills}", fill=(0,0,0), font=font2)

                # Deaths text
                d.text((208,96), f"Deaths: {Deaths}", fill=(255,255,255), font=font2)
                d.text((209,97), f"Deaths: {Deaths}", fill=(0,0,0), font=font2)

                # Wins text
                d.text((410,66), f"Wins: {Wins}", fill=(255,255,255), font=font2) 
                d.text((411,67), f"Wins: {Wins}", fill=(0,0,0), font=font2) 
                    
                # Losses text
                d.text((410,96), f"Losses: {Losses}", fill=(255,255,255), font=font2)
                d.text((411,97), f"Losses: {Losses}", fill=(0,0,0), font=font2)

                # Rounds text
                d.text((11,47), f"Rounds: {Rounds}", fill=(255,255,255), font=font2)
                d.text((12,48), f"Rounds: {Rounds}", fill=(0,0,0), font=font2)

                useRound = False

                # If kills and deaths both equal 0, fixing some stupid python bug
                if Kills == "0" and Deaths == "0":
                    kdr = "0.00"

                # If got kills but no deaths, fixing some stupid python bug
                elif Kills > "0" and Deaths == "0":
                    kdr = Kills + ".00"

                # If got deaths but no kills, fixing some stupid python bug
                elif Kills == "0" and Deaths > "0":
                    kdr = "0.00"

                # If got kills and deaths, fixing some stupid python bug
                else:
                    kdr = int(Kills) / int(Deaths)
                    kdr = round(kdr, 2)

                d.text((11,77), f"K/D: {kdr}", fill=(255,255,255), font=font2)
                d.text((12,78), f"K/D: {kdr}", fill=(0,0,0), font=font2)

                # Same shit but for wins and losses, fixing some stupid python bug
                if Wins == "0" and Losses == "0":
                    wlr = "0.00"
                elif Wins > "0" and Losses == "0":
                    wlr = Wins + ".00"
                elif Wins == "0" and Losses > "0":
                    wlr = "0.00"
                else:
                    wlr = int(Wins) / int(Losses)
                    wlr = round(wlr, 2)

                d.text((11,107), f"W/L: {wlr}", fill=(255,255,255), font=font2)
                d.text((12,108), f"W/L: {wlr}", fill=(0,0,0), font=font2)
                    
                # Account ID number part
                d.text((208,126), f"Acc ID: {UserId}", fill=(255,255,255), font=font2)
                d.text((209,127), f"Acc ID: {UserId}", fill=(0,0,0), font=font2)

                # If new, old, or super new, then change texts
                if UserNew == "Yes":
                    newText = 'Very New acc'
                elif UserNew1 == 'Yes':
                    newText = 'New Acc'
                elif UserOld == 'Yes':
                    newText = 'Very Old Acc'
                else:
                    newText = 'Old Acc'

                d.text((556,11), newText, fill=(0,0,0), font=font3)
                d.text((554,9), newText, fill=(128,128,128), font=font3)
                d.text((555,10), newText, fill=(192,192,192), font=font3)

                # If got labpass, display labpass icon
                if LabpassCheck == "Yes":
                    d.text((2,5), "{B}", fill=(218,165,32), font=font2)

                # If is a moderator, display moderator icon
                if ModCheck == "Yes":
                    d.text((35,5), f"M[{UserStatus}]", fill=(10,10,10), font=font2)

                # If is banned, display red banned text
                if BanCheck == "Yes":
                    d.text((409,126), "BANNED", fill=(0,0,0), font=font2)
                    d.text((410,127), "BANNED", fill=(128,0,0), font=font2)

                # After the picture is generated, save it to the bot's directory
                img1 = img.save('stats.png')

                # Send our generated stats image to the discord server
                await ctx.message.channel.send(file=discord.File('stats.png'))

                # Close image and delete it
                img.close()
                os.remove('stats.png')
                
            # If the account doesn't have any stickarena stats
            else:
                finalmessage = f"Username '{member}' doesn't exist on SA!" # First part of our message
                superfinalMessage = "" # Second part of our message, letting us know if the account exists on any other XGen games or not

                # Looking up stats with the second api (boxhead)
                APIDataBBH = minidom.parseString(requests.get(APIURLBBH, timeout=10).text)

                # Extracting the response
                URLRespBBH = APIDataBBH.getElementsByTagName('rsp')[0].attributes['stat'].value

                # Check if account exists on boxhead
                if URLRespBBH == 'ok':
                    bbhCheck = "yes"
                else:
                    bbhCheck = "no"

                # Looking up stats with the third api (all other xgen games)
                APIDataGENERAL = minidom.parseString(requests.get(APIURLGENERAL, timeout=10).text)

                # Check if account exists on the rest of xgen games
                try:
                    Found = APIDataGENERAL.getElementsByTagName('game')[0].attributes['id'].value
                    generalCheck = "yes"
                except IndexError:
                    generalCheck = "no"
                    
                # Determining what final part of our message to send back on the discord server
                if bbhCheck == "yes":
                    if generalCheck == "yes":
                        await ctx.send(finalmessage + " But it does exist on: **boxhead* and some other xgen games like **dinorun**.")
                    else:
                        await ctx.send(finalmessage + " But it does exist on: **boxhead**.")
                else:
                    if generalCheck == "yes":
                        await ctx.send(finalmessage + " But it does exist on other xgen games like **dinorun**, **two** etc.")
                        
                    # If the account doesn't have stats anywhere
                    else:
                        await ctx.send(f"Username '{member}' doesn't exist on xgen. But if you can't make it, someone must've created it via the API and just never logged in with it to any of the xgen games.")

    # If the stats request took too long & didn't receive any response     
    except Timeout:
        await ctx.send(ctx.message.author.mention + " Stats request timed out, try again.")

    # Logging any other errors that may occur
    except Exception as e:
        print(e)
        pass

# Make the command load & work
def setup(bot):
    bot.add_command(stats)

@stats.error
async def stats_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !stats [username]")
