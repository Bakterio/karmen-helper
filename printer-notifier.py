import requests
from os import system
from time import sleep
from beautifultable import BeautifulTable
from datetime import datetime

def get_token() -> str:
    config_file = open('token.txt', 'r')
    return config_file.readline().strip()

TOKEN = get_token()
log = open('/home/bakterio/Programming/karmen-helper/log.txt', 'w')
def print(text):
    log.write(str(text) + '\n')
    log.flush()

def get_data(printer, attempt: int):
    try:
        printer_data = requests.get(f"https://preprod1.next.karmen.tech/api/2/printers/{printer['id']}/?fields=client", headers= {"Authorization": f"Token {TOKEN}"}).json()
        octoprint_data = printer_data['client']['octoprint']
        octoprint_printer_data = octoprint_data['printer']['state']
        return octoprint_printer_data
    except KeyError:
        if attempt == 10:
            return None
        sleep(0.1) 
        return get_data(printer, attempt+1)

def notify_send(text: str):
    print(text)
    system(f"notify-send '{text}' -a 'Printer notifer' -i dialog-information")
    system(f"espeak '{text}'")

# Fetching data
r = requests.get("https://backend.next.karmen.tech/api/2/users/me/groups/", headers= {"Authorization": f"Token {TOKEN}"})
if r.status_code != 200:
    print('Falied connecting to Karmen servers')
    exit(1)
notify_send('Connected to Karmen servers')
GROUP_ID = r.json()[0]['id']
PRINTERS = requests.get(f"https://backend.next.karmen.tech/api/2/groups/{GROUP_ID}/printers/", headers= {"Authorization": f"Token {TOKEN}"}).json()

# Getting info from jsons & printing table with data
last_data = {}
table = BeautifulTable()
table.columns.header = [str(datetime.now()), 'Status', 'Is printing?']
for printer in PRINTERS:
    printer_data = get_data(printer, 1)
    if printer_data == None:
        table.rows.append([printer['name'], 'No data', None])
        continue
    last_data.update({printer['id']: printer_data['flags']['printing']})
    table.rows.append([printer['name'], printer_data['text'], printer_data['flags']['printing']])
print(table)


# last_data = {'aw84jyap': 0} # for testing, setting Bořislavka to not be printing
# Main loop
while True:
    sleep(1)
    table = BeautifulTable()
    table.columns.header = [str(datetime.now()), 'Status', 'Is printing?']
    for printer in PRINTERS:
        printer_data = get_data(printer, 1)
        if printer_data == None:
            table.rows.append([printer['name'], 'No data', None])
            continue
        is_printing = printer_data['flags']['printing']
        try:
            if is_printing != last_data[printer['id']]:
                print('Change!!!')
                message = 'started printing' if is_printing else 'stoped printing'
                notify_send(f"{printer['name']} {message}")
        except KeyError:
            pass
        last_data.update({printer['id']: is_printing})
        table.rows.append([printer['name'], printer_data['text'], is_printing])
    print(table)
