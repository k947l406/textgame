'''
Hackathon Mini Game
Character class
'''
import items
class Character:
    def __init__(self, MHP, HP, MMP, MP, STR, DEX, CON, INT, WIS, CHA,\
                MainHand, OffHand, Head, Armor, Accessory):
        self.MHP = MHP
        self.HP = HP
        self.MMP = MMP
        self.MP = MP
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.MainHand = MainHand
        self.OffHand = OffHand
        self.Head = Head
        self.Armor = Armor
        self.Accessory = Accessory
    #Now we do some abstraction
    #This one's for getting each stat
    def getMHP(self):
        return self.MHP
    def getHP(self):
        return self.HP
    def getMMP(self):
        return(self.MMP)   
    def getMP(self):
        return self.MP
    def getSTR(self):
        return self.STR
    def getDEX(self):
        return self.DEX
    def getCON(self):
        return self.CON
    def getINT(self):
        return self.INT
    def getWIS(self):
        return self.WIS
    def getCHA(self):
        return self.CHA
    #Increasing each stat
    def plusMHP(self, num):
        self.MHP += num
    def plusHP(self, num):
        #Current HP should not go above Max HP
        if self.HP + num > self.MHP:
            self.HP = self.MHP
        else:
            self.HP += num
    def plusMMP(self, num):
        self.MMP += num
    def plusMP(self, num):
        #Current MP should not go above Max MP
        if self.MP + num > self.MMP:
            self.MP = self.MMP
        else:
            self.MP += num
    def plusSTR(self, num):
        self.STR += num
    def plusDEX(self, num):
        self.DEX += num
    def plusCON(self, num):
        self.CON += num
    def plusINT(self, num):
        self.INT += num
    def plusWIS(self, num):
        self.WIS += num
    def plusCHA(self, num):
        self.CHA += num
    #Decrease each stat
    def minusMHP(self, num):
        self.MHP -= num
    def minusHP(self, num):
        #Current HP should not go above Max HP
        if self.HP - num > self.MHP: #Just in case of a negative number
            self.HP = self.MHP
        else:
            self.HP -= num
    def minusMMP(self, num):
        self.MMP -= num
    def minusMP(self, num):
        #Current MP should not go above Max MP
        if self.MP - num > self.MMP:
            self.MP = self.MMP
        else:
            self.MP -= num
    def minusSTR(self, num):
        self.STR -= num
    def minusDEX(self, num):
        self.DEX -= num
    def minusCON(self, num):
        self.CON -= num
    def minusINT(self, num):
        self.INT -= num
    def minusWIS(self, num):
        self.WIS -= num
    def minusCHA(self, num):
        self.CHA -= num
    #What we want to see
    def __str__ (self):
        return f"HP: {self.HP}/{self.MHP} MP: {self.MP}/{self.MMP} \
STR: {self.STR} DEX: {self.DEX} CON: {self.CON} INT: {self.INT} \
WIS: {self.WIS} CHA: {self.CHA} \nMain Hand: {self.MainHand} \
Off Hand: {self.OffHand} Head: {self.Head} Armor: {self.Armor} \
Accessory: {self.Accessory}"
    #Equip stuff
    #Get equip data
    def getMH(self):
        return self.MainHand
    def getOH(self):
        return self.OffHand
    def getHead(self):
        return self.Head
    def getArmor(self):
        return self.Armo
    def getAcc(self):
        return self.Accessory
    #Set equip data
    def setMH(self, item):
        self.MainHand = item
    def setOH(self, item):
        self.OffHand = item
    def setHead(self, item):
        self.Head = item
    def setArmor(self, item):
        self.Armor = item
    def setAcc(self, item):
        self.Accessory = item
    #There will be many checks to see if the player character is alive
    def isAlive(self):
        if self.HP > 0:
            return True
        else:
            return False

#Test stuff
'''
PC = Character(10,10,10,10,10,10,10,10,10,10,None,None,None,None,None)
print(PC.getHP())
PC.plusHP(9)
print(PC.STR)
PC.plusSTR(20)
print(PC.STR)
PC.setMH("Thing")
print(PC)
print(PC.isAlive())
'''
