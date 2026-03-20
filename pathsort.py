from pathlib import Path
from time import sleep

# === gets user input sanitieses and returns true or false ===
def consent(msg):
    while True:
        usrinpt = input(msg).strip().lower()
        if usrinpt in ('yes', 'y'):
            return True
        elif usrinpt in ('no', 'n'):
            return False
        else:
            print('invalid input')

# === files mapping ===
file_map = {
  ".png": "images",
  ".pdf": "documents",
  ".pptx": "ppt"
}

# ======= constants =======
cwd = Path.cwd()
avail_files=[]
avail_formats=[]

# === lists items -- lists file formats -- counts the numbers of  files ===
def listitems(count=0):
    for item in cwd.iterdir():
        print(item.name)
        sleep(.1)
        count+=1
        avail_files.append(item)
        if item.suffix and item.suffix not in avail_formats:
            avail_formats.append(item.suffix)

    print(f'total  number of items... {count}')
    print(f'formats file formats found... \n{avail_formats}')
    print(f'formats files found... \n{avail_files}')

# === makes directories ===
def mkdir():
        shalli=consent("""
        do you want to make the folllowing directories? y/n
        """)
        if shalli:
            for items in avail_formats:
                folder = file_map.get(items)
                if folder is not None:
                    Path(cwd/folder).mkdir(parents=True, exist_ok=True)


# === moves files to appropriate folders ===
def movefiles():
        shalli= consent('do you want to move files to appropriate folders? y/n \n')
        if shalli:
            for item in avail_files:
                if item.is_file():
                        folder = file_map.get(item.suffix)
                        if folder is not None:
                            des = cwd/folder/item.name
                            item.rename(des)
                        if folder is None:
                            print(f'file not identified \n=====\n{item}\n=====\n')
        elif not shalli:
            print('items will not be moved')



                
        
# === calling ===
print("initiating programme...")

print(f'Current working dir... {cwd}\n')

print("items in cwd...")
listitems()

mkdir()

movefiles()
