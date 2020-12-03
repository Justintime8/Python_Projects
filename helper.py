from random import randint

class Dice:
    def __init__(self):
        self.min_roll = 1
        self.max_roll = 6

    def roll_dice(self):
        return randint(self.min_roll, self.max_roll)
