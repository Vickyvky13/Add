import os
from colorama import init, Fore
from time import sleep
import csv
import time
import random
import os
import pickle
import sys
scam = '@notoscam'
init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
be = Fore.BLUE
colors = [lg, r, w, cy, ye]


def banner():
    os.system('clear')
    print(f"""
{cy}
          
 __----__     
(   p p  ).  
(____||__)__ ██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗{r}
  /  || \/ / ██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║{lg}
 / /  - |_/  ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██╔████╔██║{ye}
 \_\    |.   ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║{be}
  |= = =|.   ░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║{w}
  '-----'.   ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝
  |_) |_)  


""")
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    clr()
    banner()
    print(ye+'Choose an Option:'+n)
    print(cy+'            [1] Setup Script'+n)
    print(cy+'            [2] Exit'+n)
    a = int(input('\n Enter your choice: '))
    if a == 1:
    
       print("[+] Installing requierments ...")
       os.system('pip install telethon==1.24.0')
       os.system('pip install termcolor')
       os.system('pip install colorama')
       os.system('pip install requests')
       os.system('pip install rich')
       os.system('pip install newthon')
       os.system('pip install pyrogram')
       os.system('pip install tgcrypto')
       os.system('pip install IP2Location')
       os.system('pip install pytz')
       os.system('pip install licensing')
       os.system('pip install pyfiglet')

       print("[+] setup complete !")
       print("[+] now you can run any tool !")
       input(f'\n Press enter to goto main menu...')
       
    if a == 2:
        clr()
        banner()
        exit()