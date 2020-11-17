# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext import *
from configparser import ConfigParser
from Tools import sa
from Tools.sa import *
from Tools import actions as acs

# Extracting variables from config file
config_object = ConfigParser()
config_object.read("config.ini")
botaccs = config_object["BOT ACCS"]

ServerNames = {'2dc': '45.76.234.65:1138', 'ptc': '45.76.235.18:1138', 'fli': '45.32.193.38:1138',
               'uofsa': '45.32.192.205:1138', 'mobius': '45.32.192.102:1138', 'eu': '45.63.119.253:1138', 
               'cartesian': '45.32.193.38:1139', 'squaresville': '45.32.193.38:1031', 'lp': '104.238.147.27:1138'}

CustomMap = ['V', 'W', 'X', 'Y', 'Z']

@commands.command(aliases=['info'])
async def gameinfo(ctx, server, *, game):
    if not (server in ServerNames):
        await ctx.send("Wrong server specified! Use !servers command for help.")
    else:
        BotServer, BotPort = ServerNames[server].split(':')
        a = sa.SABot(botaccs['bot'], botaccs['bot_password'], BotServer, int(BotPort), True)
        if a.banned == True:
            await ctx.send(botaccs['bot'] + " is currently banned, use other bot.")
        else:
            a.sendPacket(a.SocketConn, f"04{game}")
            a.sendPacket(a.SocketConn, f"06{game};mp")
            time.sleep(0.5)
            a.sendPacket(a.SocketConn, f"06{game};rc")
            time.sleep(0.5)
            if a.Players != '':
                if a.GameMap != '':
                    Players = a.Players
                    TimeLeft = a.TimeLeft
                    MapName = a.GameMap
                    Mode = a.GameMode
                    gameCreator = a.Creator
                    finalMessage = ''
                    if MapName in CustomMap:
                        finalMessage = acs.loadCustomMap(MapName, gameCreator)
                    else:
                        finalMessage = MapName
                    embed=discord.Embed(title=f". : : Game Info For '{game}' in {server.upper()} : : .", description="**Players:** {}\n**Time Left:** {}\n**Map:** {}\n**Mode:** {}\n**Creator:** {}".format(Players, TimeLeft, finalMessage, Mode, gameCreator), color=0x24262B)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(f"Game '{game}' doesn't exist!")
            a.SocketConn.shutdown(socket.SHUT_RD)
            a.SocketConn.close()

# Load the command & make it work
def setup(bot):
    bot.add_command(gameinfo)

@gameinfo.error
async def gameinfo_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !gameinfo [server] [game name]. Type !servers for the list of server shortcuts.")