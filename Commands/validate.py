# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import re

@commands.command(aliases=['valid', 'validatecolor', 'validcolor'])
async def validate(ctx, *, member):
    if len(member) != 9:
        await ctx.send("That's not a proper SA color format! Hint: 255000000")
    else:
        RGBcolor = re.findall('...',member)
    
        RedC = int(RGBcolor[0]) + 100
        GreenC = int(RGBcolor[1]) + 100
        BlueC = int(RGBcolor[2]) + 100
    
        if RedC > 255:
            RedC = 255
        if GreenC > 255:
            GreenC = 255
        if BlueC > 255:
            BlueC = 255
    
        RGB2INT = RedC << 16 ^ GreenC << 8 ^ BlueC
    
        if RGB2INT < 6582527 or RGB2INT > 16777158:
            await ctx.send("This color **will** have a red glitch in the lobby.")
        else:
            await ctx.send("This color **won't** have a red glitch in the lobby.")

# Make the command load & work
def setup(bot):
    bot.add_command(validate)

@validate.error
async def validate_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !validate [color code]")