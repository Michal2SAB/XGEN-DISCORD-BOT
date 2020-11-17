from Tools import sa
from Tools.sa import *
from configparser import ConfigParser
from bs4 import BeautifulSoup
import requests

config_object = ConfigParser()
config_object.read("config.ini")
botaccs = config_object["BOT ACCS"]

CustomMaps = {'V': '0', 'W': '1', 'X': '2', 'Y': '3', 'Z': '4'}

def isBanned(*values):
    nr = ''
    for a in enumerate(values):
        if a[1].banned == True:
            if values[0] > 0:
                nr = str(values[0])
            return botaccs['bot' + nr] + " is currently banned, use other bot."
        else:
            return False

def disconnect(*values):
    for a in values:
        a.SocketConn.shutdown(socket.SHUT_RD)
        a.SocketConn.close()

def loadCustomMap(MapName, gameCreator):
    try:
        mapSlot = CustomMaps[MapName]

        APIURL = f'http://api.xgenstudios.com/?method=xgen.stickarena.maps.get&username={gameCreator}&slot_id={mapSlot}'
        httpAPI = requests.get(APIURL).text
        APIData = BeautifulSoup(httpAPI, "html.parser")
      
        CustomMapName = APIData.find("name").string
        mapSlotConvert = int(mapSlot) + 1
      
        return CustomMapName + f" ({gameCreator}, slot {str(mapSlotConvert)})"
    except Exception as e:
        print(e)
        pass