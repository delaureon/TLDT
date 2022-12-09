from item import Item

class Food(Item):
    def __init__(self, name, description):
        self.Food = Food
        self.name = name
        self.description = description
        self.restoreHP = 25
        self.count = 0
        
    def add(self):
        self.count = self.count + 1
        
    def consume(self):
        if self.count > 0:
            self.count = self.count - 1
            
    def restoreHP(self):
        return self.restoreHP()
    