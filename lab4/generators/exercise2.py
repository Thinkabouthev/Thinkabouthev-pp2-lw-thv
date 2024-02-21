def my_generator():
    n = int(input())
    for i in range(1,n+1):
        if i%2==0:
            yield i
    
list = []
for num in my_generator():
    if num not in list:
        list.append(num)

print(list)