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
