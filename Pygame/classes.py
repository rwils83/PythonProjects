class Item():
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


class Weapon(Item):
    def __init__(self, name, weight, price, attack):
        Item.__init__(self, name, weight, price)
        self.attack = attack


class Armor(Item):
    def __init__(self, name, weight, price, armor):
        Item.__init__(self, name, weight, price)
        self.armor = armor


class Inventory():
    def __init__(self):
        self.weapons = {}
        self.armor = {}

    def add_weapon(self, weapon):
        self.weapons[weapon.name] = weapon

    def add_armor(self, armor):
        self.armor[armor.name] = armor

    def print_weapons(self):
        print('\t'.join(['Name', 'Atk', 'Lb', 'Val']))
        for item in self.weapons.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.weight, item.price]]))

    def print_armor(self):
        print('\t'.join(['Name', 'Arm', 'Lb', 'Val']))
        for item in self.armor.values():
            print('\t'.join([str(x) for x in [item.name, item.armor, item.weight, item.price]]))


class Shop():
    def __init__(self):
        self.items = {}

    def remove_item(self, item):
        self.items[item.name] = item


class Character():
    def __init__(self):
        pass


class Player(Character):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health = self.health - damage

    def add_health(self, restore):
        self.health = self.health + restore

    def print_player_stats(self):
        print("Name: " + str(self.name.title()))
        print("Health: " + str(self.health))
        print("Strength: " + str(self.strength))

