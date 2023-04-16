'''
Hackathon Mini Game
Enemy Class
'''
#Very similar to player character with some differences streamlined
#for combat-only purpose
class Enemy:
    def __init__(self, name, MHP, HP, MMP, MP, STR, DEX, CON, INT, WIS, CHA, \
                 minDmg, maxDmg, pDef, mDef):
        self.name = name
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
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.pDef = pDef
        self.mDef = mDef
    #Now we do some abstraction
    def getName(self):
        return self.name
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
    def getMinDmg(self):
        return self.minDmg
    def getMaxDmg(self):
        return self.maxDmg
    def getPDef(self):
        return self.pdef
    def mgetMDef(self):
        return self.mDef
    #Increasing each stat
    #Honestly we probably won't be seeing any of these functions in use
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
    def plusMinDmg(self, num):
        self.minDmg += num
    def plusMaxDmg(self, num):
        self.maxDmg += num
    def plusPDef(self, num):
        self.pdef += num
    def plusMDef(self, num):
        self.mDef += num
    #Decrease each stat
    #Not sure why we have a + and a - function for each stat when
    #we could just slap on a negative sign when we need it
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
    def minusMinDmg(self, num):
        self.minDmg -= num
    def minusMaxDmg(self, num):
        self.maxDmg -= num
    def minusPDef(self, num):
        self.pdef -= num
    def minusMDef(self, num):
        self.mDef -= num

    def isAlive(self):
        if self.HP > 0:
            return True
        else:
            return False
        
    #What we want to see
    def __str__ (self):
        return f"Name: {self.name} \
HP: {self.HP}/{self.MHP} MP: {self.MP}/{self.MMP} \
STR: {self.STR} DEX: {self.DEX} CON: {self.CON} INT: {self.INT} \
WIS: {self.WIS} CHA: {self.CHA} \nminDmg: {self.minDmg} \
maxDmg: {self.maxDmg} pDef: {self.pDef} mDef: {self.mDef}"

#Initialize enemies, woohoo
#Similar to items, load this from a file for future version
Slime = Enemy("Slime",10,10,10,10,5,5,5,5,5,5,0,0,5,5)
Large_Slime = Enemy("Large_Slime",10,10,10,10,10,10,10,10,10,10,0,0,5,5)
King_Slime = Enemy("Large_Slime",25,25,10,10,10,10,10,10,10,10,10,10,10,10)
EnemyIDs = {
    0: Slime,
    1: Slime,
    2: Large_Slime,
    3: King_Slime
    }
