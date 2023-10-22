"""
A Caculator with functions
"""

"""Import library to exit the program"""
import os

"""Display menu function"""
def menu():
    print("")
    print("")

    print("--- Caculator App ---")
    print("- Choose function: ")

    print("1. a + b")
    print("2. a - b")
    print("3. a * b")
    print("4. a / b")

    print("5. Exit")


# User input the function want to use.
def get_choice():
    while True:
        try:
            n = int(input("Choose function (1-5): "))
            if n >= 1 and n <= 5:
                break
            else:
                print("Invalid. Try again!")
        except ValueError:
            print("Invalid. Try again!")

    return n

# Get input to start caculating
def get_input():
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))

            break
        except ValueError:
            print("Invalid input. Try again!")

    return a, b

def functions(choice, a, b):
    match choice:
            case 1:
                print(f"{a} + {b} =", round(a + b, 2), end=" ")
                print("")

            case 2:
                print(f"{a} - {b} =", round(a - b, 2), end=" ")
                print("")

            case 3:
                print(f"{a} * {b} =", round(a * b, 2), end=" ")
            case 4:
                if b == 0:
                    print("Cannot divide by 0")
                else:
                    print(f"{a} / {b} =", round(a / b, 2), end=" ")
            case _:
                print("Loading...")

"""Main"""
def main():
    while(True):

        menu()

        choice = get_choice()

        # Exit program if function = 5
        if choice == 5:          
            os.system('cls')
            exit()

        # Input a and b to caculate
        a, b = get_input()

        # Functions 1 - 4
        functions(choice, a, b)
        

if __name__ == "__main__":
    main()
