def my_generator(a,b):
    for i in range(a, b+1):
         yield i*i
a = int(input())
b = int(input())
for num in my_generator(a,b):
    for i in range(a, b+1):
        if num == i*i:
            print(num)
