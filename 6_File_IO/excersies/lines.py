# implement a program that expects exactly one command-line argument, 
# the name (or path) of a Python file, and outputs the number of lines of code in that file,
# excluding comments and blank lines. If the user does not specify exactly one command-line argument, 
# or if the specified file’s name does not end in .py, or if the specified file does not exist, 
# the program should instead exit via sys.exit.

# Assume that any line that starts with 
#, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

lines = []
count = 0

try:
    with open("debugging.py") as file:
        for line in file:
            stripped_line = line.lstrip()
            if stripped_line != "" and not stripped_line.startswith('#'):
                count += 1
    print(count)
except FileNotFoundError:
    print("File not found")
