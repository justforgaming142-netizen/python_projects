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
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML

# cached constants
sum_total=0
main_menu = ["total Balance", "add an entry", "add an accounts", "delete/edit an entry"]

pstyle = Style.from_dict({
    ""             : "bg:#161310 #efe9df",   # default: input text on dark bg
    "prompt"       : "#d1a662 bold",          # the ">" or label part
    "title"        : "#efe9df bold",          # like your "Daniel S" heading
    "accent"       : "#d1a662",               # gold accents (pills, links)
    "muted"        : "#8a6d3f italic",        # subdued/secondary text
    "bottom-toolbar": "bg:#100e0c #d1a662",
    "completion-menu.completion"          : "bg:#100e0c #efe9df",
    "completion-menu.completion.current"  : "bg:#d1a662 #161310",
    "scrollbar.background"                : "bg:#161310",
    "scrollbar.button"                    : "bg:#8a6d3f",
})

print(
    HTML("<title>═══ Budget Tracker ═══</title>"),
    style=pstyle,   # the same Style object your session uses
)

data = {}

ss = PromptSession(
    style=pstyle,
    bottom_toolbar=lambda: HTML(
        "<accent>[budget-tracker]</accent> <muted>ctrl-c to quit · ctrl-d to save</muted>"
    ),
)


print(HTML("<muted>Current working directory is...</muted>"), style=pstyle)
print(HTML("<muted>Path().cwd()</muted>"), style=pstyle)


jfile=Path().joinpath(Path().cwd(), 'btracker.json')


if jfile not in Path().cwd().iterdir():
    print("--------", style=pstyle)
    print('item not found', style=pstyle)
    print('new item "btracker.json" will be created', style=pstyle)
    print("--------", style=pstyle)
else:
    print("--------", style=pstyle)
    print('item found', style=pstyle)
    print('item will be updated', style=pstyle)
    print("--------", style=pstyle)
    with open(jfile, "r") as file:
        data = json.load(file)


for option in main_menu:
    print(option, style=pstyle)
label = 'hello world'
ss.prompt(HTML(f"<prompt>{label} ›</prompt> "),  completer=WordCompleter(main_menu), complete_while_typing=True)

usrr = ss.prompt(message="What to you want to do?", completer=WordCompleter(main_menu), complete_while_typing=True) 

if usrr == 'total Balance':
    sum_total=0
    for items in data["entries"]:
        if items['type']== 'credit':
            sum_total = sum_total - int(items["amount"])
        elif items['type']== 'debit':
            sum_total = sum_total + int(items["amount"])
    print('The total balance is', style=pstyle)
    print(f'=== {sum_total} ===', style=pstyle)
elif usrr == "add an entry":
    temp_data = {}
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    tran_type = ss.prompt(message='credit or debit?')
    amount = ss.prompt(message='how much?')
    temp_data.update({"date": current_time, "type": tran_type, "amount": amount})
    print(temp_data, style=pstyle)
    cons = ss.prompt(message='confirms?')
    if cons == 'y':
        data['entries'].append(temp_data)
    json_str = json.dumps(data, indent=4)
    with open(jfile, "w") as file:
         file.write(json_str)