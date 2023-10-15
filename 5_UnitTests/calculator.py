#Lecture 5 - Unit Tests

def main():
    x = input("x's value: ")
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

if __name__ == "__main__":
    main()