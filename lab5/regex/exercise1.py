import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

x = re.findall(r"ab*", text)  
print(x)


#Write a Python program that matches a string that has an followed by zero or more 'a''b'
#Напишите программу на Python, которая соответствует строке, за которой следует ноль или более 'a"b'
