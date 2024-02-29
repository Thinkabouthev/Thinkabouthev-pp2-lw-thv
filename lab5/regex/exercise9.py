import re

with open('dariya.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    x = r"([A-Z])"
    result = re.sub(x, r" \1", text).strip()

    print(result)









#Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.
#Write a Python program to insert spaces between words starting with capital letters.

