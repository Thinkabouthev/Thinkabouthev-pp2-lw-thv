string = input()
low = list(filter(lambda x: x.isupper(), string))
up = list(filter(lambda x: x.islower(), string))
print(f"{len(low)} - lowercase letters\n{len(up)} - uppercase letters")


#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters