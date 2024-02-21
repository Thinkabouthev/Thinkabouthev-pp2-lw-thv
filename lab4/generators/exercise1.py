def my_generator():
    n = int(input())
    for i in range(1,n+1):
        yield i*i

list = []
for num in my_generator():
    if num not in list:
        list.append(num)

print(list)