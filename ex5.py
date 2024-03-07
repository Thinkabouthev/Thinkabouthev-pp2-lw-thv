with open('test.txt', 'w') as text:
    list = [input() for _ in range(10)]
    
    for i in list:
        text.write(f'{i}\n')


'''with open('test.txt', 'a') as text:
    list = [input() for _ in range(10 ** 6)]
    
    for i in list:
        text.write(f'{i}\n')'''


#Write a Python program to write a list to a file.
