import random


class Enemy:
    def __init__(self, name, info,
                 strenght, dexterity, constitution, intellegence, wisdom, charisma,
                 health, cursed_energy):
        self.name = name
        self.info = info
        self.STR = strenght
        self.DEX = dexterity
        self.CON = constitution
        self.INT = intellegence
        self.WIZ = wisdom
        self.CHA = charisma
        self.HP = health
        self.CE = cursed_energy


file = open("Data/Cherecters/enemy.txt", "r", encoding="utf-8")
lines = file.readlines()
ind_enemy = []
name_enemy = []
info_enemy = []
scal_enemy = []
list_all_enemy = []


def create_enemy():
    for line in lines:
        ind_enemy.append(line.split(';')[0])
        name_enemy.append(line.split(';')[1].replace('\n', ''))
        info_enemy.append(line.split(';')[2].replace('\n', ''))
        scal_enemy.append(int(line.split(';')[3].replace('\n', '')))
    for e, name_info in enumerate(zip(name_enemy, info_enemy), 0):
        s = scal_enemy[e]
        STR = random.randint(1 * s, 5 * s)
        DEX = random.randint(1 * s, 5 * s)
        CON = random.randint(1 * s, 5 * s)
        INT = random.randint(1 * s, 5 * s)
        WIZ = random.randint(1 * s, 5 * s)
        CHA = random.randint(1 * s, 5 * s)
        HP = random.randint(10 * s, 20 * s)
        CE = random.randint(10 * s, 20 * s)
        list_all_enemy.append(Enemy(name_info[0], name_info[1], STR, DEX, CON, INT, WIZ, CHA, HP, CE))


create_enemy()

for i in list_all_enemy:
    print(i.name, i.HP, i.CE)
