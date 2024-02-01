#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}


#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#{False, True, 'cherry', 'apple', 'banana'}


#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)