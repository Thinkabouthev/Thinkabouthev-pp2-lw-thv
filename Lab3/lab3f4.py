def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt = cnt + 1
    return cnt == 2 #it means num has only two factors (1 and itself)


mylist = map(int, input().split())
newlist = [x for x in mylist if isPrime(int(x))]
print(newlist)


#'mylist = map(int, input().split()) - This line takes input from the user, splits it into a list of strings using whitespace as a delimiter, and then converts each element of the list into an integer using the map() function.