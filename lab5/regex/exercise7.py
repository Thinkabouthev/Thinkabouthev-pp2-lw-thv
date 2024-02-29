import re

def snake_to_camel(snake_case_string):
    return ''.join(word.capitalize() for word in snake_case_string.split('_'))

text = input()

pattern = r"\w+"
result = re.finditer(pattern, text)

for match in result:
    snake_case_string = match.group()  
    camel_case_string = snake_to_camel(snake_case_string)  
    print(camel_case_string)


#Write a python program to convert snake case string to camel case string.
#Напишите программу на python для преобразования строки регистра snake в строку регистра camel.



'''Snake case — стиль написания составных слов, при котором несколько слов разделяются символом подчеркивания (_), 
и не имеют пробелов в записи, причём каждое слово обычно пишется с маленькой буквы — «foo_bar», «hello_world» и т. д.
CamelCase - стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово
внутри фразы пишется с прописной буквы. Стиль получил название CamelCase, поскольку прописные буквы внутри слова напоминают горбы верблюда (англ. Camel)
NerdCaps
PascalCase
PolyCaps
WordCase
WordMixing'''

'''
some_variable
_count_variable
sum_of_column
i_love_PYTHON
'''