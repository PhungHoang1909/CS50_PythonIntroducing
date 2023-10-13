# In a file called professor.py, implement a program that:

# Prompts the user for a level,
# . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
#  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.

import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            pass
        else:
            break
    return level


def generate_integer(level):
    score = 0
    for _ in range(10):
        # Generate two non-negative integers with 'level' digits
        x = random.randint(10 ** (level - 1), 10**level - 1)
        y = random.randint(10 ** (level - 1), 10**level - 1)

        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    print("Correct!")
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")

        else:  # This block executes if the 'for' loop completes normally (i.e., no 'break')
            print(f"The correct answer is {x + y}.")

    print(f"Your score: {score}/10")


if __name__ == "__main__":
    main()
