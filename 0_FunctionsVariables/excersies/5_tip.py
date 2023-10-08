def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# dollars_to_float, which should accept a str as 
# input (formatted as $##.##, wherein each # is a decimal digit), 
# remove the leading $, and return the amount as a float. For instance, 
# given $50.00 as input, it should return 50.0
def dollars_to_float(d):
    d = d.lstrip(d[0])
    d = float(d)
    return d


def percent_to_float(p):
    p = p.rstrip(p[-1])
    p = float(p)
    return p/100


main()