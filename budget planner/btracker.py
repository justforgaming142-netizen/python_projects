# general idea
# find json file in folder or create on.
    # if file = read data 
# ask what user wants to do
# if new entery
    # get data from user and dump to file
# if summary operate on the data and give out put. or say  file empty.

# json file should have a simple config where the accounts exist.

import json
from pathlib import Path
import time
# cached constants
sum_total=0
main_menu = ["Total Balance", "add an entry", "add an accounts", "delete/edit an entry"]


data = {}

print("Current working directory is...")
print(Path().cwd())


jfile=Path().joinpath(Path().cwd(), 'btracker.json')


if jfile not in Path().cwd().iterdir():
    print("--------")
    print('item not found')
    print('new item "btracker.json" will be created')
    print("--------")
else:
    print("--------")
    print('item found')
    print('item will be updated')
    print("--------")
    with open(jfile, "r") as file:
        data = json.load(file)

print(data)

for option in main_menu:
    print(option)

usr = input("what to do...?")

usrr = main_menu[int(usr)-1]

if usrr == 'Total Balance':
    for items in data["entries"]:
        if items['type']== 'paid':
            sum_total = sum_total - int(items["amount"])
        elif items['type']== 'debited':
            sum_total =+ int(items["amount"])
    print('The total balance is')
    print(f'=== {sum_total} ===')
elif usrr == "add an entry":
    temp_data = {}
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    tran_type = input('credit or debit?…')
    amount = input('how much?')
    temp_data.update({"date": current_time, "type": tran_type, "amount": amount})
    print(temp_data)
    cons = input("confirm the following data?")
    if cons == 'y':
        data['entries'].append(temp_data)
    json_str = json.dumps(data, indent=4)
    with open(jfile, "w") as file:
         file.write(json_str)