import requests
from os import system

# Fetching data
TOKEN = "xD0BVO6Z2UhG79HPLtF0QNS4k9PyixjA33fxQsZNthA" # obviously not working token
r = requests.get("https://backend.next.karmen.tech/api/2/users/me/groups/", headers= {"Authorization": f"Token {TOKEN}"})
if r.status_code != 200:
    print('Falied connecting to Karmen servers')
    exit(1)
print('Connected to Karmen servers')
GROUP_ID = r.json()[0]['id']
total_pages = int(int(requests.get(f"https://backend.next.karmen.tech/api/2/groups/{GROUP_ID}/files/", headers= {"Authorization": f"Token {TOKEN}"}).json()['count'])/20+1)
files = []
print('Fetching data from karmen servers...')
for page_number in range(1, total_pages+1):
    r = requests.get(f"https://backend.next.karmen.tech/api/2/groups/{GROUP_ID}/files/?page={page_number}", headers= {"Authorization": f"Token {TOKEN}"})
    print(str((page_number/total_pages)*100) + "%")
    files += r.json()['results']
files.reverse()
print('Data fatched')

print(files[2]['name'])
print(files[2]['name'].lower().find('holder'))

# Searching in data
word = input('Search: ').lower()
s_files = []
for file in files:
    if file['name'].lower().find(word) == -1 and file['note'].lower().find(word) == -1:
        continue
    print("Found!!!")
    s_files.append(file)
    print(file['id'])
    system(f"xdg-open https://next.karmen.tech/gcodes/{file['id']}")
    exit(0)

# Printing searched files
for file, i in zip(s_files, range(1, len(s_files))):
    print(f"{i}. - {file['name']} [{file['id']}]")
