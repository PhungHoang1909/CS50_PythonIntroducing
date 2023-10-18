# In a file called working.py,
# implement a function called convert that expects a str in either of the 12-hour formats
# below and returns the corresponding str in 24-hour format
# (i.e., 9:00 to 17:00).
# Expect that AM and PM will be capitalized (with no periods therein)
# and that there will be a space before each.
# Assume that these times are representative of actual times,
# not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# Raise a ValueError instead if the input to convert is not in either of those formats
# or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
# But do not assume that someone’s hours will start ante meridiem
# and end post meridiem; someone might work late and even long hours
# (e.g., 5:00 PM to 9:00 AM).

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Check if the input string matches the expected format
    match = re.match(
        r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\s*to\s*(\d{1,2})(?::(\d{2}))?\s*(AM|PM)", s
    )

    if match:
        # Extract the hours, minutes, and AM/PM from the match
        (
            start_hour,
            start_minute,
            start_ampm,
            end_hour,
            end_minute,
            end_ampm,
        ) = match.groups()

        # Convert the hours and minutes to integers
        start_hour = int(start_hour)
        end_hour = int(end_hour)
        start_minute = int(start_minute) if start_minute else 0
        end_minute = int(end_minute) if end_minute else 0

        # Validate the hours and minutes
        if (
            not (0 <= start_hour <= 12)
            or not (0 <= end_hour <= 12)
            or not (0 <= start_minute < 60)
            or not (0 <= end_minute < 60)
        ):
            raise ValueError("Invalid time")

        # Convert the hours from 12-hour format to 24-hour format
        if start_ampm == "PM" and start_hour != 12:
            start_hour += 12
        elif start_ampm == "AM" and start_hour == 12:
            start_hour = 0
        if end_ampm == "PM" and end_hour != 12:
            end_hour += 12
        elif end_ampm == "AM" and end_hour == 12:
            end_hour = 0

        # Return the times in 24-hour format
        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    else:
        raise ValueError("Invalid format")


if __name__ == "__main__":
    main()
