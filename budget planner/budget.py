import json
from pathlib import Path
from datetime import datetime
import inquirer

date = datetime.now()
formatted_month = date.strftime("%B")
print(formatted_month)
print(date)


# listes of all kinds
# main menu list
main_menu_list =(
    "add new entry",
    "list",
    "check balance summaray",
    "monthly transactions",
    "catagory wise summary",
    "add new..."
    )

# new entry list
# typelist 
type_list = ["transfer", "debit", "credit"]
# catlist
cat_list = ["food", "bus"]
#account list
acc_list = ["bank/UPI", "cash"]
#from to acc
acc_t_list = []
for i in range(0, len(acc_list)):
    for j in range(0, len(acc_list)):
        if not i == j:
            acc_t_list.append(f'{acc_list[i]} => {acc_list[j]}')

# the question template
def question(key, msg, choices):
    ques =[ inquirer.List(key,
                    msg,
                    choices,),]
    ans=inquirer.prompt(ques)
    return ans

def questext(key, msg):
    ques =[ inquirer.Text(key,
                     message=msg,
                     validate=lambda _, x: x.strip())]
    ans=inquirer.prompt(ques)
    return ans


# main menu that uses the question template
def main_menu():
    action =question("menu_choise","What would you like to do?", main_menu_list)
    print(f"you have chosen {action["menu_choise"]}")
    if action["menu_choise"] == "check balance summaray":
        balanceact()
    elif action["menu_choise"] == "monthly transactions":
        mon_sum()
    elif action["menu_choise"] == "catagory wise summary":
        cat_sum()
    elif action["menu_choise"] == "add new entry":
        add_new_entry()
    elif action["menu_choise"] == "list":
        listitems()
        
def add_new_entry():
    #1 TYPE
    transtype = question("transtype", "transfer debit or credit?", type_list)
    #2 AMOUNT
    amount = questext("amount", "the amount")
    #3 CAREGORY        
    if not transtype["transtype"] == "transfer":
        category = question("category", "choose category", cat_list)
    else:
        category = {"category":"-"}
    #4 ACCOUNT
    if not transtype["transtype"] == "transfer":
        account = question("account", "account?", acc_list)
    else:
        account =  question("account", "from where to where?", acc_t_list)
    #5 COMMENT
    comment = questext("comment", "Add comment")
    #updating the entry to a dict
    entry = {**transtype, **category, **amount, **account, **comment}
    print(entry)
    with open("budgetfile.json", mode="w", encoding="utf-8") as file:
            json.dump(entry, file)
    return entry

# check for existing json file
def readwrite ():
    cwd = Path.cwd()
    file = Path(cwd/"budgetfile.json")
    if file.is_file():
        print('file found')
        print(file)
        print(datetime.now())
        

    else:
        print("no relevent file found \n creating new json file")
        
readwrite()
main_menu()
# get info
# store info
# write info

        
        


# data format/template
# template = [
#  {
#    "TIME": "Mar 15, 2026 8:19 PM",
#    "typeof": "(*) Transfer",
#    "AMOUNT": 1200,
#    "CATEGORY": "  -  ",
#    "ACCOUNT": "Bank/UPI->papa",
#    "NOTES": ""
#  }
# ]