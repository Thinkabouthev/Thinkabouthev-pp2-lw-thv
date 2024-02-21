def my_generator(n):
    for i in range(n, -1, -1):
        yield i

n=int(input())
for num in my_generator(n):
    print(num, end = " ")