from item import Item

class Weapon(Item):
    def __init__(self, name, description, damage):
        self.Weapon = Weapon
        self.name = name
        self.description = description
        self.damage = damage
        self.count = 0

    def get_damage(self):
        return self.damage

# weapon = Weapon(25)
# weapon.set_count(1)
# print(weapon.get_damage())
# weapon.destroy()
# print(weapon.get_count())