import sys
import requests

def get_bitcoin_price():
    # Check the command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Error: Invalid number of arguments.")
    
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number.")
    
    try:
        # Query the CoinDesk API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
        
        # Calculate and print the cost of the specified number of Bitcoins
        cost = bitcoins * price
        print(f"The current cost of {bitcoins} Bitcoins is {cost:,.4f} USD.")
    except requests.RequestException:
        sys.exit("Error: Could not retrieve data from the CoinDesk API.")

get_bitcoin_price()
