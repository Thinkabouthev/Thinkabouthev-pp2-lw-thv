print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

#Print a message based on whether the condition is True or False:

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Evaluate a string and a number:

print(bool("Hello")) #true
print(bool(15)) #true


#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x)) #true
print(bool(y)) #true


#The following will return True:
#true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Print the answer of a function:
def myFunction() :
  return True

print(myFunction()) #true