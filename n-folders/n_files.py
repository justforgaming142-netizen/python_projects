from pathlib import Path

num_fold = input('give a number')
nam_fold = input("name the folder")

for i in range(int(num_fold)):
    folder = nam_fold+str(i)
    Path(Path.cwd()/folder).mkdir(parents=True, exist_ok=True)

