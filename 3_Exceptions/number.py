#Lecture 3 - Exceptions

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("x's value: "))
        except ValueError:
            # print("x is not an integer")
            pass
        else:
            break
    return x

main()