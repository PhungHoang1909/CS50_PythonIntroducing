#Lecture 7 - Regular Expressions

import re

email = input("Your email: ").strip()

# . : any character except a new line 
# * : 0 or more repetitions
# + : 1 or more repetitions
# ? : 0 or 1 repetition
# {m}: m repetitions
# {m, n}: m-n repetitions

# ^ : matches the start of the string
# $ : matches the end of the string or just before the newline at the end 
# of the string

# [] : set of characters
# [^] : complementing the set

if re.search(r"^\w+@\w+\.(edu|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")