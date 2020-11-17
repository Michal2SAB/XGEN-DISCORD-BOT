from configparser import SafeConfigParser
import requests
from requests.exceptions import Timeout
from xml.dom import minidom

parser = SafeConfigParser()
parser.read('config.ini')

try:
    Username = input("Your bot name: ")
    Password = input("What password to use: ")
    Color = "113000150"
    Count = 0
    nr = ''
    while Count < 7:
        if Count > 0:
            nr = str(Count)
        PostData = {"username": Username + nr, "userpass": Password, "usercol": Color, "action": "create"}
        URLData = requests.post("http://www.xgenstudios.com/stickarena/stick_arena.php", data=PostData, timeout=10).text
 
        if "success" in URLData:
            print("Successfully created '" + Username + nr + "'")

            parser.set('BOT ACCS', 'bot' + nr, Username + nr)
            parser.set('BOT ACCS', 'bot_password', Password)

            with open('config.ini', 'w') as configfile:
                parser.write(configfile)
        else:
            print("Could not create: '" + Username + nr + "'")

        Count += 1
        
except Timeout:
    print("Your request timed out, try again.")
except Exception as Error:
    print(Error)