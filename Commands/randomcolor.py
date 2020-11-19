# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from PIL import Image, ImageDraw, ImageFont
import os
import asyncio
import random
from Tools import spinners as s

@commands.command(aliases=['rand', 'random', 'randcol', 'randcolor'])
async def randomcolor(ctx, valid=None):
    generated = 0
    allowed = True
    extra = ''
    stringR = 0
    stringG = 0
    stringB = 0
    theInt = -99
    while generated == 0:
        await asyncio.sleep(0.5)
        
        if valid != None:
            theInt = 000
            
        stringR = random.randint(theInt, 255)
        stringG = random.randint(theInt, 255)
        stringB = random.randint(theInt, 255)
  
        mathNumbers = stringR + stringG + stringB

        if valid != None:
            extra = ' **working**'
            if mathNumbers < 248:
                allowed = False
            elif mathNumbers > 522:
                allowed = False
            else:
                if stringR < 128 and stringG < 128 and stringB < 128:
                    allowed = False
                elif stringR == stringG and stringR == stringB and stringG == stringB:
                    allowed = False
                else:
                    allowed = True

        if allowed == False:
            pass
        else:
            finalRed = str(stringR)
            finalGreen = str(stringG)
            finalBlue = str(stringB)

            if len(finalRed) == 1:
                finalRed = "00" + finalRed
            elif len(finalRed) == 2:
                finalRed = "0" + finalRed
            if '-' in finalRed and len(finalRed) == 2:
                finalRed = "-0" + finalRed[1:]

            if len(finalGreen) == 1:
                finalGreen = "00" + finalGreen
            elif len(finalGreen) == 2:
                finalGreen = "0" + finalGreen
            if '-' in finalGreen and len(finalGreen) == 2:
                finalGreen = "-0" + finalGreen[1:]

            if len(finalBlue) == 1:
                finalBlue = "00" + finalBlue
            elif len(finalBlue) == 2:
                finalBlue = "0" + finalBlue
            if '-' in finalBlue and len(finalBlue) == 2:
                finalBlue = "-0" + finalBlue[1:]
  
            font = ImageFont.truetype('Resources/saFont.ttf', 19)
            img = Image.open('Resources/oldskool.png')
            d = ImageDraw.Draw(img)
      
            convRed = stringR + 100
            convGreen = stringG + 100
            convBlue = stringB + 100
        
            if convRed > 255:
                convRed = 255
            if convGreen > 255:
                convGreen = 255
            if convBlue > 255:
                convBlue = 255

            colorCode = "".join(finalRed) + "".join(finalGreen) + "".join(finalBlue)
  
            d.text((238, 67), " Michal", fill=(0,0,0), font=font)
            d.text((237, 66), " Michal", fill=(convRed,convGreen,convBlue), font=font)
  
            img1 = img.save(colorCode + '.png')
  
            profile = Image.open(colorCode + '.png')
  
            oldskool = s.gen(colorCode, colorCode, 'oldskool')

            oldskool = Image.open(oldskool)
      
            profile.paste(oldskool, (135, 310), mask=oldskool)
            profile.save('finalProfile.png')
  
            await ctx.send(f"Generated new{extra} color code: {colorCode}")
            await ctx.message.channel.send(file=discord.File('finalProfile.png'))
            generated = 1
            imgList = ['outer.png', 'inner.png', 'spinner.png', 'finalProfile.png', colorCode + '.png']
            for img in imgList:
                os.remove(img)

# Make the command load & work.
def setup(bot):
    bot.add_command(randomcolor)
