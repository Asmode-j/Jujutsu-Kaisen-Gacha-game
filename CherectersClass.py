import random


class Cherecters:
    def __init__(self, name, info, abilites, level,
                 strenght, dexterity, constitution, intellegence, wisdom, charisma,
                 health, cursed_energy, energy,
                 attack, class_dodge, class_armor):
        self.NAME = name
        self.INFO = info
        self.ABIL = abilites
        self.LVL = level

        self.STR = strenght
        self.DEX = dexterity
        self.CON = constitution
        self.INT = intellegence
        self.WIZ = wisdom
        self.CHA = charisma

        self.HP = health+((constitution*level)+((strenght+dexterity)//2))
        self.CE = cursed_energy+((intellegence*level)+((wisdom+charisma)//2))
        self.EN = energy

        self.ATK = ((attack+(strenght+dexterity+wisdom+charisma)//2)*level)//3
        self.DODG = (class_dodge+dexterity)//2
        self.ARMR = (class_armor+constitution)//2

file = open("Data/Cherecters/cherecters.txt", "r", encoding="utf-8")
lines = file.readlines()
ind_pers = []
name_pers = []
info_pers = []
abilites_pers = []
list_all_cherecters=[]

def create_cherecters():
    for line in lines:
        ind_pers.append(line.split(';')[0])
        name_pers.append(line.split(';')[1].replace('\n', ''))
        info_pers.append(line.split(';')[2].replace('\n', ''))
        abilites_pers.append(line.split(';')[3].replace('\n', ''))
    for e, name_info_abil in enumerate(zip(name_pers, info_pers, abilites_pers), 1):
        LVL = 1
        STR = random.randint(1, 20)
        DEX = random.randint(1, 20)
        CON = random.randint(1, 20)
        INT = random.randint(1, 20)
        WIZ = random.randint(1, 20)
        CHA = random.randint(1, 20)
        HP = 100
        CE = 100
        EN = 3
        ATK = 5
        DODG = 5
        ARMR = 5
        list_all_cherecters.append(Cherecters(name_info_abil[0], name_info_abil[1], name_info_abil[2], LVL,
                                              STR, DEX, CON, INT, WIZ, CHA,
                                              HP, CE, EN,
                                              ATK, DODG, ARMR))

create_cherecters()
