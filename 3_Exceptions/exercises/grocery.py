# In a file called grocery.py, 
# implement a program that prompts the user for items, one per line, 
# until the user inputs control-d (which is a common way of ending one’s input to a program). '
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
# prefixing each line with the number of times the user inputted that item. 
# No need to pluralize the items. Treat the user’s input case-insensitively.

def grocery_list():
    items = []
    while True:
        try:
            item = input("Enter an item (or Ctrl-D to finish): ")
            items.append(item.lower())
        except EOFError:  # User pressed Ctrl-D
            break

    # Count the occurrences of each item
    item_counts = {
        item: items.count(item) for item in set(items)
    }

    # Sort the items alphabetically
    sorted_items = sorted(item_counts.items())

    # Print the grocery list
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

grocery_list()