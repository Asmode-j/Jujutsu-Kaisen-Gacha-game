import random, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Cards:
    def __init__(self, id_card, name, info, cost):
        self.id_card = id_card
        self.name = name
        self.info = info
        self.cost = cost


base = sqlite3.connect("JJK_Data.db")
sql = base.cursor()
all_cards = sql.execute("SELECT id_card, name_card, text_card, cost_card FROM Cards").fetchall()
base.commit()

list_all_cards = []
dict_all_cards = {}

def create_cards():
    for card in all_cards:
        list_all_cards.append(Cards(card[0], card[1], card[2], card[3]))


create_cards()

for obj_card in list_all_cards:
    dict_all_cards[obj_card.id_card] = obj_card



# for i in list_all_cards:
#     print(i.id_card, i.name, i.info, i.cost)

# print(dict_all_cards)
#
# print(dict_all_cards.get(f"card_1").name)