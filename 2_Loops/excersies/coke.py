# In a file called coke.py, implement a program that prompts the user to 
# insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change 
# the user is owed. 
# Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination: 25 10 5

amount = 50
changes = 0
while (amount > 0):
    print("Amount Due: ", amount)
    coin = int(input("Insert coin: "))
    amount = amount - coin
    changes += coin
    if (amount <= 0):
        if (amount == 0):
            print("Change Owned: 0")
        elif (amount < 0):
            print("Change Owned: ",  changes - 50)


        