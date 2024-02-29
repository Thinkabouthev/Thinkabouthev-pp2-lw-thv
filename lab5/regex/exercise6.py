import re


with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  
    x = r"[\s,\.]"
    result = re.sub(x, ':', text)   
    print(result)

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
#Напишите программу на Python, чтобы заменить все вхождения пробела, запятой или точки двоеточием.
