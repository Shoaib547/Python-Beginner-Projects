import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter a number between 1 and {x}: '))
        if guess < random_number:
            print("sorry. Guess gain. Too low")
        elif guess > random_number:
            print("sorry, guess again. Too high")
    print(
        f"Yayy. Congrats !!! You have Guessed the number {random_number} correctly.")


guess(10)