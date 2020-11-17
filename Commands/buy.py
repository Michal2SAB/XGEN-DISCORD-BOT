# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from Tools import sa
from Tools.sa import *
import re

Spinners = {'oldskool': '100', 'spiral': '101', 'neon':  '102', 'radioactive':  '103',
            'skulls':  '104',  'minimalist':  '105', 'retro':  '106', 'buttercup': '107', 'thehex': '108', 'yinyang': '109',
           'revolution': '110', 'wrongway': '111', 'vinyl': '112', 'razorblades': '113', 'hollywood': '114', 'rebel': '115', 
            'chance': '116', 'thepro': '117', 'omega': '118', 'biohazard': '119', 'triskelion': '120', '1337': '121', 'glint': '122', 
            'theplague': '123', 'roflmao': '124', 'brainwash': '125', 'shuriken': '126', '4thdimensions': '127', 'affluenza': '128', 
            'dabomb': '129', 'the8bit': '130', 'flux': '131', 'theofficer': '132', 'solar': '133', 'ouroboros': '134', 'stealth': '135',
           'bullettime': '136', 'baller': '137', 'wakkawakka': '138', 'gearsofgore': '139', 'pyro': '140', 'assassin': '141', 'globe': '142',
           'galaxy': '143', 'teabag': '144', 'canttouchthis': '145', 'fireworks': '146', 'jaws': '147', 'plop': '148', 'dimspinner1': '149',
           'dimspinner2': '150', 'fakeassassin': '151'}

SpinnersCost = {'oldskool': '120', 'spiral': '130', 'neon':  '370', 'radioactive':  '990',
            'skulls':  '350',  'minimalist':  '420', 'retro':  '500', 'buttercup': '540', 'thehex': '660', 'yinyang': '710',
           'revolution': '775', 'wrongway': '850', 'vinyl': '980', 'razorblades': '1500', 'hollywood': '3300', 'rebel': '4100', 
            'chance': '6500', 'thepro': '9001', 'omega': '2500', 'biohazard': '5200', 'triskelion': '2700', '1337': '1337', 'glint': '5350', 
            'theplague': '6800', 'roflmao': '1700', 'brainwash': '910', 'shuriken': '2350', '4thdimensions': '1259', 'affluenza': '15000', 
            'dabomb': '1850', 'the8bit': '2925', 'flux': '3900', 'theofficer': '625', 'solar': '3450', 'ouroboros': '4600', 'stealth': '12000',
           'bullettime': '4000', 'baller': '2600', 'wakkawakka': '4800', 'gearsofgore': '3200', 'pyro': '6000', 'assassin': '24000', 'globe': '880',
           'galaxy': '3400', 'teabag': '4600', 'canttouchthis': '5800', 'fireworks': '3750', 'jaws': '3330', 'plop': '1450', 'dimspinner1': '8800',
           'dimspinner2': '7600', 'fakeassassin': '2200'}

@commands.command(aliases=['purchase', 'buyspinner'])
async def buy(ctx, account, PW, spinnerID, color1, color2):
    allowedChars = set('0123456789-')
    RGBcolor1 = re.findall('...',color1)
    RGBcolor2 = re.findall('...',color2)
  
    mathNumbers1 = int(RGBcolor1[0]) + int(RGBcolor1[1]) + int(RGBcolor1[2])
    mathNumbers2 = int(RGBcolor2[0]) + int(RGBcolor2[1]) + int(RGBcolor2[2])
  
    if mathNumbers1 < 248:
        await ctx.send("The color code given for name color will not work. The total value is less than 248.")
    elif mathNumbers1 > 522:
        await ctx.send("The color code given for name color will not work. The total value is greater than 522.")
    else:
        if int(RGBcolor1[0]) < 128 and int(RGBcolor1[1]) < 128 and int(RGBcolor1[2]) < 128:
            await ctx.send("The color code given for name color will not work. Atleast 1 out of the RED, GREEN or BLUE numbers got to be 128 or greater.")
        elif int(RGBcolor1[0]) == int(RGBcolor1[1]) and int(RGBcolor1[0]) == int(RGBcolor1[2]) and int(RGBcolor1[1]) == int(RGBcolor1[2]):
            await ctx.send("The color code given for name color will not work. All 3 RGB values cannot be the same.")
        elif "-" in RGBcolor1[1] or "-" in RGBcolor1[2]:
            await ctx.send("The color code given for name color will not work. Green and Blue values cannot be negatives, only Red can be.")
        elif int(RGBcolor1[0]) > 255 or int(RGBcolor1[1]) > 255 or int(RGBcolor1[2]) > 255:
            await ctx.send("The color code given for ring color will not work. Neither Red, Green or Blue value can be greater than 255.")
        elif len(color1) != 9:
            await ctx.send("Invalid first (name) color code given. Format: RRRGGGBBB")
        elif set(color1).issubset(allowedChars) != True:
            await ctx.send("Invalid first (name) color code given. You can only use the minus symbol and numbers.")
        else:
            if mathNumbers2 < 248:
                await ctx.send("The color code given for ring color will not work. The total value is less than 248.")
            elif mathNumbers2 > 522:
                await ctx.send("The color code given for ring color will not work. The total value is greater than 522.")
            else:
                if int(RGBcolor2[0]) < 128 and int(RGBcolor2[1]) < 128 and int(RGBcolor2[2]) < 128:
                    await ctx.send("The color code given for ring color will not work. Atleast 1 out of the RED, GREEN or BLUE numbers got to be 128 or greater.")
                elif int(RGBcolor2[0]) == int(RGBcolor2[1]) and int(RGBcolor2[0]) == int(RGBcolor2[2]) and int(RGBcolor2[1]) == int(RGBcolor2[2]):
                    await ctx.send("The color code given for ring color will not work. All 3 RGB values cannot be the same.")
                elif "-" in RGBcolor2[1] or "-" in RGBcolor2[2]:
                    await ctx.send("The color code given for ring color will not work. Green and Blue values cannot be negatives, only Red can be.")
                elif int(RGBcolor2[0]) > 255 or int(RGBcolor2[1]) > 255 or int(RGBcolor2[2]) > 255:
                    await ctx.send("The color code given for ring color will not work. Neither Red, Green or Blue value can be greater than 255.")
                elif len(color2) != 9:
                    await ctx.send("Invalid secondary (ring) color code given. Format: RRRGGGBBB")
                elif set(color2).issubset(allowedChars) != True:
                    await ctx.send("Invalid secondary (ring) color code given. You can only use the minus symbol and numbers.")
                else:
                    if not (spinnerID in Spinners):
                        await ctx.send("This spinner doesn't exist. Use !spinners command to get the list of available spinners.")
                    else:
                        await ctx.send("Attempting to purchase your item...")
                        a = sa.SABot(account, PW, '45.32.192.205', 1138, True)
                        if a.incorrect == True:
                            await ctx.send(f"Incorrect password for {account}. Cannot purchase item.")
                        elif a.banned == True:
                            await ctx.send(account + " is currently banned. Cannot purchase item.")
                        else:
                            if int(Spinners[spinnerID]) > 109:
                                if a.labpass == False:
                                    await ctx.send(f"Your account does not have labpass and it is required to purchase '{spinnerID}'. Please try a different spinner.")
                                else:
                                    if int(a.creds) < int(SpinnersCost[spinnerID]):
                                        await ctx.send(f"You do not have enough creds to purchase '{spinnerID}'. You have {a.creds} creds and the spinner costs {SpinnersCost[spinnerID]} creds.")
                                    else:
                                        a.sendPacket(a.SocketConn, "0b" + Spinners[spinnerID] + color1 + color2)
                                        await ctx.send(f"Successfully purchased '{spinnerID}' on the account '{account}' for {SpinnersCost[spinnerID]} creds.")
                            else:
                                if int(a.creds) < int(SpinnersCost[spinnerID]):
                                    await ctx.send(f"You do not have enough creds to purchase '{spinnerID}'. You have {a.creds} creds and the spinner costs {SpinnersCost[spinnerID]} creds.")
                                else:
                                    a.sendPacket(a.SocketConn, "0b" + Spinners[spinnerID] + color1 + color2)
                                    await ctx.send(f"Successfully purchased '{spinnerID}' on the account '{account}' for {SpinnersCost[spinnerID]} creds.")

                        a.SocketConn.shutdown(socket.SHUT_RD)
                        a.SocketConn.close()

# Make the command load & work
def setup(bot):
    bot.add_command(buy)

@buy.error
async def buy_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !buy [user] [password] [spinner] [color1] [color2]")