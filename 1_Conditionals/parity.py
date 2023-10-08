# Lecture 1 - Conditionals

def main():
    x = int(input("X value: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()