# . : : Stick Arena Packet Structure : : .

## Client to Server
| Packet      | Description | Example   |
| :---        |    :---   | :---      |
| 08 | Server capacity check | 08key    |
| 09 | Login to server | 09username;password |
| 02Z900_ | Join lobby | 02Z900_ |
| 03_ | Join lobby 2 | 03_ |
| 0a | Collect creds ticket | 0a |
| 01 | Check open games list | 01 |
| 9 | Send chat message | 9Hello World |
| 00 + id + P | Send private message to user | 0010fPYou're trash |
| 00 + id + P + >VIP< | Add user to VIP list | 0010fP>VIP< |
| 03 | Join game | 03XGen Hq |
