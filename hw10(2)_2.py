class User:
    def __init__(self, health):
        self.health = health
        self.crash = 10

    def attack(self, enemy):
        enemy.health -= 10
        print(enemy.health)

    def damage(self, enemy):
        self.health -= enemy.crash
        print(self.health)


class Mage(User):
    def __init__(self, health):
        super().__init__(health)
        self.crash = 20

    def attack(self, enemy):
        enemy.health -= 20
        print(enemy.health)

    def damage(self, enemy):
        self.health -= enemy.crash


class Archer(User):
    def __init__(self, health):
        super().__init__(health)
        self.crash = 40

    def attack(self, enemy):
        enemy.health -= 40
        print(enemy.health)

    def damage(self, enemy):
        self.health -= enemy.crash


class Warrior(User):
    def __init__(self, health):
        super().__init__(health)
        self.crash = 30

    def attack(self, enemy):
        enemy.health -= 30
        print(enemy.health)

    def damage(self, enemy):
        self.health -= enemy.crash
