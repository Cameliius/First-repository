import random

class Tank:
    def __init__(self, model, armor, health, min_damage, max_damage):
        self.model = model
        self.armor = armor
        self.health = health
        self.damage = random.randint(min_damage, max_damage)

    def print_info(self):
        print(self.model, 'имеет лобовую броню', self.armor, 'здоровье', self.health,
              'и урон', self.damage)

    def health_down(self, enemy_damage):
        self.health -= enemy_damage
        print('\n', self.model)
        print('Командир, по экипажу', self.model, 'нанесли',
              enemy_damage, 'урона, текущее здоровье:',
              self.health)

    def shot(self, enemy):

        if enemy.health <= 0 or self.damage >= enemy.health:
            enemy.health = 0
            print(enemy.model, 'был уничтожен')
        else:
            enemy.health_down(self.damage)
            print('\n', self.model)
            print('Точно в цель! У противника осталось', enemy.health, 'hp')



tank1 = Tank('tiger', 100, 100, 50, 150)
tank2 = Tank('AMZ', 81, 50, 10, 80)
tank3 = Tank('ИС3', 150, 20, 100, 200)

tank1.model = 'T34'

tank1.print_info()
tank2.print_info()
tank3.print_info()

tank2.shot(tank1)
