'''
Hackathon Mini Game
Save and load
'''
from character import Character
from inventory import Inventory
'''
Character(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 200, 300, 400, 500)
'''
def Save(PC, INV):
    f = open("save.txt", "w")
    f.write(repr(PC))
    f.write("\n")
    f.write(repr(INV))
    f.close()

def LoadPC():
    f = open("save.txt", "r")
    pc = f.readline()
    PC = eval(pc)
    f.close()
    return PC
def LoadINV():
    f = open("save.txt", "r")
    f.readline()
    inv = f.readline()
    INV = eval(inv)
    f.close()
    return INV
