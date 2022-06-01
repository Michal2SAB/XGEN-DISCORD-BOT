Stick Arena structure, secrets and other cool knowledge that I learned over years. 

# . : : Stick Arena Packet Structure : : .

## Client to Server
| Packet      | Description | Example   |
| :---        |    :---   | :---      |
| 0 | Keep alive packet | 0 |
| 08 | Server capacity check | 08awdWDxasdDWD45    |
| 09 | Login to server | 09username;password |
| 03_ | Join lobby 1 | 03_ |
| 02Z900_ | Join lobby 2 | 02Z900_ |
| 0a | Collect creds ticket | 0a |
| 01 | Check open games list | 01 |
| 9 | Send chat message | 9Hello World |
| 00 + id + P | Send private message to user | 0010fPHello World |
| 00 + id + P + >VIP< | Add user to VIP list | 0010fP>VIP< |
| 00 + id + P + >UNVIP< | Remove user from VIP list | 0010fP>UNVIP< |
| 027200 | Create public game | 027200The Pit
| 03 | Join game | 03XGen Hq |
| 04 | Get game info | 04XGen Hq |
| 06;mp | Get game map | 06XGen Hq;mp |
| 06;rc | Get game creator | 06Xgen Hq;rc |
| 0h | Find user in server | 0hMichal |
| 0b + spinner id + color1 + color2 | Buy spinner | 0b100255000000255000000

## Server to Client
| Packet      | Description |
| :---        | :---        |
| A           | Receive your lobby stats |
| U           | Add new online user to game/lobby and receive their stats |
| D           | Remove user who left lobby/game |
| 08          | Server capacity check success |
| 09          | Incorrect login password |
| 091         | Account is banned |
| 093         | Secondary login |
| 0c          | Receive cred ticket |
| 01          | Receive open games list |
| 04          | Receive info about selected game |
| 06;mp       | Receive map name from selected game |
| 06;rc       | Discover who created selected game |
| 0h          | Receive response for /find command |
| 0f and 0e   | You got banned, ban time and ban message |
| 0g          | Receive mod warning / mod global message |


# . : : Color Code Rules : : .
## Shop Purchase / Create Account
* Total value of RGB ($\color{#FA3535}{Red}$ + $\color{#4CFF4C}{Green}$ + $\color{#3333FF}{Blue}$) can't exceed $\color{#FF7DF6}{522}$
* Total value of RGB ($\color{#FA3535}{Red}$ + $\color{#4CFF4C}{Green}$ + $\color{#3333FF}{Blue}$) can't be less than $\color{#FF7DF6}{248}$
* Atleast one value ($\color{#FA3535}{Red}$ + $\color{#4CFF4C}{Green}$ + $\color{#3333FF}{Blue}$) has to be $\color{#FF7DF6}{128}$ or greater
* $\color{#FA3535}{Red}$, $\color{#4CFF4C}{Green}$ and $\color{#3333FF}{Blue}$ values can't be all the same
* Only $\color{#FA3535}{Red}$ can be a negative value, not $\color{#4CFF4C}{Green}$ or $\color{#3333FF}{Blue}$
* None of the $\color{#FA3535}{Red}$, $\color{#4CFF4C}{Green}$ and $\color{#3333FF}{Blue}$ values can exceed $\color{#FF7DF6}{255}$
* Negative $\color{#FA3535}{Red}$ value doesn't work when creating new account, only through shop purchase

## Red Color Glitch
If RGB [decimal](https://en.wikipedia.org/wiki/Decimal) value is less than $\color{#FF7DF6}{6582527}$ or exceeds $\color{#FF7DF6}{16777158}$, color will appear as red in lobby to other players

This rule doesn't apply to mod users or when in-game

* Math: 
  
  ```Red << 16 ^ Green << 8 ^ Blue```

## Color Transform Rules
Stick Arena transforms RGB colors so $\color{#FF0000}{255000000}$ will not look the same as on some website. 
* Game adds $\color{#FF7DF6}{100}$ to all three $\color{#FA3535}{Red}$, $\color{#4CFF4C}{Green}$ and $\color{#3333FF}{Blue}$ values
* If any value ($\color{#FA3535}{Red}$, $\color{#4CFF4C}{Green}$ or $\color{#3333FF}{Blue}$) is greater than $\color{#FF7DF6}{255}$, they becomes $\color{#FF7DF6}{255}$
* $\color{#FF0000}{255000000}$ RGB will return $\color{#ff6464}{255100100}$ and 255-99-99 will return $\color{#FF0000}{255001001}$

# . : : Moderator Commands, Privileges and Secrets : : .
## Original Commands
* /killroom {game} - Close any game in server
* /ban {user} {level} {reason} - Self explanatory
* /warn {user} {message} - Send a popup box with a warning message to user
* /global {message} - Send a global popup box message to everybody in server
* /ip {user} - Get any user's IP Address
* /kick {user} - Kick any user from game with just 1 vote

## New Special Commands (2015-now)
* !showgames - Get list of all opened games in server, including full ones and private games
* !listplayers {game} - Get a list of all players in specified game
* !disconnect {user} - Kick any user out of server, simulate disconnection
* !creator {game} (uncomfirmed) & /creator {game} (on mod client) - Get the specified game's creator
* /iplookup {user} (on mod client) - Get any user's IP address AND automatically lookup basic info about it (isp, general isp location etc)

## Mod Privileges
* Red color glitch in lobby doesn't apply, no matter what the [decimal](https://en.wikipedia.org/wiki/Decimal) value of RGB is
* Can't be kicked from any game
* 40/60 kills limit in-game doesn't apply
* /find will tell game name even if it's private
* Color code rules for shop purchase don't apply for level 2 mods (unconfirmed)
* Always above everybody's rank in lobby, even labpass players
* XGen admins favouritism, favors and numerous advantages
* Incredible power, little to no responsibility

## Mod Tools

#### 1. Mod Control Panel & Features
Used to be located at http://xgenstudios.com:8000 and later at Neo's webserver. 2017-now either moved, uses ip whitelisting or got built-in in an app because of me.

Features:
* Lookup all accounts tied to specified IP Address (won't find if the alts are currently under different IP)
* Check account ban record; ban date, times, reasons etc.
* Check account's registered e-mail address
* Get IP Address of any user
* Ban any user up to 5 years (regardless of mod level)
* Ban account along with the IP tied to it (default) or ban the account alone
* Check any user's game stats, status, last login date, current IP and current RGB color code, current verified email or unverified one (attempted at account creation)


![mcp](https://github.com/Michal2SAB/XGEN-DISCORD-BOT/raw/main/Screenshot_2.png)

### 2. Mod Client
Custom stick arena flash client created by Neo for moderators

Features:
* Quick action; quick command input upon button click and selected user or game
* /iplookup command
* /creator command (non-mod users can use it too)
* Automatically disconnect/ban anybody who is joining and rejoining lobby too fast (for rcp manipulation purposes for example) - in v2
* Ability to use mod commands sneakily via regular account (incognito mode)

   * v1: by having a mod account join random private game and use its socket connection to send packets
   
   * v2: by having a mod account connect to server but not send lobby appearance packet and use its socket conn to send packets

[![mcc](https://github.com/Michal2SAB/XGEN-DISCORD-BOT/blob/main/Screenshot_3.png)](https://www.youtube.com/watch?v=7AYOveT-t7k)
