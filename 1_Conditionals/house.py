# Lecture 1 - Conditionals

# Match: Same with Switch
name = input("Your name: ")

# switch (name) == match name:
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #default: == case_:
        print("Who?")
