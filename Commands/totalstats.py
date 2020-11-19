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

# Server shortcuts and their ips & ports
ServerNames = {'2dc': '45.76.234.65:1138', 'ptc': '45.76.235.18:1138', 'fli': '45.32.193.38:1138',
               'uofsa': '45.32.192.205:1138', 'mobius': '45.32.192.102:1138', 'eu': '45.63.119.253:1138', 
               'cartesian': '45.32.193.38:1139', 'squaresville': '45.32.193.38:1031', 'lp': '104.238.147.27:1138'}

# Handling totalstats command 
# This whole code is a fucking mess but you shouldn't care as long it works probably..
@commands.command(aliases=['total', 'ts', 'activity'])
async def totalstats(ctx):

    # Separating server & port for the servers
    dc2Server, dc2Port = ServerNames['2dc'].split(':')
    ptcServer, ptcPort = ServerNames['ptc'].split(':')
    fliServer, fliPort = ServerNames['fli'].split(':')
    uofsaServer, uofsaPort = ServerNames['uofsa'].split(':')
    euServer, euPort = ServerNames['eu'].split(':')
    mobiusServer, mobiusPort = ServerNames['mobius'].split(':')
    cartesianServer, cartesianPort = ServerNames['cartesian'].split(':')

    # Connect to all servers using all of our bot accounts
    a = sa.SABot(botaccs['bot'], botaccs['bot_password'], dc2Server, int(dc2Port), True)
    a1 = sa.SABot(botaccs['bot1'], botaccs['bot_password'], ptcServer, int(ptcPort), True)
    a2 = sa.SABot(botaccs['bot2'], botaccs['bot_password'], fliServer, int(fliPort), True)
    a3 = sa.SABot(botaccs['bot3'], botaccs['bot_password'], uofsaServer, int(uofsaPort), True)
    a4 = sa.SABot(botaccs['bot4'], botaccs['bot_password'], euServer, int(euPort), True)
    a5 = sa.SABot(botaccs['bot5'], botaccs['bot_password'], mobiusServer, int(mobiusPort), True)
    a6 = sa.SABot(botaccs['bot6'], botaccs['bot_password'], cartesianServer, int(cartesianPort), True)

    accsList = (a, a1, a2, a3, a4, a5, a6)

    # Send necessary packets to each server
    for botacc in accsList:
        botacc.sendPacket(botacc.SocketConn, '03_') # Appear in lobby
        botacc.sendPacket(botacc.SocketConn, '02Z900_') # Appear in lobby v2 (sometimes 03_ doesn't do the job)
        botacc.sendPacket(botacc.SocketConn, '01') # Show us all games in the room

    time.sleep(0.5) # There is some filtering/blocking going on the server so we gotta wait..

    # Check if any of our bot accounts are banned and let us know if so
    accBanned = acs.isBanned(a, a1, a2, a3, a4, a5, a6)
    if accBanned != False:
        await ctx.send(accBanned)
    
    # If no accounts banned, do the work
    else:
        UserList = []
        UserList1 = []
        UserList2 = []
        UserList3 = []
        UserList4 = []
        UserList5 = []
        UserList6 = []
    
        GameList = []
        GameList1 = []
        GameList2 = []
        GameList3 = []
        GameList4 = []
        GameList5 = []
        GameList6 = []
      
        users2dc = "Users:"
        games2dc = "Games:"
        usersptc = "Users:"
        gamesptc = "Games:"
        usersfli = "Users:"
        gamesfli = "Games:"
        usersuofsa = "Users:"
        gamesuofsa = "Games:"
        userseu = "Users:"
        gameseu = "Games:"
        usersmobius = "Users:"
        gamesmobius = "Games:"
        userscart = "Users:"
        gamescart = "Games:"
      
        gameline2dc = "\n"
        gamelineptc = "\n"
        gamelinefli = "\n"
        gamelineuofsa = "\n"
        gamelineeu = "\n"
        gamelinemobius = "\n"
        gamelinecart = "\n"

        for User in a.OnlineUserMap:
            UserList .append(User)
          
        for User1 in a1.OnlineUserMap:
            UserList1 .append(User1)
        
        for User2 in a2.OnlineUserMap:
            UserList2 .append(User2)
        
        for User3 in a3.OnlineUserMap:
            UserList3 .append(User3)
            
        for User4 in a4.OnlineUserMap:
            UserList4 .append(User4)
        
        for User5 in a5.OnlineUserMap:
            UserList5 .append(User5)
            
        for User6 in a6.OnlineUserMap:
            UserList6 .append(User6)
      
        for Game in a.RoomList: 
            GameList .append(Game)
      
            if '_0' in GameList:
                GameList.remove('_0')
            if '' in GameList:
                GameList.remove('')
            if '_' in GameList:
                GameList.remove('_')
        
        for Game in a1.RoomList:
            GameList1 .append(Game)
      
            if '_0' in GameList1:
                GameList1.remove('_0')
            if '' in GameList1:
                GameList1.remove('')
            if '_' in GameList1:
                GameList1.remove('_')
        
        for Game in a2.RoomList:
            GameList2 .append(Game)
      
            if '_0' in GameList2:
                GameList2.remove('_0')
            if '' in GameList2:
                GameList2.remove('')
            if '_' in GameList2:
                GameList2.remove('_')
        
        for Game in a3.RoomList:
            GameList3 .append(Game)
      
            if '_0' in GameList3:
                GameList3.remove('_0')
            if '' in GameList3:
                GameList3.remove('')
            if '_' in GameList3:
                GameList3.remove('_')
        
        for Game in a4.RoomList:
            GameList4 .append(Game)
      
            if '_0' in GameList4:
                GameList4.remove('_0')
            if '' in GameList4:
                GameList4.remove('')
            if '_' in GameList4:
                GameList4.remove('_')
        
        for Game in a5.RoomList:
            GameList5 .append(Game)
      
            if '_0' in GameList5:
                GameList5.remove('_0')
            if '' in GameList5:
                GameList5.remove('')
            if '_' in GameList5:
                GameList5.remove('_')
        
        for Game in a6.RoomList:
            GameList6 .append(Game)
      
            if '_0' in GameList6:
                GameList6.remove('_0')
            if '' in GameList6:
                GameList6.remove('')
            if '_' in GameList6:
                GameList6.remove('_')
      
        totalUsers = len(UserList)+len(UserList1)+len(UserList2)+len(UserList3)+len(UserList4)+len(UserList5)+len(UserList6)
        totalGames = len(GameList)+len(GameList1)+len(GameList2)+len(GameList3)+len(GameList4)+len(GameList5)+len(GameList6)
      
        if len(UserList) == 0:
            users2dc = ""
        if len(GameList) == 0:
            games2dc = ""
            gameline2dc = ""
        if len(UserList1) == 0:
            usersptc = ""
        if len(GameList1) == 0:
            gamesptc = ""
            gamelineptc = ""
        if len(UserList2) == 0:
            usersfli = ""
        if len(GameList2) == 0:
            gamesfli = ""
            gamelinefli = ""
        if len(UserList3) == 0:
            usersuofsa = ""
        if len(GameList3) == 0:
            gamesuofsa = ""
            gamelineuofsa = ""
        if len(UserList4) == 0:
            userseu = ""
        if len(GameList4) == 0:
            gameseu = ""
            gamelineeu = ""
        if len(UserList5) == 0:
            usersmobius = ""
        if len(GameList5) == 0:
            gamesmobius = ""
            gamelinemobius = ""
        if len(UserList6) == 0:
            userscart = ""
        if len(GameList6) == 0:
            gamescart = ""

        # If no games and no users online
        if totalUsers == 0 and totalGames == 0:
            await ctx.send("SA is completely dead right now. No games and no users online :sob:")
        else:
            embed=discord.Embed(title=f"Total Users: {totalUsers} / Total Games: {totalGames}", description="**2-Dimensional Central**\n\n{} {}\n{} {} {}\n**Paper Thin City**\n\n{} {}\n{} {} {}\n**Fine Line Island \ Flat World**\n\n{} {}\n{} {} {}\n**U of SA \ Sticktopia**\n\n{} {}\n{} {} {}\n**Europe Amsterdam**\n\n{} {}\n{} {} {}\n**Mobius Metropolis \ Planar Outpost**\n\n{} {}\n{} {} {}\n**Cartesian Republic**\n\n{} {}\n{} {} {}\n".format(users2dc, ', '.join(UserList), games2dc, ', '.join(GameList), gameline2dc, usersptc, ', '.join(UserList1), gamesptc, ', '.join(GameList1), gamelineptc, usersfli, ', '.join(UserList2), gamesfli, ', '.join(GameList2), gamelinefli, usersuofsa, ', '.join(UserList3), gamesuofsa, ', '.join(GameList3), gamelineuofsa, userseu, ', '.join(UserList4), gameseu, ', '.join(GameList4), gamelineeu, usersmobius, ', '.join(UserList5), gamesmobius, ', '.join(GameList5), gamelinemobius, userscart, ', '.join(UserList6), gamescart, ', '.join(GameList6), gamelinecart), color=0x24262B)
            await ctx.send(embed=embed)

        # Disconnect from all servers after done its job
        acs.disconnect(a, a1, a2, a3, a4, a5, a6)

# Make the command load & work
def setup(bot):
    bot.add_command(totalstats)
