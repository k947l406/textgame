'''
Hackathon Mini Game
Town Scene
'''
import random
from character import Character
from enemy import Enemy
from inventory import Inventory
from items import itemIDs
from battle import Battle

def run():
running = True
while running:
    moveList = ["Store", "Train", "Status", "Inventory", "Battle"]
        for action in moveList:
            print(f"{action}|", end="")
        print()
        userInput = input("What will you do?: ")
        if userInput.lower() == "store":
            
        elif userInput.lower() == "train":
            
        elif userInput.lower() == "battle":
            #newBattle = Battle()
        elif userInput.lower() == "status":
            print(self.char)
        elif userInput.lower() == "inventory":
            print(self.inv)
