import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

x = re.search(r"[a-z]+_+[a-z]*", text)  
if x:
    print("Match found:", x.group())
else:
    print("No match found")
#Write a Python program to find sequences of lowercase letters joined with a underscore.
#Напишите программу на Python для поиска последовательностей строчных букв, соединенных символом подчеркивания.



'''import re


with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

x = re.findall(r"[a-z]+_+[a-z]", text)  
print(x)
'''


