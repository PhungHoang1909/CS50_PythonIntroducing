# Lecture 0 - Functions, Variables

# To create a function 
# use keyword "def"
# function need to be definied before being called

def hello(name = "Mister/Miss"):
    print("Hello, " + name)

name = input("Your name: ")
hello(name)