# XGEN-DISCORD-BOT

A discord bot for XGenStudios. Mostly for stick arena. Just thought I'd release the rewritten and easy to use version for those who still play sa and shit and wanna run the bot in their server, cause I don't care about these games anymore and I won't bring the bot back myself.

# REQUIREMENTS

1. You need python 3.6 or newer installed on your computer. Make sure to check "add to PATH" option in the installer.
2. After you have installed python, download this repository as .zip file. Or go to the releases page and download this project.
3. After you downloaded and unpacked the folder, go to the folder "Install Modules". 
4. Then run the file 'install.bat'. It will install all the required modules for this project for you.
5. If you see any errors, you might need to also download and install this: https://sourceforge.net/projects/gtk-win/files/latest/download

# HOW TO RUN THIS BOT

1. After you done the stuff above, you can go back and get to editing the config.ini file. You can open it with notepad or any other editor.
2. In config.ini you have bunch of variables that you need to edit. Bot token, your admin name.. etc. You will get it once you open it. To set your bot accounts for sa, just run 'botGenerator.py'. It will help you create the bots and edit the variables in config.ini file for you so you don't have to do that manually.
3. You don't need to edit the bot_prefix, bot_activity, bot_status_text, bot_status variables.
4. After you set all the variables, you can just run the 'run.py' file and your bot will start in the server you invited it to.
5. If you don't know how to get a discord bot token or how to invite the bot to your server, just google it, there are tons of tutorials for that.
6. And that's all. Have fun I guess. The bot is pretty much yours (kinda).
7. Also, don't edit any of the .py files unless you know what you're doing.

# COMMANDS
```diff
!stats [account] - Lookup stats for a Stick Arena account.

!statsbbh [account] - Lookup stats for a Boxhead account. Aliases: !bbhstats, !bbh, !statsboxhead, !boxheadstats

!oldstats [account] - Check stats for an account before the dumb reset. Aliases: !old, !prevstats, !statsold

!prems [account] - Lookup premium items for a boxhead account. Aliases: !premiums

!users [server] - Check who's currently online in a specified Stick Arena server.

!games [server] - Check what games are currently available in a specified Stick Arena server.

!gameinfo [server] [game name] - Check info on a specified game in a specified Stick Arena server. Aliases: !info

!creator [server] [game name] - Check who created a specified game in a specified Stick Arena server.

!find [player] - Search for user through all of Stick Arena servers. Aliases: !f

!totalstats - Check how many users are online and how many games are opened in all sa servers. Aliases: !total, !ts, !activity

!create [username] [password] [optional color code] - Create a new XGen account. Aliases: !createacc, !make

!namechange [current name] [password] [new name] - Change your XGen username. Aliases: !change, !changename

!check [primary color code] [optional secondary] - Generate profile with your given color code for name and spinner. Aliases: !spinner, !color, !checkcolor, !checkspinner, !cp

!randomcolor - Generate random sa color (to request only working color code, type !randomcolor valid). Aliases: !rand, !random, !randcol, !randcolor

!oldskool [RRRGGGBBB] [RRRGGGBBB] - Generate oldskool spinner with the color code you specified. Aliases: !os

!pro [RRRGGGBBB] [RRRGGGBBB] - Generate the pro spinner with the code code you specified. Aliases: !thepro

!validate [RRRGGGBBB] - Check if a color code will have a red glitch in Stick Arena lobby. Aliases: !valid, !validcolor, !validatecolor

!buy [account] [password] [spinner] [RRRGGGBBB] [RRRGGGBBB] - Buy any Stick Arena spinner of any color code. Aliases: !purchase, !buyspinner

!verify [account] [password] [email] - Verify an xgen account.

!recover [email] - Recover an xgen account. Aliases: !recov, !lostacc, !lost

!servers - Server names for !users, !games, !creator and !gameinfo commands.

!spinners - List of SA spinners that you can purchase with bot. (For !buy command).

!staff - Give link to current XGen staff forum thread. Aliases: !admins, !mods

!forums - Request for XGen forums link. Aliases: !forumslink, !forum, !discourse

!highscores - Request for all Stick Arena highscores links. Aliases: !hs, !leaderboard, !lb

!xgenapis - Request a list of all (useful) XGen apis. Aliases: !apis, !apiurls

!maptools - Request for available Stick Arena map tools. Aliases: !eedok

!commands - Obviously get the list of all commands. Aliases: !cmds, !command

!help - What the hell is this bot? Yea.. that command is for that.
```
