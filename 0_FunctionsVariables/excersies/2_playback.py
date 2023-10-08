# In a file called playback.py, implement a program in Python 
# that prompts the user for input and then outputs that same input, 
# replacing each space with ... (i.e., three periods).

str2 = input("Input your string: ")
str2 = "...".join(str2.split())

print(str2)