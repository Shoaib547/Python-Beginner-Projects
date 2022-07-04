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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'is {guess} too high (h), too low (l) or correct (c)')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print("Yay, the computer guessed the number correctly")
