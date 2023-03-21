import random, sqlite3


class Characters:
    def __init__(self, id, name, info, abilities, level,
                 strength, dexterity, constitution, intelligence, wisdom, charisma,
                 health, cursed_energy, energy,
                 attack, class_dodge, class_armor, personal_artifacts=""):
        self.ID = id
        self.NAME = name
        self.INFO = info
        self.ABIL = abilities

        self.LVL = level

        self.STR = strength
        self.DEX = dexterity
        self.CON = constitution
        self.INT = intelligence
        self.WIZ = wisdom
        self.CHA = charisma

        self.MAX_HP = health + ((constitution * level) + ((strength + dexterity) // 2))
        self.MAX_CE = cursed_energy + ((intelligence * level) + ((wisdom + charisma) // 2))
        self.MAX_EN = energy

        self.ATK = ((attack + (strength + dexterity + wisdom + charisma) // 2) * level) // 3
        self.DODG = (class_dodge + dexterity) // 2
        self.ARMR = (class_armor + constitution) // 2

        self.PA = personal_artifacts
    def lvlup(self, level):
        self.LVL = level

        self.MAX_HP = self.MAX_HP + ((self.CON * level) + ((self.STR + self.DEX) // 2))
        self.MAX_CE = self.MAX_CE + ((self.INT * level) + ((self.WIZ + self.CHA) // 2))

        self.ATK = ((self.ATK + (self.STR + self.DEX + self.WIZ + self.CHA) // 2) * level) // 3


base = sqlite3.connect("JJK_Data.db")
sql = base.cursor()

all_characters = sql.execute("SELECT * FROM Сharacters").fetchall()
base.commit()

stars_pers = []
ind_pers = []
name_pers = []
info_pers = []
abilities_pers = []
personal_artifacts = []
list_all_characters = []
dict_all_characters = {}

characters_5 = []
characters_4 = []
characters_3 = []


def create_characters():
    for character in all_characters:
        stars_pers.append(character[0])
        ind_pers.append(character[1])
        name_pers.append(character[2])
        info_pers.append(character[3])
        abilities_pers.append(character[4])
        personal_artifacts.append(character[5])
    for e, name_info_abil_star_art in enumerate(zip(name_pers, info_pers, abilities_pers, stars_pers, personal_artifacts), 0):
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

        list_all_characters.append(
            Characters(ind_pers[e], name_info_abil_star_art[0], name_info_abil_star_art[1], name_info_abil_star_art[2], LVL,
                       STR, DEX, CON, INT, WIZ, CHA,
                       HP, CE, EN,
                       ATK, DODG, ARMR, name_info_abil_star_art[4]))

        if name_info_abil_star_art[3] == 5:
            characters_5.append(ind_pers[e])
        elif name_info_abil_star_art[3] == 4:
            characters_4.append(ind_pers[e])
        elif name_info_abil_star_art[3] == 3:
            characters_3.append(ind_pers[e])


create_characters()

for obj_character in list_all_characters:
    dict_all_characters[obj_character.ID] = obj_character

# print(list_all_characters)
# print(dict_all_characters)
# print(characters_5)
# print(characters_4)
# print(characters_3)

# print(dict_all_characters.get(f"01").NAME)

# gg = list_all_characters[0]
# print(gg.ID ,gg.NAME, gg.LVL, gg.ABIL , gg.MAX_HP, gg.MAX_CE, gg.ATK, gg.DODG, gg.ARMR, gg.PA)
#
# gg.lvlup(gg.LVL+1)
# print(gg.ID ,gg.NAME, gg.LVL, gg.ABIL , gg.MAX_HP, gg.MAX_CE, gg.ATK, gg.DODG, gg.ARMR)

