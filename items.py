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

Fist = Weapon("Fist", 1, 1, 0.05, 2, "MainHand")    
Sword = Weapon("Sword", 3, 5, 0.05, 2, "MainHand")
Dagger = Weapon("Dagger", 1, 4, 0.10, 3, "MainHand")
Spear = {
    "Name": "Spear",
    "MinDmg": 4,
    "MaxDmg": 6,
    "CritChance": 0.05,
    "CritMultiplier": 2,
    "EqSlot": "MainHand"
    }
Axe = {
    "Name": "Axe",
    "MinDmg": 2,
    "MaxDmg": 7,
    "CritChance": 0.05,
    "CritMultiplier": 2,
    "EqSlot": "MainHand"
    }
Wood_Shield = {
    "Name": "Wood_Shield",
    "pDef": 2,
    "mDef": 1,
    "EqSlot": "OffHand"
    }
Spellbook = {
    "Name": "Spellbook",
    "pDef": 0,
    "mDef": 4,
    "EqSlot": "OffHand"
    }
Kettle_Helm = {
    "Name": "Kettle_Helm",
    "pDef": 2,
    "mDef": 1,
    "EqSlot": "Head"
    }
Wizard_Hat = {
    "Name": "Wizard_Hat",
    "pDef": 1,
    "mDef": 2,
    "EqSlot": "Head"
    }
Leather_Armor = {
    "Name": "Leather_Armor",
    "pDef": 3,
    "mDef": 2,
    "EqSlot": "Armor"
    }
Chainmail_Armor = {
    "Name": "Chainmail_Armor",
    "pDef": 4,
    "mDef": 1,
    "EqSlot": "Armor"
    }
Steel_Armor = {
    "Name": "Steel_Armor",
    "pDef": 7,
    "mDef": 2,
    "EqSlot": "Armor"
    }
Power_Ring = {
    "Name": "Power_Ring"
    }
Health_Potion = {
    "Name": "Health_Potion"
    }
Tome_of_Firebolt = {
    "Name": "Tome_of_Firebolt",
    "Spell": "Firebolt"
    }

itemIDs = {
    #100: MainHand
    100: Fist,
    101: Sword,
    102: Dagger,
    103: Spear,
    104: Axe,
    #200: OffHand
    201: Wood_Shield,
    202: Spellbook,
    #300: Head
    301: Kettle_Helm,
    302: Wizard_Hat,
    #400: Armor
    401: Leather_Armor,
    402: Chainmail_Armor,
    403: Steel_Armor,
    #500: Accessory
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
'''
