# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout
from PIL import Image, ImageDraw, ImageFont
from xml.dom import minidom
from bs4 import BeautifulSoup
import os

@commands.command(alises=['old', 'prevstats', 'statsold'])
async def oldstats(ctx, *, member):
    try:
        APIURL = 'http://api.xgenstudios.com/?method=xgen.stickarena.stats.get&username=' + member
        PHPURL = 'http://www.xgenstudios.com/stickarena/highscore/index.php?date=2017-08-31'
        table_list = []

        APIData = minidom.parseString(requests.get(APIURL, timeout=10).text)
        URLResp = APIData.getElementsByTagName('rsp')[0].attributes['stat'].value
        Username = APIData.getElementsByTagName('user')[0].attributes['username'].value

        newText = ''

        if URLResp == 'ok':
            if Username != '':
                StatTag = APIData.getElementsByTagName('stat')
                Ballistick = StatTag[5].firstChild.nodeValue
            
                UserStatus = int(APIData.getElementsByTagName('user')[0].attributes['perms'].value)
                UserId = int(APIData.getElementsByTagName('user')[0].attributes['id'].value)
            
                BanCheck = ('Yes' if UserStatus < 0 else 'No')
                ModCheck = ('Yes' if UserStatus > 0 else 'No')

                UserNew1 = ('Yes' if UserId > 33000000 else 'No')
                UserNew = ('Yes' if UserId > 40000000 else 'No')
                UserOld = ('Yes' if UserId < 20000000 else 'No')

                LabpassCheck = ('Yes' if Ballistick == '1' else 'No')
      
                theAction = {'username': member}
                checkHS = requests.post(PHPURL, data = theAction)
            
                soup = BeautifulSoup(checkHS.text, 'html.parser')
                for table_data in soup.find_all('td'):
                    table_list.append(str(table_data))
      
                Kills = table_list[9]
                Kills = Kills[26:].strip('</td>')
                Kills = Kills.replace(',', '')
      
                Deaths = table_list[10]
                Deaths = Deaths[26:].strip('</td>')
                Deaths = Deaths.replace(',', '')
      
                Wins = table_list[11]
                Wins = Wins[26:].strip('</td>')
                Wins = Wins.replace(',', '')
      
                Losses = table_list[12]
                Losses = Losses[26:].strip('</td>')
                Losses = Losses.replace(',', '')
      
                Rounds = int(Wins) + int(Losses)
                Rounds = str(Rounds)
      
                font = ImageFont.truetype('Resources/Roboto-Regular.ttf', 25)
                font2 = ImageFont.truetype('Resources/Roboto-Regular.ttf', 22)
                font3 = ImageFont.truetype('Resources/saFont.ttf', 17)
                img = Image.open('Resources/background.png')
            
                d = ImageDraw.Draw(img)
  
                d.text((291,11), Username, fill=(0,0,0), font=font)
                d.text((289,9), Username, fill=(255,255,255), font=font)
                d.text((290,10), Username, fill=(166,124,0), font=font)
      
                d.text((208,67), "Kills: " + Kills, fill=(255,255,255), font=font2)
                d.text((209,68), "Kills: " + Kills, fill=(0,0,0), font=font2)
        
                d.text((208,96), "Deaths: " + Deaths, fill=(255,255,255), font=font2)
                d.text((209,97), "Deaths: " + Deaths, fill=(0,0,0), font=font2)
        
                d.text((410,66), "Wins: " + Wins, fill=(255,255,255), font=font2) 
                d.text((411,67), "Wins: " + Wins, fill=(0,0,0), font=font2) 
        
                d.text((410,96), "Losses: " + Losses, fill=(255,255,255), font=font2)
                d.text((411,97), "Losses: " + Losses, fill=(0,0,0), font=font2)
        
                d.text((11,47), "Rounds: " + Rounds, fill=(255,255,255), font=font2)
                d.text((12,48), "Rounds: " + Rounds, fill=(0,0,0), font=font2)
                
                if Kills == "0" and Deaths == "0":
                    kdr = "0.00"
                elif Kills > "0" and Deaths == "0":
                    kdr = Kills + ".00"
                elif Kills == "0" and Deaths > "0":
                    kdr = "0.00"
                else:
                    kdr = int(Kills) / int(Deaths)
                    kdr = round(kdr, 2)

                d.text((11,77), f"K/D: {kdr}", fill=(255,255,255), font=font2)
                d.text((12,78), f"K/D: {kdr}", fill=(0,0,0), font=font2)

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
                    
                d.text((208,126), f"Acc ID: {UserId}", fill=(255,255,255), font=font2)
                d.text((209,127), f"Acc ID: {UserId}", fill=(0,0,0), font=font2)
                
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
                  
                if LabpassCheck == "Yes":
                    d.text((2,5), "{B}", fill=(218,165,32), font=font2)
                  
                if ModCheck == "Yes":
                    d.text((35,5), f"M[{UserStatus}]", fill=(10,10,10), font=font2)
                  
                if BanCheck == "Yes":
                    d.text((409,126), "BANNED", fill=(0,0,0), font=font2)
                    d.text((410,127), "BANNED", fill=(128,0,0), font=font2)
                
                img1 = img.save('oldstats.png')
                await ctx.message.channel.send(file=discord.File('oldstats.png'))
                img.close()
                os.remove('oldstats.png')
        
            else:
                await ctx.send(f"'{member}' doesn't have any previous stats.")
        else:
            await ctx.send("Something went wrong with the XGen API, try again.")    
    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your request timed out, try again.")
    except Exception as e:
        await ctx.send(f"'{member}' doesn't have any previous stats.")
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(oldstats)
    
@oldstats.error
async def oldstats_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !oldstats [username]")
