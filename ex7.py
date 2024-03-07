with open('smthg.txt') as file:
    file_for_copy = file.read()
    
    file_to_copy = open('test.txt', 'w')
    file_to_copy.write(file_for_copy)
    
    file_to_copy.close()


#Write a Python program to copy the contents of a file to another file
