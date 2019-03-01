class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]]))


class Shop(object):
    def __init__(self):
        self.items = {}

    def remove_item(self, item):
        self.items[item.name] = item