# In a file called numb3rs.py, implement a function called validate 
# that expects an IPv4 address as input as a str and then returns True or False, 
# respectively, if that input is a valid IPv4 address or not.

#.#.#.#. But each # should be a number between 0 and 255, inclusive. 
# Suffice it to say 275 is not in that range! 
# If only NUMB3RS had validated the address in that scene

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return(f"True")
    else:
        return(f"False")


if __name__ == "__main__":
    main()