# In a file called indoor.py, implement a program in Python that 
# prompts the user for input and then outputs that same input in lowercase. 
# Punctuation and whitespace should be outputted unchanged. Y
# ou’re welcome, but not required, to prompt the user explicitly, 
# as by passing a str of your own as an argument to input.

str1 = input("Input: ")
str1 = str1.casefold()
print(str1)