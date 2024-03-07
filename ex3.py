import os

path = r'C:\Users\HUAWEI\Desktop\python\lab4'

if os.path.exists(path):
    print("Path exists:")
    
    for filename in os.listdir(path):
        print(filename)
else:
    print("Path does not exist")


#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
