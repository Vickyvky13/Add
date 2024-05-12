from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
from telethon.errors.rpcerrorlist import FloodWaitError
import configparser
import sys
import csv
from csv import reader
import traceback
from message import Message
import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from colorama import init, Fore
init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

with open('memory.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)
    row_number = 1
    col_number = 1
    numdel = list_of_rows[row_number - 1][col_number - 1]

Legend_dev = int(numdel)
global nextLegend_dev
nextLegend_dev = Legend_dev + 1

with open('phone.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    row_number = Legend_dev
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]
with open('apis.csv', 'r') as Api_iiid:
    csv_reader = csv.reader(Api_iiid)
    list_of_rows = list(csv_reader)
    row_number = Legend_dev
    Legend = list_of_rows[row_number - 1][0]

with open('apis.csv', 'r') as hash_iid:
    csv_reader = csv.reader(hash_iid)
    list_of_rows = list(csv_reader)
    row_number = Legend_dev
    Dev = list_of_rows[row_number - 1][1]

api_id = int(Legend)
api_hash = str(Dev)
pphone = value

config = configparser.ConfigParser()
config.read("config.ini")
to_group = config['Legend_dev']['ToGroup']
messagessss = Message
legendfile = config['Legend_dev']['Message_file']

SLEEP_TIME_2 = 100
def autos():
    Legend_dev_message = messagessss
    channel_username = to_group
    phone = utils.parse_phone(pphone)
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    
    client.connect()
    if not client.is_user_authorized():
        print(Style.BRIGHT + Fore.RED + 'some thing has changed')
        client.send_code_request(phone)
        client.sign_in(phone, input    (Style.BRIGHT + Fore.GREEN + 'Enter the code: '))
    

    user = client.get_me()
    if not user.last_name:
        LegendName = user.first_name
    else:
        LegendName = user.first_name +' '+user.last_name
    input_file = 'data.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
            #user['access_hash'] = int(row[3])
            user['name'] = row[3]
            users.append(user)

    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 2
        numnext = list_of_rows[row_number - 1][col_number - 1]
    
    startfrom = int(numnext)
    nextstart = startfrom+50
    
    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 3
        numend = list_of_rows[row_number - 1][col_number - 1]
    
    endto = int(numend)
    nextend = endto+50
        
    with open("memory.csv","w",encoding='UTF-8') as df:
        writer = csv.writer(df, delimiter=",", lineterminator="\n")
        writer.writerow([nextLegend_dev,nextstart,nextend])

    rex = 0
    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                rex += 1
                status = 'Legend_dev'
                receiver = client.get_input_entity(user['username'])
                if user['username'] == "":
                    print("no username, moving to next")
                    continue

                if not legendfile:
                    client.send_message(receiver, f"Hi {user['name']}\n {Legend_dev_message}")
                else:
                    client.send_file(receiver, legendfile)
                    client.send_message(receiver, f"Hi {user['name']}\n {Legend_dev_message}")
                status = Style.BRIGHT + Fore.GREEN + 'DONE'


                time.sleep(random.randrange(3, 6))

            except UserPrivacyRestrictedError:
                status = 'PrivacyRestrictedError'


            except UserAlreadyParticipantError:
                status = 'ALREADY'


            except PeerFloodError as g:
                status = 'PeerFloodError :('
            except FloodWaitError as t:
                stime = t.seconds
                print(f"wait {stime} seconds")
                time.sleep(stime)
            except errors.RPCError as e:
                status = e.__class__.__name__

            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue
            print(Style.BRIGHT + Fore.GREEN +f" {LegendName} {Style.BRIGHT+Fore.RESET} > SENDING TO {Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status} >> {rex}")
        elif int(user['srno']) > int(endto):
            print(Style.BRIGHT + Fore.GREEN + "\nMessage Sended Successfully!\n")
            print(Style.BRIGHT + Fore.YELLOW + 'Press Enter To Exit')
            stat = input()
            if stat == 1 :
                autos()
            else:
                quit()
             
autos()