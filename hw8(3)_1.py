class Item:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __repr__(self):
        return self.brand


items_list = [
    Item(1000, 'Apple'),
    Item(1200, 'Apple'),
    Item(900, 'Samsung'),
    Item(700, 'Samsung'),
    Item(660, 'Xiomi')
]

result = filter(lambda item: item.brand == 'Apple', items_list)
print(list(result))


# name_list = ['данил', 'артём', 'никита', 'влад']
# result = map(lambda items: items.capitalize(), name_list)
# print(list(result))
