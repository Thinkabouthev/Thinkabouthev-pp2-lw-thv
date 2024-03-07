
import os

path = r'C:\Users\HUAWEI\Desktop\python\lab5'

print("Existence:", os.path.exists(path))
print("Read access:", os.access(path, os.R_OK))
print("Write access:", os.access(path, os.W_OK))
print("Execute access:", os.access(path, os.X_OK))



#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
