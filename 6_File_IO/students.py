#Lecture 6 - File I/O

import csv

#Create file and append
# name = input("Your name: ")
# home = input("Your home: ")

# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})


#Read file
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append( {
            "name": row["name"],
            "home": row["home"]
        } )

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")