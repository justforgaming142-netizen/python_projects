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
    "check balance summaray",
    "monthly transactions",
    "catagory wise summary",
    )

# new entry list
# typelist 
type_list = ("transfer", "debit", "credit")
# catlist
cat_list = ("food", "bus")



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
        
def add_new_entry():
    transtype = question("transtype", "transfer debit or credit?", type_list)
    amount = questext("amount", "the amount")
    print(amount)
    if not transtype["transtype"] == "transfer":
        category = question("category", "choose category", cat_list)
        



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