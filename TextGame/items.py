'''
Hackathon Mini Game
Items dictionary and inilization
'''
#We have to define all the items before arranging them into a dictionary
#These items are dictionaries themselves
class Item:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    #All items have a use function, which usually does nothing
    def use(self):
        return "This item does nothing."

    def __str__(self):
        return f"{self.name}"
    
class Weapon(Item):    
    def __init__(self, name, minDmg, maxDmg, critChance, critMulti, eqSlot):
        super().__init__(name)
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.critChance = critChance
        self.critMulti = critMulti
        self.eqSlot = eqSlot
    #This is where we get attributes
    def getMinDmg(self):
        return self.minDmg
    def getMaxDmg(self):
        return self.minDmg
    def getCritChance(self):
        return self.critChance
    def getCritMulti(self):
        return self.critMulti
    def getEqSlot(self):
        return self.eqSlot

class Armor(Item):    
    def __init__(self, name, pDef, mDef, eqSlot):
        super().__init__(name)
        self.pDef = pDef
        self.mDef = mDef
        self.eqSlot = eqSlot
    #This is where we get attributes
    def getPDef(self):
        return self.pDef
    def getMDef(self):
        return self.mDef
    def getEqSlot(self):
        return self.eqSlot

#Instead of hardcoding this, future versions should read in a file
#that translates into
Main_Empty = Weapon("Main_Empty", 1, 1, 0.05, 2, "MainHand")    
Sword = Weapon("Sword", 3, 5, 0.05, 2, "MainHand")
Dagger = Weapon("Dagger", 1, 4, 0.10, 3, "MainHand")
Spear = Weapon("Spear", 4, 6, 0.05, 2, "MainHand")
Axe = Weapon("Axe", 2, 7, 0.05, 2, "MainHand")

Off_Empty = Armor("Off_Empty", 0, 0, "OffHand")
Wood_Shield = Armor("Wood_Shield", 2, 1, "OffHand")
Spellbook = Armor("Spellbook", 0, 4, "OffHand")

Head_Empty = Armor("Head_Empty", 0, 0, "Head")
Kettle_Helm = Armor("Kettle_Helm", 2, 1, "Head")
Wizard_Hat = Armor("Wizard_Hat", 1, 2, "Head")

Armor_Empty = Armor("Armor_Empty", 0, 0, "Armor")
Leather_Armor = Armor("Leather_Armor", 3, 2, "Armor")
Chainmail_Armor = Armor("Chainmail_Armor", 4, 1, "Armor")
Steel_Armor = Armor("Steel_Armor", 7, 2, "Armor")

Accessory_Empty = Item("Accessory_Empty")
Power_Ring = Item("Power_Ring")
Health_Potion = Item("Health_Potion")
Tome_of_Firebolt = Item("Tome_of_Firebolt")

itemIDs = {
    #100: MainHand
    100: Main_Empty,
    101: Sword,
    102: Dagger,
    103: Spear,
    104: Axe,
    #200: OffHand
    200: Off_Empty,
    201: Wood_Shield,
    202: Spellbook,
    #300: Head
    300: Head_Empty,
    301: Kettle_Helm,
    302: Wizard_Hat,
    #400: Armor
    400: Armor_Empty,
    401: Leather_Armor,
    402: Chainmail_Armor,
    403: Steel_Armor,
    #500: Accessory
    500: Accessory_Empty,
    501: Power_Ring,
    #600: Consumable
    601: Health_Potion,
    #700: Tome
    602: Tome_of_Firebolt
    }

#Test stuff
'''
x = itemIDs.get(101)
print(x)
mindmgtest = x.getMinDmg()
print(x.use())
print(mindmgtest)
print(itemIDs.get(602))
ID = itemIDs
print(ID)
'''
