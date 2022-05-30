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
