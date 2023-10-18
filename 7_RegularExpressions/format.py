#Lecture 7 - Regular Expressions

import re

name = input("Your name: ").strip()
# := assign value and ask the question with if
if matches := re.seabrch(r"^(.+), *(.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")
