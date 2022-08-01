
from itertools import count
import random
from pathlib import Path
#import openpyexcel


names = ["lekan", "Tobi", "Dayo"]

print(random.choice(names))


class Dice:
    def roll(self):
        first = random.randint(3, 5)
        second = random.randint(6, 9)
        return(first, second)


dice = Dice()
print(dice.roll())
"""
path = Path("")
for the in path.glob('*.py'):   
    print(the)"""

print(2>4)

print(len(names))











        