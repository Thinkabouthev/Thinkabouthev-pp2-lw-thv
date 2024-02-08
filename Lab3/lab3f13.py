import random
print('Hello! What is your name?')
name=input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

def guess_the_number():
    secret_num = random.randint(1, 21)
    cnt = 0
    while True:
        guess = int(input("Take a guess.\n"))
        if guess == secret_num:
            print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
            break
        else:   
            print('Your guess is too low.')
        
        if guess != secret_num:
            cnt = cnt +1

guess_the_number()