import re


with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

x = re.findall(r"a.*b$", text)  
print(x)

#Write a Python program that matches a string that has an followed by anything, ending in .'a''b'
#Напишите программу на Python, которая соответствует строке, за которой следует что-либо, заканчивающееся на .'a"b"


