# In a file called pizza.py, 
# implement a program that expects exactly one command-line argument, 
# the name (or path) of a CSV file in Pinocchio’s format, 
# and outputs a table formatted as ASCII art using tabulate, 
# a package on PyPI at pypi.org/project/tabulate. 
# Format the table using the library’s grid format. 
# If the user does not specify exactly one command-line argument, 
# or if the specified file’s name does not end in .csv, or if the specified file does not exist, 
# the program should instead exit via sys.exit.

import csv, tabulate

pizzas = []

with open("sicilian.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pizzas.append({
            "Sicilian Pizza": row["Sicilian Pizza"],
            "Small": row["Small"],
            "Large": row["Large"]
        })


print (tabulate.tabulate(pizzas, tablefmt="grid", headers="keys"))