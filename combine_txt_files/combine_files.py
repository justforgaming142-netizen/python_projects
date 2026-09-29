from pathlib import Path

txt_files = {".md", ".txt"}
cons = ''
write_file = "consolidated file.md"
for item in Path().iterdir():
    if Path(item).suffix in txt_files:
        with open(item, "r") as content:
            cons = cons + f"\n=====\n{item.name} begins \n====== \n"
            cons = cons + content.read()
            cons = cons + f"\n=====\n{item.name} ends \n====== \n"

# if write_file in lamda(name: for i in Path().iterdir() i.name) :
with open( write_file, "w") as wfile:
    wfile.write(cons)
