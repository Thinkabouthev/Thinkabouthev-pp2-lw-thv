import time, math

num, miliseconds = int(input()), int(input())
time.sleep(miliseconds / 1000)

print(f'Square root of {num} after 2123 miliseconds is {math.sqrt(num)}')


#Write a Python program that invoke square root function after specific milliseconds.
'''Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858'''


'''from time import sleep
sleep(miliseconds / 1000)
'''