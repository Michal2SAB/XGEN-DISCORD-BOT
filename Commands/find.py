# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from Tools import sa
from Tools.sa import *
from Tools import actions as acs
from configparser import ConfigParser

# Extracting variables from config file
config_object = ConfigParser()
config_object.read("config.ini")
botaccs = config_object["BOT ACCS"]

# Something that we will use in order to determine in what server a player is located in
nrToServer = {0: '2-Dimensional Central', 1: 'Paper Thin City', 2: 'Fine Line Island/Flat World', 
3: 'U of SA', 4: 'Europe Amsterdam', 5: 'Mobius Metropolis/Planar Outpost', 6: 'Cartesian Republic'}

@commands.command(aliases=['f'])
async def find(ctx, player):

    # Connecting to all sa servers using all of our bots
    a = sa.SABot(botaccs['bot'], botaccs['bot_password'], '45.76.234.65', 1138, True)
    a1 = sa.SABot(botaccs['bot1'], botaccs['bot_password'], '45.76.235.18', 1138, True)
    a2 = sa.SABot(botaccs['bot2'], botaccs['bot_password'], '45.32.193.38', 1138, True)
    a3 = sa.SABot(botaccs['bot3'], botaccs['bot_password'], '45.32.192.205', 1138, True)
    a4 = sa.SABot(botaccs['bot4'], botaccs['bot_password'], '45.63.119.253', 1138, True)
    a5 = sa.SABot(botaccs['bot5'], botaccs['bot_password'], '45.32.192.102', 1138, True)
    a6 = sa.SABot(botaccs['bot6'], botaccs['bot_password'], '45.32.193.38', 1139, True)

    # Sending packets, requesting a "/find" command on each server
    accsList = (a, a1, a2, a3, a4, a5, a6)
    for a in accsList:
        a.sendPacket(a.SocketConn, '0h' + player)

    time.sleep(0.5) # We gotta wait
    
    accBanned = acs.isBanned(a, a1, a2, a3, a4, a5, a6) # Check if any of our bots is banned
    if accBanned != False:
        await ctx.send(accBanned)
        
    # If no bot accounts banned, do the work
    else:
        foundUser = False
        for acc in enumerate(accsList):

            # If found a user in some server, let us know and stop the loop
            if acc[1].FoundUser != '':
                await ctx.send(nrToServer[acc[0]] + ': ' + acc[1].FoundUser)
                foundUser = True
                break
            else:
                foundUser = False

        # If user not found anywhere, let us know
        if foundUser == False:
            await ctx.send(f"Player {player} wasn't found in any server.")

        # Disconnect from all servers after done its job
        acs.disconnect(a, a1, a2, a3, a4, a5, a6)

# Load the command & make it work
def setup(bot):
    bot.add_command(find)

@find.error
async def find_error(error, ctx): 
    return await error.send(error.message.author.mention + " Format: !find [player]")