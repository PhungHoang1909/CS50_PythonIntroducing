def convert_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_str = input("Enter a date (or Ctrl-D to finish): ")
        for i, month in enumerate(months, start=1):
            # Replace the month name with its number
            date_str = date_str.replace(month, str(i))
        
        # Split the date into month, day, and year
        parts = date_str.split('/')
        
        if len(parts) != 3:
            print("Invalid date. Please try again.")
            continue
        
        month, day, year = parts
        
        # Check if the month, day, and year are valid numbers
        if not month.isdigit() or not day.isdigit() or not year.isdigit():
            print("Invalid date. Please try again.")
            continue
        
        # Format the date in YYYY-MM-DD format
        print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        break

convert_date()
