#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #true

#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'

#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}