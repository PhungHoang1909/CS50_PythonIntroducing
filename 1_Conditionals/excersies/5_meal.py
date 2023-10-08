# Suppose that you’re in a country where it’s customary to 
# eat breakfast between 7:00 and 8:00, 
# lunch between 12:00 and 13:00, and 
# dinner between 18:00 and 19:00. 
# Wouldn’t it be nice if you had a program that could tell you what to eat when?


def main():
    time = input("What's time is it? ")
    convert(time)


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)
    
    if (hours == 7 or (hours == 8 and minutes == 00)):
        print("breakfast time")
    elif (hours == 12 or (hours == 13 and minutes == 00)):
        print("lunch time")
    elif (hours == 18 or (hours == 19 and minutes == 00)):
        print("dinner time")
    else:
        print("Not the time for eating")


main()