## 4. Write a Python program to check the validity of password input by users. Validation.


import random
hidden = random.randint(1,10)
users_guess = int(input("Guess a number between 1 and 9: "))
while users_guess != hidden:
    print("Guessed wrong, try again.")
    users_guess = int(input("Guess a number between 1 and 9: "))
    if users_guess == hidden:
        print("Well guessed!!")
        break