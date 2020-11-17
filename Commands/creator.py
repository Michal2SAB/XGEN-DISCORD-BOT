# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from Tools import sa
from Tools.sa import *
from configparser import ConfigParser

ServerNames = {'2dc': '45.76.234.65:1138', 'ptc': '45.76.235.18:1138', 'fli': '45.32.193.38:1138',
               'uofsa': '45.32.192.205:1138', 'mobius': '45.32.192.102:1138', 'eu': '45.63.119.253:1138', 
               'cartesian': '45.32.193.38:1139', 'squaresville': '45.32.193.38:1031', 'lp': '104.238.147.27:1138'}
        
# Extracting variables from config file
config_object = ConfigParser()
config_object.read("config.ini")
botaccs = config_object["BOT ACCS"]

# Handling the creator command
@commands.command()
async def creator(ctx, server, *, game):

    # If wrong server specified, help us
    if not (server in ServerNames):
        await ctx.send("Wrong server specified! Use !servers command for help.")

    # If everything good, execute the command
    else:

        # Connect our bot accoutn to the specified server
        BotServer, BotPort = ServerNames[server].split(':')
        a = sa.SABot(botaccs['bot'],  botaccs['bot_password'], BotServer, int(BotPort), True)

        # If our bot acc is banned, let us know
        if a.banned == True:
            await ctx.send(botaccs['bot'] + " is currently banned, use other bot.")

        # If not banned, continue
        else:
            a.sendPacket(a.SocketConn, f"06{game};rc") # Sending a packet, requesting room's creator name
            time.sleep(0.5) # We gotta wait because of the server

            # If game exists, tell us who created it
            if a.Creator != '':
                await ctx.send(f"Creator of '{game}' in {server} = {a.Creator}")

            # If game doesn't exist, let us know
            else:
                await ctx.send(f"Game '{game}' doesn't exist!")

            # Disconnect from the server after the job is done
            a.SocketConn.shutdown(socket.SHUT_RD)
            a.SocketConn.close()

# Load the command & make it work
def setup(bot):
    bot.add_command(creator)

@creator.error
async def creator_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !creator [server] [game name]. Type !servers for the list of server shortcuts.")