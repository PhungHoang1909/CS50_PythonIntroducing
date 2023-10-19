# Lecture 8 - OOP

import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name): #cls: class
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")