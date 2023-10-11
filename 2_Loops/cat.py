#Lecture 2 - Loops

# While Loop:
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# For Loop: 
# for _ in range(3): #range(3): 0, 1, 2
#     print("meow")


# check n is valid:

# while True:
#     n = int(input("n's value: "))
#     if n > 0:
#         break

# for _ in range(n): # 0, 1, 2, .. n
#     print("meow")

#define a function:
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("n's value: "))
        if n > 0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("meow")

main()