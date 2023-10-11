# In a file called camel.py, implement a program that 
# prompts the user for the name of a variable 
# in camel case and 
# outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.


def main():
    camel_case = input("Type Camel case: ")
    print("Snake case: ")
    print(camel_to_snake(camel_case))

def camel_to_snake(s):
    snake_case = ""
    for c in s:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    return snake_case
            

main()