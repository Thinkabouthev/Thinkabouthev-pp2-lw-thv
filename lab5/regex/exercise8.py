import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
    x = r"[A-Z]+"
    result = re.split(x, text)
    print(result)

#Write a Python program to split a string at uppercase letters.
#Напишите программу на Python для разделения строки на заглавные буквы.



