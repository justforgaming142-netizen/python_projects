import json
from pathlib import Path
from datetime import datetime
import inquirer

date = datetime.now()
dt = datetime.now().strftime("%d/%m/%y (%H:%M:%S)")
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
cat_list_cre = ["food", "bus"]
cat_list_deb = ["Salary", "Borrowed"]
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

def quesint(key, msg):
    ques =[ inquirer.Text(key,
                     message=msg,
                     validate=lambda _, x: x.isdigit())]
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
    amount = quesint("amount", "the amount")
    #3 CAREGORY        
    if transtype["transtype"] == "transfer":
        category = {"category":"-"}
    elif transtype["transtype"] == "debit":
        category = question("category", "choose category", cat_list_deb)
    elif transtype["transtype"] == "credit":
        category = question("category", "choose category", cat_list_cre)

    #4 ACCOUNT
    if transtype["transtype"] == "transfer":
        account =  question("account", "from where to where?", acc_t_list)
    else:
        account = question("account", "account?", acc_list)
    #5 COMMENT
    comment = questext("comment", "Add comment")
    #updating the entry to a dict
    value = {**transtype, **category, **amount, **account, **comment}
    entry = {dt:value}
    print(entry)

    # append to the file
    file = Path("budgetfile.json")
    if file.is_file():
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []
    try:
        data.append(entry)
    except:
        data.update(entry)


    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def balanceact():
    file = Path("budgetfile.json")
    if file.is_file():
        total_balance = 0
        total_income = 0
        total_expense = 0
        with open(file, "r") as f:
            data = json.load(f)
        for item in data:
            value = next(iter(item.values()))
            print(value)
            if value["transtype"] == "credit":
                total_expense = total_expense+int(value["amount"])
                total_balance = total_balance-int(value["amount"])
            if value["transtype"] == "debit":
                total_income = total_income+int(value["amount"])
                total_balance = total_balance+int(value["amount"])
                
        print(f'total income = {total_income}')
        print(f'total expenses = {total_expense}')
        print(f'total balance = {total_balance}')
    else:
        print("there are no valide entries")


main_menu()


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