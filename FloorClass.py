import random


def create_all_Floors():
    def Decorator_number_Floor(func):
        def Wrapper(*args):
            # print('Этаж №', args[0])
            result = func(elit_vrag=5*args[0], magazin=3*args[0]//2, otdih=3*args[0]//2)
            # print(result)
            return result
        return  Wrapper

    def Floors(elit_vrag, magazin, otdih):
        Floor = []
        events = ['Враг', 'Событие','Элитный враг', 'Магазин', 'Отдых']
        ogranichenie_elit_vrag = elit_vrag
        ogranichenie_magazin = magazin
        ogranichenie_otdih = otdih

        for row_e, column_event in enumerate(range(0,13)):
            if row_e == 0 or row_e == 12:
                if row_e == 0:
                    Floor.append(['Начало'])
                    # print(row_e, '[ Начало ]')
                    continue
                if row_e == 12:
                    Floor.append(['Босс'])
                    # print(row_e, '[ Босс ]')
                    break

            rooms_on_row = []
            kol_vo_ev = random.randint(1, 4)
            for i in range(kol_vo_ev):
                #элитный враг
                if ogranichenie_elit_vrag>0:
                    if row_e > 3 and row_e <= 9:
                        k = random.randint(1, 100)
                        if k<=30:
                            event = events[2]
                            rooms_on_row.append(event)
                            ogranichenie_elit_vrag -=1
                            continue
                #магазин
                if ogranichenie_magazin>0:
                    if  row_e >= 5 and row_e <= 10:
                        k = random.randint(1, 100)
                        if k<=40:
                            event = events[3]
                            rooms_on_row.append(event)
                            ogranichenie_magazin -=1
                            continue
                #Отдых
                if ogranichenie_otdih>0:
                    if row_e >= 3 and row_e <= 11:
                        k = random.randint(1, 100)
                        if k <= 40:
                            event = events[4]
                            rooms_on_row.append(event)
                            ogranichenie_otdih -= 1
                            continue
                index_event = random.randint(0, 1)
                event = events[index_event]
                rooms_on_row.append(event)
            Floor.append(rooms_on_row)
        return Floor


    dict_all = {'Враг': ['Слабый противник', 'Средний противник', 'Сильный противник'],
                'Событие': ['Хорошее событие','Плохое событие'],
                'Элитный враг': ['Элитный враг 1', 'Элитный враг 2','Элитный враг 3']}

    floor = Decorator_number_Floor(Floors)
    Floor_1 = floor(1)
    Floor_2 = floor(2)
    Floor_3 = floor(3)

    all_Floors = [Floor_1,Floor_2,Floor_3]
    return all_Floors
