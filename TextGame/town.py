'''
Hackathon Mini Game
Town Scene
'''
import random
from character import Character
from enemy import Enemy
from enemy import EnemyIDs as eID
from inventory import Inventory
from items import itemIDs as iID
from battle import Battle
import save
#Due to the time crunch, we're cramming everything into town
#Initializing player character data
#Currently hardcoded until save is impleneted
#'''
try:
    PC = save.LoadPC()
    INV = save.LoadINV()
except:
    print("There was an error loading save data. Starting new game...")
    PC = Character(10,10,10,10,10,10,10,10,10,10,100,200,300,400,500)
    INV = Inventory(20, 100)

def run(PC, INV):
    running = True
    while running == True:
        actList = ["Store", "Inn", "Train", "Status", "Inventory", "Battle",\
                   "Save", "Quit"]
        for action in actList:
            print(f"{action}|", end="")
        print()
        userInput = input("What will you do?: ")
        if userInput.lower() == "store":
            #store.open()
            print("You approach the store, but it is closed.")
        if userInput.lower() == "inn":
            PC.plusHP(PC.getMHP()) #heal by your own max stat
            PC.plusMP(PC.getMMP()) #effectively fully recovers
            print("You enter the inn for the day and fully recover.")
        elif userInput.lower() == "train":
            print("You enter the training center.")
            statList = ["MHP","MMP","STR","DEX","CON","INT","WIS","CHA"]
            for statName in statList:
                print(f"{statName}|", end="")
            print()
            userInput = input("What stat would you like to improve for 10 GP? ")
            if userInput.upper() in statList:
                if INV.getGold() >= 10:
                    inc = random.randint(1,3)   
                    exp = "PC.plus"+userInput.upper()+"("+str(inc)+")"
                    eval(exp)
                    print(f"Your {userInput.upper()} has increased by {inc} points.")
                    INV.remGold(10)
                    print("You paid 10 gold.")
                else:
                    print("You don't have enough gold to train.")
            else:
                print("Invalid stat name")
        elif userInput.lower() == "battle":
            newBattle = Battle(eID[random.randint(0,len(eID)-1)], PC, INV)
            outcome = newBattle.start()
            if outcome == True:
                INV.addGold(50)
            pass
        elif userInput.lower() == "status":
            print(PC)
        elif userInput.lower() == "inventory":
            print(INV)
        elif userInput.lower() == "save":
            save.Save(PC, INV)
            print("Data Saved")
        elif userInput.lower() == "quit":
            userInput = input("Would you like to save? [Y/N]: ")
            if userInput.lower() == "y":
                save.Save(PC, INV)
                print("Data Saved")
            elif userInput.lower() == "n":
                pass
            else:
                print("That is not a valid input")
            running = False
        else:
            print("That is not a valid action")

run(PC, INV)
