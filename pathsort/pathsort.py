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
    # images
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
    ".webp": "images",
    ".heic": "images",

    # documents
    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",
    ".txt": "documents",
    ".rtf": "documents",
    ".odt": "documents",

    # presentations
    ".ppt": "ppt",
    ".pptx": "ppt",
    ".odp": "ppt",

    # spreadsheets
    ".xls": "spreadsheets",
    ".xlsx": "spreadsheets",
    ".csv": "spreadsheets",
    ".ods": "spreadsheets",

    # audio
    ".mp3": "audio",
    ".wav": "audio",
    ".m4a": "audio",
    ".aac": "audio",
    ".ogg": "audio",

    # video
    ".mp4": "videos",
    ".mkv": "videos",
    ".avi": "videos",
    ".mov": "videos",
    ".webm": "videos",
    ".3gp": "videos",

    # archives
    ".zip": "archives",
    ".rar": "archives",
    ".7z": "archives",
    ".tar": "archives",
    ".gz": "archives",

    # apps / packages (mobile downloads often include these)
    ".apk": "apps",
    ".xapk": "apps",

    # misc
    ".json": "code",
    ".xml": "code",
    ".html": "code",
    ".css": "code",
    ".js": "code"
}

# ======= constants =======
cwd = Path.cwd()
avail_files=[]
avail_formats=[]

# === lists items -- lists file formats -- counts the numbers of  files ===
def listitems(count=0):
    for item in cwd.iterdir():
        print(item.name)
        count+=1
        avail_files.append(item)
        if item.suffix and item.suffix not in avail_formats:
            avail_formats.append(item.suffix)

    print(f'total  number of items... {count}')
    print(f'formats file formats found... \n{avail_formats}')

# === makes directories ===
def mkdir():
        for items in avail_formats:
            folder = file_map.get(items)
            if folder is not None:
                Path(cwd/folder).mkdir(parents=True, exist_ok=True)


# === moves files to appropriate folders ===
def movefiles():
        for item in avail_files:
            if item.is_file():
                folder = file_map.get(item.suffix)
                if folder is not None:
                    des = cwd/folder/item.name
                    item.rename(des)
                if folder is None:
                    print(f'file not identified \n=====\n{item}\n=====\n')



                
        
# === calling ===
print("initiating programme...")

print(f'Current working dir... {cwd}\n')

print("items in cwd...")
listitems()

mkdir()

movefiles()
