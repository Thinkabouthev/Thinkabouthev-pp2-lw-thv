import re


with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

x = re.findall(r"[A-Z][a-z]+", text)  
print(x)


#r"[ ]+[A-Z][a-z]+"    пробел только потом слово

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
#Напишите программу на Python для поиска последовательностей из одной заглавной буквы, за которой следуют строчные буквы.

