from gameObject import GameObject
from item import Item
from food import Food
from weapon import Weapon
from monster import Monster

class Room(GameObject):

    def __init__(self, description, n, s, w, e, item=None, look=None, monster=None, use=None):
        self.Room = Room
        self.description = description
        self.n = n
        self.s = s
        self.w = w
        self.e = e
        self.item = item
        self.monster = monster
        self.look = look
        self.use = use

    def set_item(self, newItem):
        self.item = newItem

    def set_monster(self, monster):
        self.monster = monster

    def get_item(self):
        return self.item

    def get_monster(self):
        return self.monster

    def get_look(self):
        return self.look

    def get_use(self):
        return self.use

    def direction(self, d):         # so, to explain, whatever is set at init.
        if d == 0:                  # that is your direction to the next room
            return self.n           # so when the player inputs a dir.
        elif d == 1:                # you return the ROOM's coord.'s
            return self.s
        elif d == 2:
            return self.w
        elif d == 3:
            return self.e
        return -1

    def update(self, d, r):
        if d == 0:
            self.n = r
            return self.n
        elif d == 1:
            self.s = r
            return self.s
        elif d == 2:
            self.w = r
            return self.w
        elif d == 3:
            self.e = r
            return self.e
        return -1

    def setItem(self, newItem):
        self.item = newItem
        
    def add(self):
        return self.item.take_count()

    



# 
# item = Food("banana", "brother i swear to GOD")
# 
# print(type(item))
# 
# rm2 = Room("yo", None)
# 
# map = [rm2]
# 
# print(map[0].get_description())
# print(rm2.get_item())