# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD 
# format and then sings prints how old they are in minutes, rounded to the nearest integer, 
# using English words instead of numerals, 

from datetime import date
import inflect
import sys
import re

def main():
    birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
    if not re.match(r'\d{4}-\d{2}-\d{2}', birth_date_str):
        print("Invalid date format. Please enter in YYYY-MM-DD format.")
        sys.exit(1)

    birth_date = date.fromisoformat(birth_date_str)
    age_in_minutes = calculate_age_in_minutes(birth_date)
    age_in_words = convert_to_words(age_in_minutes)

    print(f"You are {age_in_words} minutes old.")

def calculate_age_in_minutes(birth_date):
    today = date.today()
    age_in_days = (today - birth_date).days
    age_in_minutes = age_in_days * 24 * 60
    return age_in_minutes

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

if __name__ == "__main__":
    main()
