# In a file called adieu.py, implement a program that prompts the user for names, 
# one per line, until the user inputs control-d. 
# Assume that the user will input at least one name. Then bid adieu to those names, 
# separating two names with one and, three names with two commas and one and, and names with 
#  commas and one and, as in the below:

def bid_adieu():
    names = []
    while True:
        try:
            name = input("Enter a name (or Ctrl-D to finish): ")
            names.append(name)
        except EOFError:  # User pressed Ctrl-D
            break

    # Format the farewell message
    if len(names) == 1:
        farewell = f"Adieu, adieu, to {names[0]}"
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

    print(farewell)

bid_adieu()
