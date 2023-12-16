from random import randint

class Die(): # класс представляющий один кубик
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self): # возвращает одно число
        return randint (1, self.num_sides)
