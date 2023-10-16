#Lecture 6 - File I/O

# # Create and write file
# name = input("Your name: ")

# #Store names in names.txt
# with open("names.txt", "a") as file:
# #w: write #a: append
# #Write that name to the file txt
#     file.write(f"{name}\n")

# # file.close()



#Read from file 
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=False):
    print(f"Hello, {name}")