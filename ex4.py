import os

path = r'C:\Users\HUAWEI\Desktop\python\lab6\dir-and-files\smthg.txt'

with open(path, 'r') as a:  
    lines = a.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))

    #Write a Python program to count the number of lines in a text file.
