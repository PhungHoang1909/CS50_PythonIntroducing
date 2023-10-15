# All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the plate starts with at least two letters
    if not s[:2].isalpha():
        return False

    # Check if the plate contains between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if numbers are used only at the end and the first number is not '0'
    if any(char.isdigit() for char in s[2:]):
        if s[2] == '0' or any(char.isalpha() for char in s[3:]):
            return False
        
    # Check if there are any periods, spaces, or punctuation marks
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()