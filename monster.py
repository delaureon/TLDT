from gameObject import GameObject

class Monster(GameObject):

    def __init__(self, name, description, hp, attack, tag):
        self.Monster = Monster
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.tag = tag

    def is_hit(self, dmg):
        self.hp = self.hp - dmg
        if self.hp <= 0:
            self.hp = 0
            self.tag = 'dead'
            print(f"You have defeated {self.name}!")
        else:
            print(f"Its health is at {self.hp}!")

    def get_attack(self):
        return self.attack

    def get_hp(self):
        return self.hp
# monster = Monster('goblin', 'goblin thing', 15, 10, '_')
# print(monster.get_name())
# monster.is_hit(10)
# print(monster.get_hp())




