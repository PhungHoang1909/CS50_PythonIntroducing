# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, 
#     in which case the first of the two should be -f or --font, 
#     and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or 
#     the second is not the name of a font, the program should exit via sys.exit 
#     with an error message.

import sys
import random
from pyfiglet import Figlet, FigletFont

def print_figlet():
    # Get the list of available fonts
    available_fonts = FigletFont.getFonts()

    # Check the command-line arguments
    if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        if font not in available_fonts:
            sys.exit(f"Error: '{font}' is not a valid font.")
    elif len(sys.argv) == 1:
        # Choose a random font if no font was specified
        font = random.choice(available_fonts)
    else:
        sys.exit("Error: Invalid command-line arguments.")

    # Prompt the user for a string of text
    text = input("Enter a string of text: ")

    # Create a Figlet object with the desired font
    f = Figlet(font=font)

    # Output the text in the desired font
    print(f.renderText(text))

print_figlet()
