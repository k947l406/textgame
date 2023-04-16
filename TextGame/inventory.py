'''
Hackathon Mini Game
Inventory class
'''
class Inventory:
    def __init__(self, slots, gold):
        self.slots = slots
        self.gold = gold
        self.items = {}
        for i in range(slots):
            self.items[i] = None

    def __str__(self):
        string = f"Gold: {self.gold} \nSlot: Item\n"
        for i in range(self.slots):
            string += f"{i}: {self.items[i]}\n"
        return string

    def __repr__(self):
        return f"Inventory({self.slots},{self.gold})"

    def addItem(self, slot, item):
        if (0 <= slot <= self.slots):
            self.items[slot] = item
        else:
            return "That slot doesn't exist!"

    def remItem(self, slot, item):
        if (0 <= slot <= self.slots):
            self.items[slot] = None
        else:
            return "That slot doesn't exist!"
        
    def getGold(self):
        return self.gold
    def addGold(self, num):
            self.gold += num
    def remGold(self, num):
            self.gold -= num

###Test stuff
'''
inv = Inventory(20, 100)
inv.addItem(10, "Thing")
print(inv)
inv.remItem(10, "Thing")
print(inv)
'''
