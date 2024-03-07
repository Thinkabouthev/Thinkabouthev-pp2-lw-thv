import os

path = r'C:\Users\HUAWEI\Desktop\python\lab5'

with os.scandir(path) as it:
    print('dir:')
    for files in it:
        if files.is_dir():
            print(' ', files.name)
            
with os.scandir(path) as it:
    print('files: ')
    for files in it:
        if not files.is_dir():
            print(' ', files.name)

#Write a Python program to list only directories, files and all directories, files in a specified path.

