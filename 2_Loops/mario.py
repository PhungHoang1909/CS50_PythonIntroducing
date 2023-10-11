#Lecture 2 - Loops

def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

#Nested Loops:
def print_square(size):
    for i in range(size): #for each row 
        for j in range(size): #for each brick in row 
            print("#", end = "")
        print()

main()