from gameObject import GameObject

class Item(GameObject):

    def __init__(self, name, description):
        self.Item = Item
        self.name = name
        self.description = description
        self.count = 0
        
    def get_count(self):
        return self.count
    
    def set_count(self, n):
        self.count = n
    
    def take_count(self):
        self.count = self.count + 1
        
    def destroy(self):
        self.count = 0
        
    def use(self):
        if self.count == 1:
            return True
        elif self.count == 0:
            return False
        return False
    