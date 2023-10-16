# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import csv

# Read before.csv:

print("Before: ")

students = []

with open("before.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "name": row["name"],
            "house": row["house"]
        })

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# Create a new File and create first name last name and house

print("After: check file after.csv")

new_students = []

# split name to first name and last name
for student in students:
    first, last = student['name'].split(", ")
    new_students.append({
        "first": first,
        "last": last,
        "house": student["house"]
    })

# Write the new data to after.csv
with open("after.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    for student in new_students:
        writer.writerow(student)

