import random


class Cherecters:
    def __init__(self, name, strenght, dexterity, constitution, intellegence, wisdom, charisma):
        self.name = name
        self.STR = strenght
        self.DEX = dexterity
        self.CON = constitution
        self.INT = intellegence
        self.WIZ = wisdom
        self.CHA = charisma


file = open("cherecters.txt", "r", encoding="utf-8")
lines = file.readlines()
ind_pers = []
name_pers = []
list_all_cherecters=[]

def create_cherecters():
    for line in lines:
        ind = line.split(';')[0]
        nam = line.split(';')[1].replace('\n', '')
        ind_pers.append(ind)
        name_pers.append(nam)
    for e, n in enumerate(zip(ind_pers, name_pers), 1):
        STR = random.randint(1, 20)
        DEX = random.randint(1, 20)
        CON = random.randint(1, 20)
        INT = random.randint(1, 20)
        WIZ = random.randint(1, 20)
        CHA = random.randint(1, 20)
        list_all_cherecters.append(Cherecters(n[1], STR, DEX, CON, INT, WIZ, CHA))
        #globals()[f"C{n[0]}"] = Cherecters(n[1], STR, DEX, CON, INT, WIZ, CHA)
        #list_all_cherecters.append(exec(f"C{n[0]}"))
        #print(e, n)
create_cherecters()

#print(list_all_cherecters)

#for i in ind_pers:
    #exec(f"name, str, dex, con, int, wiz, cha = C{i}.name, C{i}.STR, C{i}.DEX, C{i}.CON, C{i}.INT, C{i}.WIZ, C{i}.CHA")
    #print(f"Имя: {name}|Сила- {str}|Ловкость-{dex}|Телосложение-{con}|Интеллект-{int}|Мудрость-{wiz}|Харизма-{cha}")
