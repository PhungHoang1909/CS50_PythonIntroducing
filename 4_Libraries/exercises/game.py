# In a file called game.py, implement a program that:

# Prompts the user for a level. If the user does not input a positive integer,
# the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer.
# If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

import random

# Input level
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        break

# Get random number
rand_num = random.randint(1, level)

# Guess game:
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
        elif rand_num < guess:
            print("Smaller")
        elif rand_num > guess:
            print("Bigger")
        else:
            print("You got it !!!")
            break
    except ValueError:
        pass
