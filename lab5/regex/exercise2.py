import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

x = re.findall(r"ab{2,3}", text)  
print(x)

#x = re.findall(r"ab{2,3}?", text)  minor


#Write a Python program that matches a string that has an followed by two to three .'a''b'
#Напишите программу на Python, которая соответствует строке, за которой следует от двух до трех .'a"b'




