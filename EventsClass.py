import random, sqlite3, pprint
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Events:
    def __init__(self,id_event, name_event, text_event = "", count_answer = 1, text_answer = "", text_continue = ""):
        self.id_event = id_event
        self.name_event = name_event
        self.text_event = text_event
        self.count_answer = count_answer
        self.text_answer = text_answer
        self.text_continue = text_continue


# base = sqlite3.connect("JJK_Data.db")
# sql = base.cursor()

# all_events_2_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 2").fetchall()
# start_2_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 's2'").fetchall()
# enemy_2_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'e2'").fetchall()
# strong_enemy_2_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'se2'").fetchall()
# boss_2_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'b2'").fetchall()
#
# all_events_3_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 3").fetchall()
# start_3_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 's3'").fetchall()
# enemy_3_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'e3'").fetchall()
# strong_enemy_3_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'se3'").fetchall()
# boss_3_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'b3'").fetchall()
# base.commit()


list_all_events = []
only_id_events = []
dict_all_events = {}
dict_obj_all_events = {}

def create_events():
    def events_1_floor():
        base = sqlite3.connect("JJK_Data.db")
        sql = base.cursor()
        all_events_1_floor = sql.execute("SELECT id_event, name_event, text_event,"
                                         "count_answer, text_answer, text_continue"
                                         " FROM Events WHERE floor = 1").fetchall()
        start_1_floor = sql.execute("SELECT id_event, name_event, text_event,"
                                         "count_answer, text_answer, text_continue "
                                    "FROM Events WHERE floor = 's1'").fetchall()
        enemy_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'e1'").fetchall()
        strong_enemy_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'se1'").fetchall()
        boss_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'b1'").fetchall()
        base.commit()

        for i in all_events_1_floor:
            only_id_events.append(i[0])
            dict_all_events[i[0]] = i[1], i[2], i[3], i[4], i[5]
            dict_obj_all_events[i[0]] = Events(i[0], i[1], i[2], i[3], i[4], i[5])
            list_all_events.append(Events(i[0], i[1], i[2], i[3], i[4], i[5]))
        for i in start_1_floor:
            dict_all_events[i[0]] = i[1], i[2], i[3], i[4], i[5]
            dict_obj_all_events[i[0]] = Events(i[0], i[1], i[2], i[3], i[4], i[5])
            list_all_events.append(Events(i[0], i[1], i[2], i[3], i[4], i[5]))
        for i in enemy_1_floor:
            dict_all_events[i[0]] = i[1]
            dict_obj_all_events[i[0]] = Events(i[0], i[1])
            list_all_events.append(Events(i[0], i[1]))
        for i in strong_enemy_1_floor:
            dict_all_events[i[0]] = i[1]
            dict_obj_all_events[i[0]] = Events(i[0], i[1])
            list_all_events.append(Events(i[0], i[1]))
        for i in boss_1_floor:
            dict_all_events[i[0]] = i[1]
            dict_obj_all_events[i[0]] = Events(i[0], i[1])
            list_all_events.append(Events(i[0], i[1]))

    events_1_floor()


create_events()



# for i in list_all_events:
#     print(i.id_event, i.name_event, i.text_event, i.count_answer, i.text_answer, i.text_continue)
# pprint.pprint(dict_all_events, width=170)
# print(dict_obj_all_events.get(f"event_1_start").name_event)
# print(dict_all_events.get(f"event_1_start"))
# print(only_id_events)
