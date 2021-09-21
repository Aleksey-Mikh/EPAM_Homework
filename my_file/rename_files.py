import os
files = os.listdir()
for file in files:
    os.rename(file, file[:-3].replace(".", "_") + ".py")