# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from PIL import Image, ImageDraw, ImageFont
import re
from Tools import spinners as s
import os

# Handling the check command
@commands.command(aliases=['spinner', 'color', 'checkcolor', 'checkspinner', 'cp'])
async def check(ctx, RGB1, RGB2=None):

    # If second value for inner wasn't specified, generate same inner and outer
    if RGB2 is None:
        RGB2 = RGB1

    # Extract red, green and blue values from our color and convert them to ints
    RGBcolor = re.findall('...',RGB1)
    RedC = int(RGBcolor[0]) + 100
    GreenC = int(RGBcolor[1]) + 100
    BlueC = int(RGBcolor[2]) + 100
    
    # If some value higher than 255, make it 255
    if RedC > 255:
        RedC = 255
    if GreenC > 255:
        GreenC = 255
    if BlueC > 255:
        BlueC = 255
    
    # Load our resources
    font = ImageFont.truetype('Resources/saFont.ttf', 19)
    img = Image.open('Resources/oldskool.png')
    d = ImageDraw.Draw(img)
    
    # Generate the name and use our color to color it
    d.text((238, 67), " Michal", fill=(0,0,0), font=font)
    d.text((237, 66), " Michal", fill=(RedC,GreenC,BlueC), font=font)
    
    # Save our picture
    img1 = img.save(RGB1 + '.png')
    
    # Open our profile picture
    profile = Image.open(RGB1 + '.png')
    
    # Generate oldskool image and fill it with our color
    oldskool = s.gen(RGB1, RGB2, 'oldskool')

    oldskool = Image.open(oldskool)
      
    # Paste the generated oldskool to our profile picture and save final pic
    profile.paste(oldskool, (135, 310), mask=oldskool)
    profile.save('finalProfile.png')
    
    # Reply to us with the generated picture for our color
    await ctx.message.channel.send(file=discord.File('finalProfile.png'))
        
    imgList = ['outer.png', 'inner.png', 'spinner.png', 'finalProfile.png', RGB1 + '.png']
    for img in imgList:
        os.remove(img)

# Make the command load & work
def setup(bot):
    bot.add_command(check)

@check.error
async def check_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !check [color code 1] [color code 2]")