from pathlib import Path

cwd=Path.cwd()

it_to_mv = input("Move items with... ")
mv_it_to = input("to folder...")

items = []

for i in cwd.iterdir():
    if it_to_mv in i.name:
        items.append(i)

print(items)
confirm = input(f"move the above items to {mv_it_to}? y/n").strip().lower()

if confirm == "n" or confirm == "":
    None
elif confirm == "y":
    for i in items:
        dest = Path(f"{cwd}/{mv_it_to}/{i.name}")
        dest.parent.mkdir(exist_ok=True)
        i.replace(dest)
