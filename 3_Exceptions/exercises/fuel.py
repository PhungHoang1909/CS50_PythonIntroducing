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

def fuel_percent():
    while True:
        try:
            #take input x/y
            fract = input("Fraction: ")

            #split x / y and caculate the result
            x, d, y = list(fract)
            x = float(x)
            y = float(y)
            result = round((x / y) * 100)

            if x > y or y == 0:
                continue
            if (result <= 1):
                return "E"
            elif (result >= 99):
                return "F"
            else:
                return f"{result}%"

        except (ValueError, ZeroDivisionError):
            continue

print(fuel_percent())