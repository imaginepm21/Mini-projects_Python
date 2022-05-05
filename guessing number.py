import random

def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < rand_num:
            print("The number you have entered is lesser than the actual number")
        elif guess > rand_num:
            print("The number you have entered is greater than the actual number")

    print(f"Congrats! You have guessed the number {rand_num}!")

guess(10)