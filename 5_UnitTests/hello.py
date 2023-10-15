#Lecture 5 - Unit Tests

def main():
    name = input("Your name: ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()