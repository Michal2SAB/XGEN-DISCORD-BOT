# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from Tools import sa
from Tools.sa import *
from configparser import ConfigParser

# Server shortcuts and their ips & ports
ServerNames = {'2dc': '45.76.234.65:1138', 'ptc': '45.76.235.18:1138', 'fli': '45.32.193.38:1138',
               'uofsa': '45.32.192.205:1138', 'mobius': '45.32.192.102:1138', 'eu': '45.63.119.253:1138', 
               'cartesian': '45.32.193.38:1139', 'squaresville': '45.32.193.38:1031', 'lp': '104.238.147.27:1138'}

# Server shrotcuts and their full names
NameServer = {'2dc': '2-Dimensional Central', 'ptc': 'Paper Thin City (RP)', 'fli': 'Fine Line Island / Flat World',
               'uofsa': 'U of SA / Sticktopia', 'mobius': 'Mobius Metropolis / Planar Outpost', 'eu': '{Europe} Amsterdam', 
               'cartesian': 'Cartesian Republic', 'squaresville': 'Squaresville (BoxHead)', 'lp': '{LABPASS} The SS Lineage'}

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

botaccs = config_object["BOT ACCS"]

# Handling users command
@commands.command()
async def users(ctx, server):

# If wrong server specified
    if not (server in ServerNames):
        await ctx.send("Wrong server specified! Use !servers command for help.")

    # If correct server specified
    else:
        BotServer, BotPort = ServerNames[server].split(':') # server & port to connect to

        # Connect to the server and send necessary packets to it
        a = sa.SABot(botaccs['bot'], botaccs['bot_password'], BotServer, int(BotPort), True)
        a.sendPacket(a.SocketConn, '03_') # Appear in lobby
        a.sendPacket(a.SocketConn, '02Z900_') # Appear in lobby v2 (sometimes 03_ doesn't do the job)

        # If the bot account is currently banned, let us know
        if a.banned == True:
            await ctx.send(botaccs['bot'] + " is currently banned, use other bot.")

        # If account not banned, execute the users command
        else:
            time.sleep(0.5) # There is some filtering/blocking going on the server so we gotta wait

            UserList = []
            ModList = []

            # If it's a boxhead server, things are simple
            if server == 'squaresville':
                for User in a.OnlineUserMap:
                    UserList .append(User)

            # If it's a stickarena server, things gotta be a little different
            else:
                try:
                    for User in a.OnlineUserMap:
                        if "[M]" in User:
                            ModList .append(User)
                        if "{B}" in User and "[M]" not in User:
                            UserList = [User] + UserList 
                        else:
                            UserList .append(User)
        
                    if len(ModList) == 0:
                        for mod in ModList:
                            UserList = [mod] + UserList
                except Exception as e:
                    print(e)
      
            print(UserList)

            # If no users in that server
            if len(UserList) == 0:
                await ctx.send(f"There is no one in {NameServer[server]} right now.")

            # If found some users online
            else:
                grammar = "user"

                # Just so we can get the grammar right
                if len(UserList) > 1:
                    grammar = "users"

                # Reply on discord with users count and their names
                embed=discord.Embed(title=f"{NameServer[server]} | {len(UserList)} {grammar} in the lobby.", description="**{}**".format("\n".join(UserList)), color=0x24262B)
                await ctx.send(embed=embed)

            # Close the connection
            a.SocketConn.shutdown(socket.SHUT_RD)
            a.SocketConn.close()

# Make the command load & work
def setup(bot):
    bot.add_command(users)

@users.error
async def users_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !users [server]. Type !servers for the list of server shortcuts.")