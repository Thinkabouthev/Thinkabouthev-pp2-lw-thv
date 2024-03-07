def determine():
    test = input("Enter word: ")
    rev_test = ''.join(reversed(test))
    print('The word "{}" is {}a palindrome'.format(test, '' if rev_test == test else 'not '))

determine()

#Write a Python program with builtin function that checks whether a passed string is palindrome or not.