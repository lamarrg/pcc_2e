from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

roll1 = Die()

for roll in range(1, 11):
    roll1.roll_die()

roll1 = Die(10)

for roll in range(1, 11):
    roll1.roll_die()


roll1 = Die(20)

for roll in range(1, 11):
    roll1.roll_die()


