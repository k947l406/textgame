'''
Hackathon Mini Game
Battle Scene
'''
import random
from character import Character
from enemy import Enemy
from inventory import Inventory
from items import itemIDs as iID

#TODO: cleanup and reformat
class Battle:
    def __init__(self, enemy, char, inv):
        self.enemy = enemy
        self.char = char
        self.inv = inv
        self.order = [char, enemy]
        self.fight = True

    def actions(self):
        actionList = ["Attack", "Run", "Status", "Inventory", "Pass"]
        for action in actionList:
            print(f"{action}|", end="")
        print()
        userInput = input("What will you do?: ")
        if userInput.lower() == "attack":
            #calculate damage
            minDmg = iID[self.char.MainHand].minDmg
            maxDmg = iID[self.char.MainHand].maxDmg
            rawDmg = random.randint(minDmg, maxDmg) + self.char.STR
            dmgTaken = rawDmg - self.enemy.pDef
            if dmgTaken < 0:
                dmgTaken = 0
            self.enemy.minusHP(dmgTaken)
            print(f"You hit {self.enemy.getName()} for {dmgTaken} damage")
        elif userInput.lower() == "run":
            self.fight = False
            print("You ran away!")
        elif userInput.lower() == "status":
            print(self.char)
            self.actions() #call actions again because checking status is free
        elif userInput.lower() == "inventory":
            print(self.inv)
            #add an option to use item that doesn't call self.action afterwards
            self.actions()
        elif userInput.lower() == "pass":
            print("You pass your action")
        else:
            print("That is not a valid action")
            self.actions()
    #Yeah, we could really reuse the character class for enemies
    #instead of having made a new class with slightly different values
    #so that methods can be reused
    def enemyAttack(self):
        minDmg = self.enemy.minDmg
        maxDmg = self.enemy.maxDmg
        rawDmg = random.randint(minDmg, maxDmg) + self.enemy.STR
        #need to do something here to add up all the pDef from gear
        pDef = iID[self.char.Head].getPDef() + iID[self.char.Armor].getPDef()
        mDef = iID[self.char.Head].getMDef() + iID[self.char.Armor].getMDef()
        dmgTaken = rawDmg - pDef
        self.char.minusHP(dmgTaken)
        print(f"You took {dmgTaken} damage")
    
    def start(self):
        order = self.order
        print(f"You are fighting {self.enemy.getName()}")
        while(order.count(self.char) != 0 and order.count(self.enemy) != 0 and self.fight):
            for unit in self.order:
                if unit == self.char:
                    if unit.isAlive():
                        self.actions()
                    else:
                        print("You died")
                        self.order.remove(unit)
                        return False
                elif self.fight != True:
                    break
                        
                else:
                    if unit.isAlive():
                        self.enemyAttack()
                    else:
                        print("Enemy died")
                        self.order.remove(unit)
                        return True
                
#Test stuff
'''
DummyPC = Character(100,100,10,10,10,10,10,10,10,10, \
                    itemIDs[101],None,None,itemIDs[401],None)
#After programming this, I'm not sure if we need an enemy class
#The character class honestly should work fine
DummyE = Enemy("Training_Dummy",10,10,10,10,10,10,10,10,10,10,10,10,10,10)
DummyInv = Inventory(20,100)
battle = Battle(DummyE, DummyPC, DummyInv)
battle.start()
'''
