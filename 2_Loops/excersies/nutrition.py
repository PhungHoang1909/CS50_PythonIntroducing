# In a file called nutrition.py, implement a program that prompts consumers 
# users to input a fruit (case-insensitively) and then outputs the number of calories 
# in one portion of that fruit, per the FDA’s poster for fruits, 
# which is also available as text. Capitalization aside, 
# assume that users will input fruits exactly as written in the poster 
# (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

fruits = [
    {"name" : "Apple", "calories" : "130"},
    {"name" : "Avocado", "calories" : "50"},
    {"name" : "Sweet Cherries", "calories" : "100"}
]

item = input("Item: ")
for fruit in fruits:
    if item == fruit["name"]: 
        print("Calories:", fruit["calories"])