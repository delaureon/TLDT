from gameObject import GameObject

class Player(GameObject):

    def __init__(self, hp):
        self.Player = Player
        self.hp = hp

    def get_hp(self):
        return self.hp

    def is_hit(self, dmg):
        self.hp = self.hp - dmg
        if self.hp <= 0:
            self.hp = 0
            print(f"You have defeated {self.name}!")
        else:
            print(f"Its health is at {self.hp}!")
            
    def consume(self):
        self.hp = self.hp + 20
        if self.hp >= 100:
            self.hp = 100