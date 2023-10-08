# Lecture 0 - Functions, Variables
    
def main():
    x = int(input("Value of x: "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()