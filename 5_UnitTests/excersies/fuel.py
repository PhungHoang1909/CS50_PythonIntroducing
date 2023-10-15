# In a file called fuel.py, 
# implement a program that prompts the user for a fraction, formatted as X/Y, 
# wherein each of X and Y is an integer, and then outputs, 
# as a percentage rounded to the nearest integer, 
# how much fuel is in the tank. If, though, 
# 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
# (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    fract = input("Fraction: ")
    percent = convert(fract)
    result = print(gauge(percent))
    return result


def convert(fraction):

    try:
        x, d, y = list(fraction)
        x = int(x)
        y = int(y)

        if isinstance(x, int) == False or isinstance(y, int) == False:
            raise ValueError
        
        if x > y:
            raise ValueError
        
        if y == 0:
            raise ZeroDivisionError

        percent = round((x / y) * 100)
        return percent

    except (ValueError):
        print("ValueEroor. Check x or y again!")

    except (ZeroDivisionError):
        print("Cannot divided by 0!")



def gauge(percentage):
    if (percentage <= 1):
        return "E"
    elif (percentage >= 99):
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()