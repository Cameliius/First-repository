class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other

    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            return self.price / other


item1 = Item('Видеокарта', 15, 0)
item2 = Item('Процесор', 2, 0)

answer1 = item1 + item2
answer2 = item1 - item2
answer3 = item1 * item2
answer4 = item1 / item2
print(answer1)
print(answer2)
print(answer3)
print(answer4)
