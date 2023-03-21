import random, sqlite3


# base = sqlite3.connect("JJK_Data.db")
# sql = base.cursor()
#
# all_events_all_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 0").fetchall()
#
# all_events_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 1").fetchall()
# start_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 's1'").fetchall()
# enemy_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'e1'").fetchall()
# strong_enemy_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'se1'").fetchall()
# boss_1_floor = sql.execute("SELECT id_event, name_event FROM Events WHERE floor = 'b1'").fetchall()
#
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

# print(all_events_all_floor)
# print(all_events_1_floor)
# print(start_1_floor)
# print(enemy_1_floor)
# print(strong_enemy_1_floor)
# print(boss_1_floor)

# if Num_Floor == 1:
#     start = start_1_floor
#     all_events = all_events_1_floor
#     enemy = enemy_1_floor
#     strong_enemy = strong_enemy_1_floor
#     boss = boss_1_floor
# elif Num_Floor == 2:
#     start = start_2_floor
#     all_events = all_events_2_floor
#     enemy = enemy_2_floor
#     strong_enemy = strong_enemy_2_floor
#     boss = boss_2_floor
# elif Num_Floor == 3:
#     start = start_3_floor
#     all_events = all_events_3_floor
#     enemy = enemy_3_floor
#     strong_enemy = strong_enemy_3_floor
#     boss = boss_3_floor

def create_all_Floors():
    def Decorator_number_Floor(func):
        def Wrapper(*args):
            # print('Этаж №', args[0])
            result = func(elit_vrag=5*args[0], magazin=3*args[0]//2, otdih=3*args[0]//2, Num_Floor=args[0])
            # print(result)
            return result
        return  Wrapper

    def Floors(elit_vrag, magazin, otdih, Num_Floor):
        Floor = []

        all_events = ["Start", "Event", "Enemy", "Strong_Enemy", "Rest", "Shop", "Boss"]

        ogranichenie_elit_vrag = elit_vrag
        ogranichenie_magazin = magazin
        ogranichenie_otdih = otdih

        event_count=1
        enemy_count=1
        senemy_count=1
        rest_count=1
        shop_count=1
        for row_e, column_event in enumerate(range(0,13)):
            if row_e == 0 or row_e == 12:
                if row_e == 0:
                    #Начало
                    Floor.append([all_events[0]])
                    continue
                if row_e == 12:
                    #Босс
                    Floor.append([all_events[6]])
                    break

            rooms_on_row = []
            kol_vo_ev = random.randint(1, 4)
            for i in range(kol_vo_ev):
                #элитный враг
                if ogranichenie_elit_vrag>0:
                    if row_e > 3 and row_e <= 9:
                        k = random.randint(1, 100)
                        if k<=30:
                            rooms_on_row.append(f"{all_events[3]}_{senemy_count}")
                            senemy_count+=1
                            ogranichenie_elit_vrag -=1
                            continue
                #магазин
                if ogranichenie_magazin>0:
                    if  row_e >= 5 and row_e <= 10:
                        k = random.randint(1, 100)
                        if k<=40:
                            rooms_on_row.append(f"{all_events[5]}_{shop_count}")
                            shop_count+=1
                            ogranichenie_magazin -=1
                            continue
                #Отдых
                if ogranichenie_otdih>0:
                    if row_e >= 3 and row_e <= 11:
                        k = random.randint(1, 100)
                        if k <= 40:
                            rooms_on_row.append(f"{all_events[4]}_{rest_count}")
                            rest_count+=1
                            ogranichenie_otdih -= 1
                            continue

                event_or_enemy = random.randint(0, 1)
                if event_or_enemy == 0:
                    rooms_on_row.append(f"{all_events[1]}_{event_count}")
                    event_count+=1
                elif event_or_enemy == 1:
                    rooms_on_row.append(f"{all_events[2]}_{enemy_count}")
                    enemy_count+=1

            Floor.append(rooms_on_row)

        return Floor


    floor = Decorator_number_Floor(Floors)
    Floor_1 = floor(1)
    Floor_2 = floor(2)
    Floor_3 = floor(3)

    all_Floors = [Floor_1,Floor_2,Floor_3]
    return all_Floors


create_all_Floors()