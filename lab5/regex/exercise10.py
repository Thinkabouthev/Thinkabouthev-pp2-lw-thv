import re

with open('dariya.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    x = r"([A-Z])"
    snake_case_text = re.sub(x, r"_\1", text).lower()  
    print(snake_case_text.lstrip('_'))  











#Write a Python program to convert a given camel case string to snake case.
#Напишите программу на Python для преобразования заданной строки регистра camel в регистр snake.