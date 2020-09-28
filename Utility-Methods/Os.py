import os

osName = os.name  # nt = windows
print(osName)

# *********************************

currentFolder = os.getcwd()
print(currentFolder)

# *********************************

os.mkdir("newfolder")  # Create Folder
os.rename("newfolder", "newfolder-newname")  # Change Name
os.makedirs("newfolder1/innerfolder")  # Create Nested Folder
os.rmdir("newfolder-newname")  # Delete Folder without Nested Folder
os.removedirs("newfolder1/innerfolder")  # Delete Nested Folder

# *********************************

os.chdir('C:\\')  # change location
currentFolder = os.getcwd()
print(currentFolder)

# *********************************

list = os.listdir()
print(list)

# **********************************

for folder in os.listdir():
    if folder.endswith('.py'):  # display python folders
        print(folder)

# *********************************

from datetime import datetime

infos = os.stat("Python-Ornekleri")
print(infos)

result = infos.st_size / 1024
print(result)

result = datetime.fromtimestamp(infos.st_ctime)  # Creating date
print(result)
result = datetime.fromtimestamp(infos.st_atime)  # last accessed date
print(result)
result = datetime.fromtimestamp(infos.st_mtime)  # last modified date
print(result)

# *****************************************************************

os.system("notepad.exe")  # run notepad

# **********************************************************************

# PATH
print("\n")

result = os.path.abspath("Python-Ornekleri/iterators.py")
print(result)

result = os.path.dirname(os.path.abspath("Python-Ornekleri/iterators.py"))
print(result)

result = os.path.exists("Python-Ornekleri/iterators.py")
print(result)

result = os.path.isdir("C:/Users/furka/Desktop/Python-Ornekleri")
print(result)

result = os.path.isfile("C:/Users/furka/Desktop/Python-Ornekleri/os.py")
print(result)

result = os.path.join("C:\\", "deneme", "deneme1")
print(result)

result = os.path.split("C:\\deneme")
print(result)

result = os.path.splitext("os.py")
result = result[0]
print(result)
