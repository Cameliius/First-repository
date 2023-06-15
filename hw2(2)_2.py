import random


class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health


def draka():
    unit_1 = Unit('Воин 1', health=100)
    unit_2 = Unit('Воин 2', health=100)
    persons = [unit_1, unit_2]
    while unit_1.health != 0 and unit_2.health != 0:
        atk = random.choice(persons)
        if atk == unit_1:
            unit_2.health -= 20
            print('Воин 1 атакавал война 2. Здоровье война 2:', unit_2.health)
        else:
            unit_1.health -= 20
            print('Воин 2 атакавал война 1. Здоровье война 1:', unit_1.health)
        if unit_1.health == 0:
            print('Воин 2 выиграл')
        elif unit_2.health == 0:
            print('Воин 1 выиграл')


draka()
