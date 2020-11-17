import socket
import struct
import threading
import time

class SABot:
    def __init__(self, Username, Password, IP, Port, Commands):
        self.NullByte = struct.pack('B', 0)
        self.BufSize = 4096
        self.InLobby = False
        self.OnlineUsers = {}
        self.OnlineUserMap = {}
        self.RoomList = {}
        self.NewRoomList = []
        self.FoundUser = ""
        self.Creator = ""
        self.Players = ""
        self.TimeLeft = ""
        self.GameMap = ""
        self.GameMode = ""
        self.banned = False
        self.incorrect = False
        self.labpass = False
        self.creds = ""
        self.botuser = Username

        self.NameToIP = {'2DC': '45.76.234.65:1138', 'Paper': '45.76.235.18:1138', 'fineline':  '45.32.193.38:1138', 'U of SA':  '45.32.192.205:1138',
                                      'europe':  '45.63.119.253:1138',  'Mobius':  '45.32.192.102:1138', 'Cartesian':  '45.32.193.38:1139', 'Squaresville': '45.32.193.38:1031', 'LP Server': '104.238.147.27:1138'}

        self.IPToName = {'45.76.234.65:1138': '2DC', '45.76.235.18:1138': 'Paper', '45.32.193.38:1138': 'Fineline', '45.32.192.205:1138': 'U of SA',
                                               '45.63.119.253:1138': 'europe', '45.32.192.102:1138': 'Mobius', '45.32.193.38:1139': 'Cartesian', '45.32.193.38:1031': 'Squaresville', '104.238.147.27:1138': 'LP Server'}
        
        self.Maps = {'0': 'XGen Hq', '1': 'Sunnyvale Trailer Park', '2': 'Toxic Spillway', '3': 'Workplace Anxiety', '4': 'Storage Yard', '5': 'Green Labirynth',
                     '6': 'Floor Thirteen', '7': 'The Pit', '8': 'Industrial Drainage', '9': 'Globalmegacorp LTD', 'A': 'Concrete Jungle', 'B': 'Nuclear Underground', 
                     'C': 'Unstable Terrace', 'D': 'Office Space', 'E': 'The Foundation', 'F': 'Brawlers Burrow', 'G': 'Trench Run', 'H': 'Corporate Wasteland', 
                     'I': 'Sewage Treatment', 'J': 'Storm Drain', 'K': '{B} Stick Federation HQ', 'L': '{B} Transgalactic Com Station', 'M': '{B} Space Elevator Control', 
                     'N': '{B} Automated Discovery Pod', 'O': '{B} The SF Vengeance', 'P': '{B} Gemini Control Station', 'Q': '{B} Outpost', 'R': '{B} Space Mountain', 'S': '{B} Barge', 
                     'T': '{B} Cliffside', 'U': '{B} Orbit', 'a': '{F} Abandoned City (by Sk1)', 'b': '{F} Anarchy Streets (by Bloodsyn)', 'c': '{F} Cruelity (by Jzuo)', 'd': '{F} Desert Laboratory (by Crocodile)',
                     'e': '{F} Exploration (by Difficult)', 'f': '{F} Facility (by Shadowcasterx4ffc', 'g': '{F} Failcorp (by Enclave)', 'h': '{F} Fortmoon (by Hanktankerous)', 'i': '{F} Island Hopping (by Infal)',
                     'j': '{F} Lost Facility (by Volt)', 'k': '{F} Lowzone (by Springbranch, Stickslayer138)', 'l': '{F} Marked Territory (by Coldhot)', 'm': '{F} My pet glock (by Joe7777777)', 'n': '{F} Space Excavations (by 718)', 
                     'o': '{F} Venice Streets (by Jaguar)', 'p': '{F} Office Pod (by Vegeta,rock)', 'q': '{F} Space Bridge (by Bullet.girl.)', 'r': '{F} Elite Base (by Jzuo)', 's': '{F} D Day (by Shot..to..kill...)', 't': '{F} Cliffs (by Masterchuf)',
                     'u': '{F} Last Map (by ,.Smokez.,)', 'v': '{F} Ship dock (by Bridgeofstraw)', 'w': '{F} Radiation (by Jzuo)', 'x': '{F} Shelter (by Jzuo)', 'y': '{F} Sewer Tunnel (by Ghecko)', 'z': '{F} Trench Space (by Jzuo, Dr.wolfe)'}
        
        self.normalMaps = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                           'U', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.ServerIP = IP
        self.ServerPort = Port
        self.BotServer = self.IPToName[ '{}:{}'.format(self.ServerIP, self.ServerPort)]
            
        self.connectToServer(Username, Password, self.ServerIP, self.ServerPort)

    def sendPacket(self, Socket, PacketData, Receive = False):
        Packet = bytes(PacketData, 'utf-8')

        if Socket:
            Socket.send(Packet + self.NullByte)

            if Receive:
                return Socket.recv(self.BufSize).decode('utf-8')
            
    def calculate_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        self.TimeLeft = "%02d:%02d" % (mins, secs)
        
    def connectionHandler(self):
        Buffer = b''

        while hasattr(self, 'SocketConn'):
            try:
                Buffer += self.SocketConn.recv(self.BufSize)
            except OSError:
                if hasattr(self, 'SocketConn'):
                    pass
                    #self.SocketConn.shutdown(socket.SHUT_RD)
                    #self.SocketConn.close()

            if len(Buffer) == 0:
                print(f'Disconnected {self.botuser} from {self.BotServer}')
                break
            elif Buffer.endswith(self.NullByte):
                Receive = Buffer.split(self.NullByte)
                Buffer = b''

                for Data in Receive:
                    Data = Data.decode('utf-8')
                  
                    if Data.startswith('U'):
                        UserID = Data[1:][:3]
                        Username = Data[4:][:20].replace('#', '')

                        self.parseUserData(Data)
                    elif Data.startswith('D'):
                        UserID = Data[1:][:3]
                        Username = self.OnlineUsers[UserID]

                        del self.OnlineUserMap[Username]
                        del self.OnlineUsers[UserID]
                    elif Data.startswith('0g') or Data.startswith('0j'):
                        print('{{Server}}: ' + Data[2:])
                    elif Data.startswith('093'):
                        print(f"Secondary login with '{self.botuser}' in {self.BotServer}")
                        break
                    elif Data.startswith('0f') or Data.startswith('0e'):
                        Time, Reason = Data[2:].split(';')
                        print(f'{self.botuser} has just been banned [Time: {Time} / Reason: {Reason}]')
                    elif Data.startswith('0c'):
                        print(Data[2:])
                    elif Data.startswith('01'):
                        if self.BotServer == "Squaresville":
                            self.RoomList = Data[4:].split(';')
                        else:
                            for Room in Data[2:].split('0;'):
                                self.RoomList = Data[2:].split('0;')
                                #self.RoomList = Data[2:].split('0;')
                                    
                    elif Data.startswith('0h'):
                        if 'located' in str(Data[2:]):
                            self.FoundUser = str(Data[2:])
                    
                    elif Data.startswith('06'):
                        if str(Data[2:][:2]) == "mp":
                            #print(str(Data[5:][:1]))
                            myMap = str(Data[5:][:1])
                            if myMap in self.normalMaps:
                              self.GameMap = self.Maps[myMap]
                            else:
                              self.GameMap = myMap
                        else:
                            self.Creator = str(Data[5:])
                        
                    elif Data.startswith('04'):
                        if self.BotServer == 'Squaresville':
                            if str(Data[5:][:1]) == "0":
                                self.Players = str(Data[6:][:1]) + "/16"
                            else:
                                self.Players = str(Data[5:][:2]) + "/16"
                        else:
                            #print(str(Data))
                            self.Players = str(Data[4:][:1]) + "/4"
                            timeleft = str(Data[5:][:3])
                            timeleft = int(timeleft)-30
                            self.calculate_time(timeleft)
                            if str(Data[3:][:1]) == "2":
                                self.GameMode = "Repeat"
                            elif str(Data[3:][:1]) == "0":
                                self.GameMode = "Cycle"
                            elif str(Data[3:][:1]) == "1":
                                self.GameMode = "Random"
                        

    def connectToServer(self, Username, Password, ServerIP, ServerPort):
        try:
           self.SocketConn = socket.create_connection((ServerIP, ServerPort))
        except Exception as Error:
            print(Error)
            return

        Handshake = self.sendPacket(self.SocketConn, '08HxO9TdCC62Nwln1P', True).strip(self.NullByte.decode('utf-8'))

        if Handshake == '08':
            Credentials = '09{};{}'.format(Username, Password)
            RawData = self.sendPacket(self.SocketConn, Credentials, True).split(self.NullByte.decode('utf-8'))

            for Data in RawData:
                if Data.startswith('A'):
                    self.InLobby = True
                    if self.BotServer != "Squaresville":
                        self.sendPacket(self.SocketConn, "0a")
                        self.creds = Data[3 + len(Username):].replace('#', '').split(';')[8]
                        #print(self.creds)
                        if Data[3 + len(Username):].replace('#', '').split(';')[5] == "1":
                          self.labpass = True

                    print(f'Logged in to {self.BotServer} with {self.botuser}')

                    ConnectionThread = threading.Thread(target=self.connectionHandler)
                    ConnectionThread.start()
                    break
                elif Data == '09':
                    self.incorrect = True
                    print('Incorrect password for ' + self.botuser)
                    break
                elif Data == '091':
                    self.banned = True
                    print(self.botuser + ' is currently banned')
                    break
        else:
            print('Server capacity check failed for ' + self.BotServer)

    def parseUserData(self, Packet, Password = None):
        StatsString = Packet.replace('\x00', '')
        UserID = StatsString[1:][:3]
        Type = StatsString[:1]

        if Type == 'U':
            if self.InLobby == True:
                Username = StatsString[4:][:20].replace('#', '')
                if self.BotServer == "Squaresville":
                    self.OnlineUsers[UserID] = Username
                    self.OnlineUserMap[Username] = UserID
                else:                
                    Labpass = StatsString.split(";")[5]
                    Mod = StatsString.split(";")[6]
                
                    lpString = ""
                    modString = ""
                
                    if Labpass == "1":
                        lpString = "{B} "
                    if int(Mod) > 0:
                        modString = "[M] "
                    
                    self.OnlineUsers[UserID] = modString + lpString + Username
                    self.OnlineUserMap[modString + lpString + Username] = UserID
        
if __name__ == '__main__':
    SABot('',  '', '', 1138, True)