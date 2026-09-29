from pathlib import Path

print(Path.cwd())

todel = input('delete files with the string… ')

print('These items will be deleted')
def delfile():
    for item in Path.cwd().iterdir():
        if todel in item.name:
            print(item.name)
    yn = input('proceed?… y/n').strip().lower()
    if yn == "y":
        for item in Path.cwd().iterdir():
            if todel in item.name:
                item.unlink()
    elif yn == 'n':
        print('process canceled')
    else:
        print('input error')

delfile()
    