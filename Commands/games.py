# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from Tools import sa
from Tools.sa import *
from configparser import ConfigParser

# Extracting variables from config file
config_object = ConfigParser()
config_object.read("config.ini")
botaccs = config_object["BOT ACCS"]

# Some shit we will use further down the code
ServerNames = {'2dc': '45.76.234.65:1138', 'ptc': '45.76.235.18:1138', 'fli': '45.32.193.38:1138',
               'uofsa': '45.32.192.205:1138', 'mobius': '45.32.192.102:1138', 'eu': '45.63.119.253:1138', 
               'cartesian': '45.32.193.38:1139', 'squaresville': '45.32.193.38:1031', 'lp': '104.238.147.27:1138'}

NameServer = {'2dc': '2-Dimensional Central', 'ptc': 'Paper Thin City (RP)', 'fli': 'Fine Line Island / Flat World',
               'uofsa': 'U of SA / Sticktopia', 'mobius': 'Mobius Metropolis / Planar Outpost', 'eu': '{Europe} Amsterdam', 
               'cartesian': 'Cartesian Republic', 'squaresville': 'Squaresville (BoxHead)', 'lp': '{LABPASS} The SS Lineage'}


# Handling the games command
@commands.command()
async def games(ctx, server):
    lpcheck = ""

    # If wrong server specified, help us
    if not (server in ServerNames):
        await ctx.send("Wrong server specified! Type !servers command for help.")
        
    # If all good, execute the command
    else:

        # Conenct our bot the specified server
        BotServer, BotPort = ServerNames[server].split(':')
        a = sa.SABot(botaccs['bot'], botaccs['bot_password'], BotServer, int(BotPort), True)

        # If banned, let us know
        if a.banned == True:
            await ctx.send(botaccs['bot'] + " is currently banned, use other bot.")

        # If not banned, continue
        else:
            a.sendPacket(a.SocketConn, '01') # Sending a packet, requesting the list of opened games
            time.sleep(0.5) # We gotta wait because of the server bs

            # We will store our games here
            GameList = []
            NewGameList = []
                
            # Stripping the ugly game list from unnecesary characters and making it nice & clean
            for Game in a.RoomList:
                GameList .append(Game)

                if '_0' in GameList:
                    GameList.remove('_0')
                if '' in GameList:
                    GameList.remove('')
                if '_' in GameList:
                    GameList.remove('_')

            # If no games are opened atm, let us know
            if len(GameList) == 0:
                await ctx.send(f"There are no games in {NameServer[server]} right now.")
                
            # If found games, get info
            else:
                grammar = 'game'
                count = len(GameList)

                # if more than 1 game, change the grammar
                if len(GameList) > 1:
                    grammar = 'games'

                try:

                    # If boxhead server
                    if server == 'squaresville':
                        for gamez in GameList: # Run through all games in the list
                            gamez = gamez[2:] # Get the actual game name, without messy character
                            a.sendPacket(a.SocketConn, '04' + gamez) # Sending a packet, requesting info for the game
                            time.sleep(0.5) # we gotta wait because of the server bs

                            NewGameList.append(gamez + f" ({a.Players})") # Add game to our final list

                    # If stickarena server
                    else:
                        for gamez in GameList:

                            # If it's a labpass game
                            if gamez.endswith('1'):
                                gamez = gamez[:-1]
                                lpcheck = "{B} "

                            # If normal game
                            else:
                                lpcheck = ""

                            # Fequest info for the game & add it to our final list
                            a.sendPacket(a.SocketConn, '04' + gamez)
                            time.sleep(0.5)
                            NewGameList.append(lpcheck + gamez + f" ({a.Players})")

                    # Reply to us on discord, with all the games in the server
                    embed=discord.Embed(title=f"{NameServer[server]} | {count} {grammar} opened.", description="**{}**".format("\n".join(NewGameList)), color=0x24262B)
                    await ctx.send(embed=embed)
                except Exception as e:
                    print(e)
                        
            # Disconnect our bot from the server after all done
            a.SocketConn.shutdown(socket.SHUT_RD)
            a.SocketConn.close()

# Load the command & make it work
def setup(bot):
    bot.add_command(games)

@games.error
async def games_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !games [server]. Type !servers for the list of server shortcuts.") 