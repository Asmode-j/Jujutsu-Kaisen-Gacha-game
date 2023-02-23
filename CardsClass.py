import random
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Cards:
    def __init__(self, index, name, info, cost):
        self.index = index
        self.name = name
        self.info = info
        self.cost = cost


file = open("Data/Cards/Cards.txt", "r", encoding="utf-8")
lines = file.readlines()

index_card = []
name_card = []
info_card = []
cost_card = []
list_all_cards = []
dict_all_cards = {}

def create_cards():
    for line in lines:
        index_card.append(line.split(';')[0])
        name_card.append(line.split(';')[1].replace('\n', ''))
        info_card.append(line.split(';')[2].replace('\n', ''))
        cost_card.append(int(line.split(';')[3].replace('\n', '')))
    for ind_nam_inf_cost in zip(index_card, name_card, info_card, cost_card):
        index = ind_nam_inf_cost[0]
        name = ind_nam_inf_cost[1]
        info = ind_nam_inf_cost[2]
        cost = ind_nam_inf_cost[3]
        list_all_cards.append(Cards(index, name, info, cost))


create_cards()

for obj_card in list_all_cards:
    dict_all_cards[obj_card.index] = obj_card



for i in list_all_cards:
    print(i.index, i.name, i.info, i.cost)

print(dict_all_cards)

print(dict_all_cards.get(f"card_1").name)