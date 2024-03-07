import os

path = r'C:\Users\HUAWEI\Desktop\python\lab6\dir-and-files\ForDeleting.txt'

if os.access(path, mode=os.EX_OK):
    os.remove(path)


#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.