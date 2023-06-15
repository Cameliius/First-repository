class User:
    def __init__(self, health):
        self.health = health

    def attack(self, enemy):
        enemy.health -= 10
        print(enemy.health)

    def damage(self):
        self.health -= 10
        print(self.health)
