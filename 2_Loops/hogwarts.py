#Lecture 2 - Loops

#list: []
# students = ["Harry", "Ron", "Hermione", "Draco"]

# # len: n of list 
# for i in range(len(students)):
#     print(i + 1, students[i])


# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Dictionary: {}
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

#key: name, house, patronus
#values: Hermione, Gryffindor, Otter

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ', ')