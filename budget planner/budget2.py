import json
from pathlib import Path
from datetime import datetime
import inquirer

class Entries:
    def __init__(self, data):
        if not data == []:
            for item in data:
                print(item)
                



file = Path("budgetfile.json")
if file.is_file():
    with open(file, "r") as f:
        old_data = json.load(f)        
else:
    old_data = []
transactions = Entries(old_data)





# {'04/04/26 (09:57:01)': {'transtype': 'transfer', 'category': '-', 'amount': '2', 'account': 'bank/UPI => cash', 'comment': 'e'}}

# try:
    # data.append(entry)
# except:
    # data.update(entry)
# with open(file, "w") as f:
        # json.dump(data, f, indent=2)

# the main idea
# initiation -- create a file or find the file of interest
# feed the data to processor 
# 