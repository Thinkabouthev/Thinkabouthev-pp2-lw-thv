from functools import reduce

lst = [int(x) for x in input().split()]

res = reduce((lambda x, y: x * y), lst)

print("Result:", res)

#Write a Python program with builtin function to multiply all the numbers in a list