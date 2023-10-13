#Lecture 4 - Libraries

import random

coin = random.choice(["heads", "tails"])
number = random.randint(1, 10)
cards  = ["jack", "queen", "king"]
random.shuffle(cards)

print(coin)
print(number)
for card in cards:
    print(card)
