import pprint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, random, datetime
from FloorClass import create_all_Floors
from CharactersClass import *
from CardsClass import dict_all_cards
from EventsClass import list_all_events, only_id_events, dict_all_events, dict_obj_all_events
from AartifactsClass import list_obj_all_artifacts, dict_all_artifacts

game_player = list_all_characters[0]
# print(game_player.NAME)
class Ui_Map(object):
    num_Floor = 0
    gold = 10

    EXP = 0

    actual_HP = game_player.MAX_HP
    actual_CE = game_player.MAX_CE

    deck = ["card_1","card_1","card_1","card_1","card_1",
            "card_2","card_2","card_2","card_2","card_2","card_3"]

    artifacts = []
    for PA_art in game_player.PA.split(";"):
        artifacts.append(PA_art)


    actual_pers_row = 0
    all_Floors = create_all_Floors()
    otmetka_rooms = []
    map_floor = []
    dict_Floor = {}

    def Main_map(self, MainWindow):
        print(self.actual_pers_row)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.map_btn_info = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_btn_info.sizePolicy().hasHeightForWidth())
        self.map_btn_info.setSizePolicy(sizePolicy)
        self.map_btn_info.setMinimumSize(QtCore.QSize(250, 0))
        self.map_btn_info.setObjectName("map_btn_info")
        self.gridLayout.addWidget(self.map_btn_info, 3, 14, 1, 1)
        self.map_exit_in_menu = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_exit_in_menu.sizePolicy().hasHeightForWidth())
        self.map_exit_in_menu.setSizePolicy(sizePolicy)
        self.map_exit_in_menu.setMinimumSize(QtCore.QSize(150, 0))
        self.map_exit_in_menu.setObjectName("map_exit_in_menu")
        self.gridLayout.addWidget(self.map_exit_in_menu, 3, 15, 1, 1)
        self.map_HP_CE = QtWidgets.QLabel(self.centralwidget)
        self.map_HP_CE.setObjectName("map_HP_CE")
        self.gridLayout.addWidget(self.map_HP_CE, 3, 13, 2, 1)
        self.map_gold = QtWidgets.QLabel(self.centralwidget)
        self.map_gold.setObjectName("map_gold")
        self.gridLayout.addWidget(self.map_gold, 3, 12, 2, 1)
        self.map_num_floor = QtWidgets.QLabel(self.centralwidget)
        self.map_num_floor.setObjectName("label")
        self.gridLayout.addWidget(self.map_num_floor, 4, 15, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.map = QtWidgets.QScrollArea(self.centralwidget)
        self.map.setWidgetResizable(True)
        self.map.setObjectName("map")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1260, 751))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        def create_map(num_Floor):
####create all buttons
            for i in self.all_Floors[num_Floor][0:13:]:
                for k in i:
                    if k == "Boss":
                        self.map_event_Boss = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                        self.map_event_Boss.setMinimumSize(QtCore.QSize(0, 150))
                        self.map_event_Boss.setObjectName("map_event_Boss")
                        self.gridLayout_2.addWidget(self.map_event_Boss, 12, 0, 1, 4)
                    elif k == "Start":
                        self.map_event_Start = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                        self.map_event_Start.setMinimumSize(QtCore.QSize(0, 150))
                        self.map_event_Start.setObjectName("map_event_Start")
                        self.gridLayout_2.addWidget(self.map_event_Start, 0, 0, 1, 4)
                    else:
                        exec(f"self.map_event_{k} = QtWidgets.QPushButton(self.scrollAreaWidgetContents)")
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        exec(f"sizePolicy.setHeightForWidth(self.map_event_{k}.sizePolicy().hasHeightForWidth())")
                        exec(f"self.map_event_{k}.setSizePolicy(sizePolicy)")
                        exec(f"self.map_event_{k}.setMinimumSize(QtCore.QSize(100, 100))")
                        exec(f"self.map_event_{k}.setObjectName('map_event_{k}')")

#####Название кнопок на карте
            for widget in self.scrollAreaWidgetContents.children():
                if isinstance(widget, QtWidgets.QPushButton):
                    if widget.objectName() == "map_event_Start":
                        exec(f"""self.{widget.objectName()}.setText(f"{dict_obj_all_events.get(f'event_{self.num_Floor+1}_start').name_event}")""")
                    elif widget.objectName() == "map_event_Boss":
                        exec(f"""self.{widget.objectName()}.setText(f"{dict_obj_all_events.get(f'event_{self.num_Floor + 1}_boss').name_event}")""")
                    elif widget.objectName().split("_")[2] == "Enemy":
                        exec(f"""self.{widget.objectName()}.setText(f"Враг")""")
                    elif widget.objectName().split("_")[2] == "Strong":
                        exec(f"""self.{widget.objectName()}.setText(f"Сильный Враг")""")
                    elif widget.objectName().split("_")[2] == "Event":
                        exec(f"""self.{widget.objectName()}.setText(f"Cобытие")""")
                    elif widget.objectName().split("_")[2] == "Shop":
                        exec(f"""self.{widget.objectName()}.setText(f"Магазин")""")
                    elif widget.objectName().split("_")[2] == "Rest":
                        exec(f"""self.{widget.objectName()}.setText(f"Отдых")""")

#####Расстановка ячеек по местам
            if len(self.dict_Floor) == 0:
                row = 0
                v_map_floor = []
                for i in self.all_Floors[num_Floor][1:12:]:
                    row+=1
                    column = list(range(4))
                    random.shuffle(column)
                    column_index=0
                    if v_map_floor != []:
                        self.map_floor.append(v_map_floor)
                        v_map_floor = []
                    for k in i:
                        exec(f"self.gridLayout_2.addWidget(self.map_event_{k}, {row}, {column[column_index]}, 1, 1)")
                        v_map_floor.append(f"map_event_{k}")

                        self.dict_Floor[f"map_event_{k}"] = [row, column[column_index], k]

                        column_index += 1
                self.map_floor.append(v_map_floor)
            elif len(self.dict_Floor) > 0:
                for widget in self.scrollAreaWidgetContents.children():
                    if isinstance(widget, QtWidgets.QPushButton):
                        if widget.objectName() == 'map_event_Start' or widget.objectName() == "map_event_Boss":
                            pass
                        else:
                            row_column_text = self.dict_Floor.get(widget.objectName(), 0)
                            self.gridLayout_2.addWidget(widget, row_column_text[0], row_column_text[1], 1, 1)
#####Создание обводки в ячейках которых ты был
            for widget in self.scrollAreaWidgetContents.children():
                if isinstance(widget, QtWidgets.QPushButton):
                    for otmetka in self.otmetka_rooms:
                        if widget.objectName() == otmetka:
                            widget.setStyleSheet("QWidget {"
                                 "border: 5px solid black;"
                                 "border-radius: 5px;"
                                 "}")

            self.map.setWidget(self.scrollAreaWidgetContents)
            self.gridLayout.addWidget(self.map, 5, 12, 1, 4)
            MainWindow.setCentralWidget(self.centralwidget)

            self.Main_map_retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        create_map(self.num_Floor)

        def change_event():
            button = MainWindow.sender()
            self.otmetka_rooms.append(button.objectName())
            button.setStyleSheet("QWidget {"
                                 "border: 5px solid black;"
                                 "border-radius: 5px;"
                                 "}")
####Создание ссылок на кнопках
            if button.objectName() == "map_event_Start":
                self.actual_pers_row = 0
                self.Event(MainWindow, button)
            elif button.objectName() == "map_event_Boss":
                self.Event(MainWindow, button)
                self.num_Floor += 1
                self.dict_Floor = {}
                self.otmetka_rooms = []
                self.map_floor = []
                self.actual_pers_row = 0

            elif button.objectName().split("_")[2] == "Enemy":
                self.Event(MainWindow, button)
            elif button.objectName().split("_")[2] == "Strong":
                self.Event(MainWindow, button)
            elif button.objectName().split("_")[2] == "Event":
                self.Event(MainWindow, button)
            elif button.objectName().split("_")[2] == "Shop":
                self.Shop(MainWindow)
            elif button.objectName().split("_")[2] == "Rest":
                self.Rest(MainWindow)

        def btn_enebled():
            all_button_widget = []
            for widget in self.scrollAreaWidgetContents.children():
                if isinstance(widget, QtWidgets.QPushButton):
                    widget.clicked.connect(change_event)
                    all_button_widget.append(widget)
                    widget.setEnabled(False)

            all_button_in_floor = []
            v_all_button_in_floor = []
            for map_fl in self.map_floor:
                if v_all_button_in_floor != []:
                    all_button_in_floor.append(v_all_button_in_floor)
                    v_all_button_in_floor = []
                for k in map_fl:
                    for button in all_button_widget:
                        if button.objectName() == k:
                            v_all_button_in_floor.append(button)
            all_button_in_floor.append(v_all_button_in_floor)
            all_button_in_floor.insert(0,[self.map_event_Start])
            all_button_in_floor.append([self.map_event_Boss])

            for widgets_on_floor in all_button_in_floor[0:self.actual_pers_row+1:]:
                for widget in widgets_on_floor:
                    widget.setEnabled(True)

            for widgets_on_floor in all_button_in_floor[0:self.actual_pers_row:]:
                for widget in widgets_on_floor:
                    widget.setEnabled(False)

        btn_enebled()

        self.map_btn_info.clicked.connect(lambda: self.Map_info(MainWindow))

    def Event(self, MainWindow, id_event_sender):
        self.actual_pers_row += 1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.event_centralwidget = QtWidgets.QWidget(MainWindow)
        self.event_centralwidget.setObjectName("event_centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.event_centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.event_name = QtWidgets.QLabel(self.event_centralwidget)
        self.event_name.setObjectName("event_name")
        self.gridLayout.addWidget(self.event_name, 1, 1, 1, 3)
        self.event_text = QtWidgets.QTextBrowser(self.event_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.event_text.sizePolicy().hasHeightForWidth())
        self.event_text.setSizePolicy(sizePolicy)
        self.event_text.setObjectName("event_text")
        self.gridLayout.addWidget(self.event_text, 2, 3, 1, 1)
        self.event_image = QtWidgets.QLabel(self.event_centralwidget)
        self.event_image.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.event_image.setText("")
        self.event_image.setObjectName("event_image")
        self.gridLayout.addWidget(self.event_image, 2, 1, 5, 2)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.event_centralwidget)

        ######Получение индекса кнопки, id награды евента и направление на получение награды
        ######Направление на изменение послеивентового текста и отображение кнопок
        def choice_result_event(text_continue):
            button = MainWindow.sender()
            try:
                index_btn = int(str(button.objectName())[-1])
                id_choice = text_answer[index_btn].split('|')[1].split(" ")[0]
                try:
                    kol_vo = int(text_answer[index_btn].split('|')[1].split(" ")[1])
                except:
                    kol_vo = text_answer[index_btn].split('|')[1].split(" ")[1]
                dict_functions[f"event_{id_choice}"](kol_vo, text_continue[index_btn])
                create_btn_exit_event()
            except:
                self.Main_map(MainWindow)

        def create_btn_exit_event():
            for btn_in_event in self.event_centralwidget.children():
                if isinstance(btn_in_event, QtWidgets.QPushButton):
                    btn_in_event.setVisible(False)

            self.event_btn_0 = QtWidgets.QPushButton(self.event_centralwidget)
            self.event_btn_0.setStyleSheet('font: 14pt \"MS Shell Dlg 2\";')
            self.event_btn_0.setObjectName('event_btn_0')
            self.gridLayout.addWidget(self.event_btn_0, 3, 3, 4, 1)
            self.event_btn_0.setText("Уйти")
            self.event_btn_0.clicked.connect(lambda: self.Main_map(MainWindow))


        ############GET#############
        def event_get_HP(kol_vo):
            self.actual_HP += kol_vo
            if self.actual_HP > game_player.MAX_HP:
                self.actual_HP = game_player.MAX_HP

        def event_get_CE(kol_vo):
            self.actual_CE += kol_vo
            if self.actual_CE > game_player.MAX_CE:
                self.actual_CE = game_player.MAX_CE

        def event_get_gold(kol_vo):
            self.gold += kol_vo

        def event_get_card(card, text_continue):
            self.deck.append(card)

            text_exit_event = f"{text_continue}  Вы добавили в свою колоду карту: {dict_all_cards.get(card).name}"
            self.Event_retranslateUi(MainWindow, text_event=text_exit_event)

        def event_get_artifact(artifact):
            self.artifacts.append(artifact)

        ############INCREASE#############
        def event_increase_random_parametr(kol_vo, text_continue):
            d_all = {"STR":"Сила","DEX":"Ловкость","CON":"Телосложение",
                     "INT":"Интеллект","WIZ":"Мудрость","CHA":"Харизма"}
            all = ["STR","DEX","CON","INT","WIZ","CHA"]
            random.shuffle(all)
            dict_functions[f"event_increase_{all[0]}"](kol_vo)

            text_exit_event = f"{text_continue}  Вы увеличили характеристику {d_all[all[0]]} на {kol_vo}"
            self.Event_retranslateUi(MainWindow, text_event=text_exit_event)

        def event_increase_LVL():
            game_player.lvlup(game_player.LVL+1)

        def event_increase_MAX_HP(kol_vo, text_continue):
            game_player.MAX_HP += kol_vo
            if game_player.MAX_HP < self.actual_HP:
                self.actual_HP = game_player.MAX_HP

            text_exit_event = f"{text_continue}  Вы увеличили максимальное здоровье на {kol_vo}"
            self.Event_retranslateUi(MainWindow, text_event = text_exit_event)

        def event_increase_MAX_CE(kol_vo):
            game_player.MAX_CE += kol_vo

        def event_increase_MAX_EN(kol_vo):
            game_player.MAX_EN += kol_vo

        def event_increase_STR(kol_vo):
            game_player.STR += kol_vo

        def event_increase_DEX(kol_vo):
            game_player.DEX += kol_vo

        def event_increase_CON(kol_vo):
            game_player.CON += kol_vo

        def event_increase_INT(kol_vo):
            game_player.INT += kol_vo

        def event_increase_WIZ(kol_vo):
            game_player.WIZ += kol_vo

        def event_increase_CHA(kol_vo):
            game_player.CHA += kol_vo

        ######Словарь функций
        dict_functions = {"event_get_HP": event_get_HP, "event_get_CE": event_get_CE, "event_get_gold":event_get_gold,
                          "event_get_card":event_get_card,"event_get_artifact":event_get_artifact,
                          "event_increase_random_parametr":event_increase_random_parametr,
                          "event_increase_LVL":event_increase_LVL, "event_increase_MAX_HP":event_increase_MAX_HP,
                          "event_increase_MAX_CE":event_increase_MAX_CE, "event_increase_MAX_EN":event_increase_MAX_EN,
                          "event_increase_STR":event_increase_STR, "event_increase_DEX":event_increase_DEX,
                          "event_increase_CON":event_increase_CON, "event_increase_INT":event_increase_INT,
                          "event_increase_WIZ":event_increase_WIZ, "event_increase_CHA":event_increase_CHA}
        random.shuffle(only_id_events)

        ########Извлечение данных евента из класса
        def create_event():
            global name_event, text_event, count_answer, text_answer

            if id_event_sender.objectName().split("_")[2] == "Start":
                name_event = dict_obj_all_events.get(f"event_{self.num_Floor+1}_start").name_event
                text_event = dict_obj_all_events.get(f"event_{self.num_Floor+1}_start").text_event
                count_answer = dict_obj_all_events.get(f"event_{self.num_Floor+1}_start").count_answer
                text_answer = dict_obj_all_events.get(f"event_{self.num_Floor+1}_start").text_answer.split("/")
                text_continue = dict_obj_all_events.get(f"event_{self.num_Floor+1}_start").text_continue.split("/")
            else:
                id_event = only_id_events.pop(0)
                name_event = dict_obj_all_events.get(f"{id_event}").name_event
                text_event = dict_obj_all_events.get(f"{id_event}").text_event
                count_answer = dict_obj_all_events.get(f"{id_event}").count_answer
                text_answer = dict_obj_all_events.get(f"{id_event}").text_answer.split("/")
                text_continue = dict_obj_all_events.get(f"event_{self.num_Floor + 1}_start").text_continue.split("/")

            for create_btn in range(count_answer):
                exec(f"self.event_btn_{create_btn} = QtWidgets.QPushButton(self.event_centralwidget)")
                exec(f"self.event_btn_{create_btn}.setStyleSheet('font: 14pt \"MS Shell Dlg 2\";')")
                exec(f"self.event_btn_{create_btn}.setObjectName('event_btn_{create_btn}')")
                exec(f"self.gridLayout.addWidget(self.event_btn_{create_btn}, {create_btn + 3}, 3, 1, 1)")

            for e,text_in_answer in enumerate(text_answer):
                exec(f"self.event_btn_{e}.setText(f'{text_answer[e].split('|')[0]}')")

            for btn_in_event in self.event_centralwidget.children():
                if isinstance(btn_in_event, QtWidgets.QPushButton):
                    btn_in_event.clicked.connect(lambda: choice_result_event(text_continue))

        create_event()

        self.Event_retranslateUi(MainWindow, name_event = name_event, text_event = text_event)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Rest(self, MainWindow):
        self.actual_pers_row += 1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.rest_centralwidget = QtWidgets.QWidget(MainWindow)
        self.rest_centralwidget.setObjectName("rest_centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.rest_centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.rest_frame_image = QtWidgets.QFrame(self.rest_centralwidget)
        self.rest_frame_image.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.rest_frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rest_frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rest_frame_image.setObjectName("rest_frame_image")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rest_frame_image)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.rest_btn_rest = QtWidgets.QPushButton(self.rest_frame_image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest_btn_rest.sizePolicy().hasHeightForWidth())
        self.rest_btn_rest.setSizePolicy(sizePolicy)
        self.rest_btn_rest.setMinimumSize(QtCore.QSize(200, 50))
        self.rest_btn_rest.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 14pt \"MS Shell Dlg 2\";")
        self.rest_btn_rest.setObjectName("rest_btn_rest")
        self.gridLayout_2.addWidget(self.rest_btn_rest, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        self.rest_btn_upgrade = QtWidgets.QPushButton(self.rest_frame_image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest_btn_upgrade.sizePolicy().hasHeightForWidth())
        self.rest_btn_upgrade.setSizePolicy(sizePolicy)
        self.rest_btn_upgrade.setMinimumSize(QtCore.QSize(200, 50))
        self.rest_btn_upgrade.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"MS Shell Dlg 2\";")
        self.rest_btn_upgrade.setObjectName("rest_btn_upgrade")
        self.gridLayout_2.addWidget(self.rest_btn_upgrade, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.rest_frame_image, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem7, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.rest_centralwidget)

        self.Rest_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def rest_heal():
            self.actual_HP += game_player.MAX_HP//3
            if self.actual_HP > game_player.MAX_HP:
                self.actual_HP = game_player.MAX_HP

        self.rest_btn_rest.clicked.connect(rest_heal)
        for btn_in_event in self.rest_frame_image.children():
            if isinstance(btn_in_event, QtWidgets.QPushButton):
                btn_in_event.clicked.connect(lambda: self.Main_map(MainWindow))

    def Shop(self, MainWindow):
        self.actual_pers_row += 1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.shop_centralwidget = QtWidgets.QWidget(MainWindow)
        self.shop_centralwidget.setObjectName("shop_centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.shop_centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.shop_frame_image = QtWidgets.QFrame(self.shop_centralwidget)
        self.shop_frame_image.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.shop_frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shop_frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shop_frame_image.setObjectName("shop_frame_image")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.shop_frame_image)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.shop_gold = QtWidgets.QLabel(self.shop_frame_image)
        self.shop_gold.setMinimumSize(QtCore.QSize(150, 0))
        self.shop_gold.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 14pt \"MS Shell Dlg 2\";")
        self.shop_gold.setObjectName("shop_gold")
        self.gridLayout_2.addWidget(self.shop_gold, 2, 2, 1, 1)

        self.shop_groupBox_artefacts = QtWidgets.QGroupBox(self.shop_frame_image)
        self.shop_groupBox_artefacts.setObjectName("shop_groupBox_artefacts")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.shop_groupBox_artefacts)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.shop_artefact_1 = QtWidgets.QPushButton(self.shop_groupBox_artefacts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_artefact_1.sizePolicy().hasHeightForWidth())

        self.shop_artefact_1.setSizePolicy(sizePolicy)
        self.shop_artefact_1.setMinimumSize(QtCore.QSize(230, 230))
        self.shop_artefact_1.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_artefact_1.setObjectName("shop_artefact_1")
        self.gridLayout_4.addWidget(self.shop_artefact_1, 0, 0, 1, 1)
        self.shop_artefact_2 = QtWidgets.QPushButton(self.shop_groupBox_artefacts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_artefact_2.sizePolicy().hasHeightForWidth())
        self.shop_artefact_2.setSizePolicy(sizePolicy)
        self.shop_artefact_2.setMinimumSize(QtCore.QSize(230, 230))
        self.shop_artefact_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_artefact_2.setObjectName("shop_artefact_2")
        self.gridLayout_4.addWidget(self.shop_artefact_2, 0, 1, 1, 1)
        self.shop_artefact_3 = QtWidgets.QPushButton(self.shop_groupBox_artefacts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_artefact_3.sizePolicy().hasHeightForWidth())
        self.shop_artefact_3.setSizePolicy(sizePolicy)
        self.shop_artefact_3.setMinimumSize(QtCore.QSize(230, 230))
        self.shop_artefact_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_artefact_3.setObjectName("shop_artefact_3")
        self.gridLayout_4.addWidget(self.shop_artefact_3, 0, 2, 1, 1)

        self.shop_artefact_price_1 = QtWidgets.QLabel(self.shop_groupBox_artefacts)
        self.shop_artefact_price_1.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_artefact_price_1.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_artefact_price_1.setObjectName("shop_artefact_price_1")
        self.gridLayout_4.addWidget(self.shop_artefact_price_1, 1, 0, 1, 1)
        self.shop_artefact_price_2 = QtWidgets.QLabel(self.shop_groupBox_artefacts)
        self.shop_artefact_price_2.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_artefact_price_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_artefact_price_2.setObjectName("shop_artefact_price_2")
        self.gridLayout_4.addWidget(self.shop_artefact_price_2, 1, 1, 1, 1)
        self.shop_artefact_price_3 = QtWidgets.QLabel(self.shop_groupBox_artefacts)
        self.shop_artefact_price_3.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_artefact_price_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_artefact_price_3.setObjectName("shop_artefact_price_3")
        self.gridLayout_4.addWidget(self.shop_artefact_price_3, 1, 2, 1, 1)

        self.gridLayout_2.addWidget(self.shop_groupBox_artefacts, 1, 0, 1, 4)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.shop_btn_delete_card = QtWidgets.QPushButton(self.shop_frame_image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_btn_delete_card.sizePolicy().hasHeightForWidth())
        self.shop_btn_delete_card.setSizePolicy(sizePolicy)
        self.shop_btn_delete_card.setMinimumSize(QtCore.QSize(200, 250))
        self.shop_btn_delete_card.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 14pt \"MS Shell Dlg 2\";")
        self.shop_btn_delete_card.setObjectName("shop_btn_delete_card")
        self.gridLayout_2.addWidget(self.shop_btn_delete_card, 1, 4, 1, 1)

        self.shop_groupBox_cards = QtWidgets.QGroupBox(self.shop_frame_image)
        self.shop_groupBox_cards.setObjectName("shop_groupBox_cards")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.shop_groupBox_cards)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.shop_card_1 = QtWidgets.QPushButton(self.shop_groupBox_cards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_card_1.sizePolicy().hasHeightForWidth())
        self.shop_card_1.setSizePolicy(sizePolicy)
        self.shop_card_1.setMinimumSize(QtCore.QSize(130, 230))
        self.shop_card_1.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_1.setObjectName("shop_card_1")
        self.gridLayout_3.addWidget(self.shop_card_1, 0, 0, 1, 1)
        self.shop_card_2 = QtWidgets.QPushButton(self.shop_groupBox_cards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_card_2.sizePolicy().hasHeightForWidth())
        self.shop_card_2.setSizePolicy(sizePolicy)
        self.shop_card_2.setMinimumSize(QtCore.QSize(130, 230))
        self.shop_card_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_2.setObjectName("shop_card_2")
        self.gridLayout_3.addWidget(self.shop_card_2, 0, 1, 1, 1)
        self.shop_card_3 = QtWidgets.QPushButton(self.shop_groupBox_cards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_card_3.sizePolicy().hasHeightForWidth())
        self.shop_card_3.setSizePolicy(sizePolicy)
        self.shop_card_3.setMinimumSize(QtCore.QSize(130, 230))
        self.shop_card_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_3.setObjectName("shop_card_3")
        self.gridLayout_3.addWidget(self.shop_card_3, 0, 2, 1, 1)
        self.shop_card_4 = QtWidgets.QPushButton(self.shop_groupBox_cards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_card_4.sizePolicy().hasHeightForWidth())
        self.shop_card_4.setSizePolicy(sizePolicy)
        self.shop_card_4.setMinimumSize(QtCore.QSize(130, 230))
        self.shop_card_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_4.setObjectName("shop_card_4")
        self.gridLayout_3.addWidget(self.shop_card_4, 0, 3, 1, 1)
        self.shop_card_5 = QtWidgets.QPushButton(self.shop_groupBox_cards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_card_5.sizePolicy().hasHeightForWidth())
        self.shop_card_5.setSizePolicy(sizePolicy)
        self.shop_card_5.setMinimumSize(QtCore.QSize(130, 230))
        self.shop_card_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_5.setObjectName("shop_card_5")
        self.gridLayout_3.addWidget(self.shop_card_5, 0, 4, 1, 1)
        self.shop_card_6 = QtWidgets.QPushButton(self.shop_groupBox_cards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_card_6.sizePolicy().hasHeightForWidth())
        self.shop_card_6.setSizePolicy(sizePolicy)
        self.shop_card_6.setMinimumSize(QtCore.QSize(130, 230))
        self.shop_card_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_6.setObjectName("shop_card_6")
        self.gridLayout_3.addWidget(self.shop_card_6, 0, 5, 1, 1)
        self.shop_card_price_1 = QtWidgets.QLabel(self.shop_groupBox_cards)
        self.shop_card_price_1.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_card_price_1.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_price_1.setObjectName("shop_card_price_1")
        self.gridLayout_3.addWidget(self.shop_card_price_1, 1, 0, 1, 1)
        self.shop_card_price_2 = QtWidgets.QLabel(self.shop_groupBox_cards)
        self.shop_card_price_2.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_card_price_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_price_2.setObjectName("shop_card_price_2")
        self.gridLayout_3.addWidget(self.shop_card_price_2, 1, 1, 1, 1)
        self.shop_card_price_3 = QtWidgets.QLabel(self.shop_groupBox_cards)
        self.shop_card_price_3.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_card_price_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_price_3.setObjectName("shop_card_price_3")
        self.gridLayout_3.addWidget(self.shop_card_price_3, 1, 2, 1, 1)
        self.shop_card_price_4 = QtWidgets.QLabel(self.shop_groupBox_cards)
        self.shop_card_price_4.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_card_price_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_price_4.setObjectName("shop_card_price_4")
        self.gridLayout_3.addWidget(self.shop_card_price_4, 1, 3, 1, 1)
        self.shop_card_price_5 = QtWidgets.QLabel(self.shop_groupBox_cards)
        self.shop_card_price_5.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_card_price_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_price_5.setObjectName("shop_card_price_5")
        self.gridLayout_3.addWidget(self.shop_card_price_5, 1, 4, 1, 1)
        self.shop_card_price_6 = QtWidgets.QLabel(self.shop_groupBox_cards)
        self.shop_card_price_6.setMinimumSize(QtCore.QSize(50, 20))
        self.shop_card_price_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.shop_card_price_6.setObjectName("shop_card_price_6")
        self.gridLayout_3.addWidget(self.shop_card_price_6, 1, 5, 1, 1)

        self.gridLayout_2.addWidget(self.shop_groupBox_cards, 0, 0, 1, 5)

        self.shop_btn_exit = QtWidgets.QPushButton(self.shop_frame_image)
        self.shop_btn_exit.setMinimumSize(QtCore.QSize(200, 0))
        self.shop_btn_exit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 14pt \"MS Shell Dlg 2\";")
        self.shop_btn_exit.setObjectName("shop_btn_exit")
        self.gridLayout_2.addWidget(self.shop_btn_exit, 2, 4, 1, 1)
        self.gridLayout.addWidget(self.shop_frame_image, 1, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.shop_centralwidget)

        self.Shop_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.shop_btn_exit.clicked.connect(lambda: self.Main_map(MainWindow))

        def shopping_card():
            button = MainWindow.sender()
            if  self.gold < 10:
                pass
            else:
                print(button)
                self.gold -= 10
                self.shop_gold.setText(f" Золото: {self.gold}")
                button.setEnabled(False)

        def shopping_artefact():
            button = MainWindow.sender()
            if self.gold < 100:
                pass
            else:
                self.gold -= 100
                self.shop_gold.setText(f" Золото: {self.gold}")
                button.setEnabled(False)

        for btn in self.shop_groupBox_cards.children():
            if isinstance(btn, QtWidgets.QPushButton):
                btn.clicked.connect(shopping_card)
        for btn in self.shop_groupBox_artefacts.children():
            if isinstance(btn, QtWidgets.QPushButton):
                btn.clicked.connect(shopping_artefact)

    def Map_info(self, MainWindow):
        self.map_info_centralwidget = QtWidgets.QWidget(MainWindow)
        self.map_info_centralwidget.setObjectName("map_info_centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.map_info_centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.map_info_abilites = QtWidgets.QLabel(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_abilites.sizePolicy().hasHeightForWidth())
        self.map_info_abilites.setSizePolicy(sizePolicy)
        self.map_info_abilites.setMinimumSize(QtCore.QSize(330, 50))
        self.map_info_abilites.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.map_info_abilites.setObjectName("map_info_abilites")
        self.gridLayout.addWidget(self.map_info_abilites, 3, 1, 1, 1)
        self.map_info_text_abilities = QtWidgets.QTextBrowser(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_text_abilities.sizePolicy().hasHeightForWidth())
        self.map_info_text_abilities.setSizePolicy(sizePolicy)
        self.map_info_text_abilities.setMinimumSize(QtCore.QSize(300, 0))
        self.map_info_text_abilities.setObjectName("map_info_text_abilities")
        self.gridLayout.addWidget(self.map_info_text_abilities, 4, 1, 2, 1)
        self.map_info_artefacts_scrollArea = QtWidgets.QScrollArea(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_artefacts_scrollArea.sizePolicy().hasHeightForWidth())
        self.map_info_artefacts_scrollArea.setSizePolicy(sizePolicy)
        self.map_info_artefacts_scrollArea.setWidgetResizable(True)
        self.map_info_artefacts_scrollArea.setObjectName("map_info_artefacts_scrollArea")
        self.map_info_artefacts_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.map_info_artefacts_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 438, 118))
        self.map_info_artefacts_scrollAreaWidgetContents.setObjectName(
            "map_info_artefacts_scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.map_info_artefacts_scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        #####Создание отображения артефактов
        for num_art, art in enumerate(self.artifacts):
            exec(f"self.map_info_artefact_{num_art} = QtWidgets.QLabel(self.map_info_artefacts_scrollAreaWidgetContents)")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            exec(f"sizePolicy.setHeightForWidth(self.map_info_artefact_{num_art}.sizePolicy().hasHeightForWidth())")
            exec(f"self.map_info_artefact_{num_art}.setSizePolicy(sizePolicy)")
            exec(f"self.map_info_artefact_{num_art}.setMinimumSize(QtCore.QSize(100, 100))")
            exec(f"self.map_info_artefact_{num_art}.setObjectName('map_info_artefact_{num_art}')")
            exec(f"self.map_info_artefact_{num_art}.setToolTip('{dict_all_artifacts.get(art).text_art}')")
            exec(f"self.gridLayout_3.addWidget(self.map_info_artefact_{num_art}, 0, {num_art}, 1, 1)")
            x = "{}"
            QToolTip.setFont(QFont('Georgia', 11))
            exec(f"self.map_info_artefact_{num_art}.setStyleSheet('QToolTip {x[0]} background-color: #c4c4c4;"
                 f" color: black;"
                 f" border: #8ad4ff solid 1px {x[1]}"
                 f"QLabel {x[0]} background-color: rgb(173, 173, 173) {x[1]}') ")


        self.map_info_artefacts_scrollArea.setWidget(self.map_info_artefacts_scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.map_info_artefacts_scrollArea, 4, 0, 2, 1)

        self.map_info_pers_name = QtWidgets.QLabel(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_pers_name.sizePolicy().hasHeightForWidth())
        self.map_info_pers_name.setSizePolicy(sizePolicy)
        self.map_info_pers_name.setMinimumSize(QtCore.QSize(330, 50))
        self.map_info_pers_name.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.map_info_pers_name.setObjectName("map_info_pers_name")
        self.gridLayout.addWidget(self.map_info_pers_name, 0, 1, 1, 1)
        self.map_info_image = QtWidgets.QLabel(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_image.sizePolicy().hasHeightForWidth())
        self.map_info_image.setSizePolicy(sizePolicy)
        self.map_info_image.setMinimumSize(QtCore.QSize(400, 600))
        self.map_info_image.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.map_info_image.setText("")
        self.map_info_image.setObjectName("map_info_image")
        self.gridLayout.addWidget(self.map_info_image, 0, 3, 3, 1)
        self.map_info_btn_cards = QtWidgets.QPushButton(self.map_info_centralwidget)
        self.map_info_btn_cards.setMinimumSize(QtCore.QSize(0, 50))
        self.map_info_btn_cards.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.map_info_btn_cards.setObjectName("map_info_btn_cards")
        self.gridLayout.addWidget(self.map_info_btn_cards, 0, 0, 1, 1)
        self.map_info_text_parameters = QtWidgets.QTextBrowser(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_text_parameters.sizePolicy().hasHeightForWidth())
        self.map_info_text_parameters.setSizePolicy(sizePolicy)
        self.map_info_text_parameters.setMinimumSize(QtCore.QSize(300, 0))
        self.map_info_text_parameters.setObjectName("map_info_text_parameters")
        self.gridLayout.addWidget(self.map_info_text_parameters, 2, 1, 1, 1)
        self.map_info_text_info_pers = QtWidgets.QTextBrowser(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_text_info_pers.sizePolicy().hasHeightForWidth())
        self.map_info_text_info_pers.setSizePolicy(sizePolicy)
        self.map_info_text_info_pers.setMinimumSize(QtCore.QSize(300, 0))
        self.map_info_text_info_pers.setObjectName("map_info_text_info_pers")
        self.gridLayout.addWidget(self.map_info_text_info_pers, 1, 1, 1, 1)
        self.map_info_exp = QtWidgets.QLabel(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_exp.sizePolicy().hasHeightForWidth())
        self.map_info_exp.setSizePolicy(sizePolicy)
        self.map_info_exp.setMinimumSize(QtCore.QSize(330, 50))
        self.map_info_exp.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.map_info_exp.setObjectName("map_info_exp")
        self.gridLayout.addWidget(self.map_info_exp, 3, 3, 1, 1)

        self.map_info_cards_scrollArea = QtWidgets.QScrollArea(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_cards_scrollArea.sizePolicy().hasHeightForWidth())
        self.map_info_cards_scrollArea.setSizePolicy(sizePolicy)
        self.map_info_cards_scrollArea.setWidgetResizable(True)
        self.map_info_cards_scrollArea.setObjectName("map_info_cards_scrollArea")
        self.map_info_cards_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.map_info_cards_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 540, 624))
        self.map_info_cards_scrollAreaWidgetContents.setObjectName("map_info_cards_scrollAreaWidgetContents")
        self.gridLayout_all_cards = QtWidgets.QGridLayout(self.map_info_cards_scrollAreaWidgetContents)
        self.gridLayout_all_cards.setObjectName("gridLayout_all_cards")

        ######Создание отображения карт
        self.deck.sort()

        for num_card_in_deck, id_card in enumerate(self.deck, 1):
            exec(f"self.card_{num_card_in_deck} = QtWidgets.QFrame(self.map_info_cards_scrollAreaWidgetContents)")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            exec(f"sizePolicy.setHeightForWidth(self.card_{num_card_in_deck}.sizePolicy().hasHeightForWidth())")
            exec(f"self.card_{num_card_in_deck}.setSizePolicy(sizePolicy)")
            exec(f"self.card_{num_card_in_deck}.setMinimumSize(QtCore.QSize(170, 300))")
            exec(f"self.card_{num_card_in_deck}.setMaximumSize(QtCore.QSize(170, 300))")
            exec(f"self.card_{num_card_in_deck}.setStyleSheet('background-color: rgb(180, 180, 180);')")
            exec(f"self.card_{num_card_in_deck}.setFrameShape(QtWidgets.QFrame.StyledPanel)")
            exec(f"self.card_{num_card_in_deck}.setFrameShadow(QtWidgets.QFrame.Raised)")
            exec(f"self.card_{num_card_in_deck}.setObjectName('card_{num_card_in_deck}')")
            exec(f"self.gridLayout_card_{num_card_in_deck} = QtWidgets.QGridLayout(self.card_{num_card_in_deck})")
            exec(f"self.gridLayout_card_{num_card_in_deck}.setObjectName('gridLayout_card_{num_card_in_deck}')")


        for num_card,card_frame in enumerate(self.map_info_cards_scrollAreaWidgetContents.children(),1):
            if isinstance(card_frame, QtWidgets.QFrame):

                exec(f"self.card_cost_{num_card-1} = QtWidgets.QLabel(self.card_{num_card-1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_cost_{num_card-1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_cost_{num_card-1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_cost_{num_card-1}.setStyleSheet('font: 75 12pt \"MS Shell Dlg 2\";')")
                exec(f"self.card_cost_{num_card-1}.setObjectName('card_cost_{num_card-1}')")
                exec(f"self.gridLayout_card_{num_card-1}.addWidget(self.card_cost_{num_card-1}, 0, 0, 1, 1)")

                exec(f"self.card_image_{num_card-1} = QtWidgets.QLabel(self.card_{num_card-1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_image_{num_card-1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_image_{num_card-1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_image_{num_card-1}.setMinimumSize(QtCore.QSize(150, 180))")
                exec(f"self.card_image_{num_card-1}.setStyleSheet('background-color: rgb(255, 255, 255);')")
                exec(f"self.card_image_{num_card-1}.setText('')")
                exec(f"self.card_image_{num_card-1}.setObjectName('card_image_{num_card-1}')")
                exec(f"self.gridLayout_card_{num_card-1}.addWidget(self.card_image_{num_card-1}, 1, 0, 1, 6)")

                exec(f"self.card_text_{num_card-1} = QtWidgets.QTextBrowser(self.card_{num_card-1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_text_{num_card-1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_text_{num_card-1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_text_{num_card-1}.setMinimumSize(QtCore.QSize(150, 20))")
                exec(f"self.card_text_{num_card-1}.setStyleSheet('background-color: rgb(231, 231, 231);')")
                exec(f"self.card_text_{num_card-1}.setObjectName('card_text_{num_card-1}')")
                exec(f"self.gridLayout_card_{num_card-1}.addWidget(self.card_text_{num_card-1}, 2, 0, 1, 1)")

                exec(f"self.card_name_{num_card-1} = QtWidgets.QLabel(self.card_{num_card-1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_name_{num_card-1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_name_{num_card-1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_name_{num_card-1}.setObjectName('card_name_{num_card-1}')")
                exec(f"self.gridLayout_card_{num_card-1}.addWidget(self.card_name_{num_card-1}, 0, 1, 1, 3)")

        ####Расположение карт
        column_card = 0
        row_card = 0
        id_card = self.deck[0]
        for card_obj in self.map_info_cards_scrollAreaWidgetContents.children():
            if isinstance(card_obj, QtWidgets.QFrame):
                id_card = card_obj.objectName()
                break

        for e,card in enumerate(self.deck, 1):
            if card == id_card:
                exec(f"self.gridLayout_all_cards.addWidget(self.card_{e}, {row_card}, {column_card}, 1, 1)")
                column_card += 1
            else:
                column_card = 0
                row_card += 1
                id_card = card
                exec(f"self.gridLayout_all_cards.addWidget(self.card_{e}, {row_card}, {column_card}, 1, 1)")
                column_card += 1

        self.map_info_cards_scrollArea.setWidget(self.map_info_cards_scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.map_info_cards_scrollArea, 1, 0, 2, 1)

        self.map_info_exp_progressBar = QtWidgets.QProgressBar(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_exp_progressBar.sizePolicy().hasHeightForWidth())
        self.map_info_exp_progressBar.setSizePolicy(sizePolicy)
        self.map_info_exp_progressBar.setProperty("value", 24)
        self.map_info_exp_progressBar.setObjectName("map_info_exp_progressBar")
        self.gridLayout.addWidget(self.map_info_exp_progressBar, 4, 3, 1, 1)
        self.map_info_btn_artefacts = QtWidgets.QPushButton(self.map_info_centralwidget)
        self.map_info_btn_artefacts.setMinimumSize(QtCore.QSize(0, 50))
        self.map_info_btn_artefacts.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.map_info_btn_artefacts.setObjectName("map_info_btn_artefacts")
        self.gridLayout.addWidget(self.map_info_btn_artefacts, 3, 0, 1, 1)
        self.map_info_btn_return_map = QtWidgets.QPushButton(self.map_info_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_info_btn_return_map.sizePolicy().hasHeightForWidth())
        self.map_info_btn_return_map.setSizePolicy(sizePolicy)
        self.map_info_btn_return_map.setMinimumSize(QtCore.QSize(300, 0))
        self.map_info_btn_return_map.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.map_info_btn_return_map.setObjectName("map_info__btn_return_map")
        self.gridLayout.addWidget(self.map_info_btn_return_map, 5, 3, 1, 1)
        MainWindow.setCentralWidget(self.map_info_centralwidget)

        self.Map_info_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def create_image():
            self.pix = QtGui.QPixmap(f"Data/CharactersFoto/{game_player.ID}.png")
            self.pix1 = self.pix.scaled(600, 600, QtCore.Qt.KeepAspectRatio)
            self.map_info_image.setPixmap(self.pix1)
        create_image()

        self.map_info_btn_return_map.clicked.connect(lambda: self.Main_map(MainWindow))
        self.map_info_btn_cards.clicked.connect(lambda: self.Map_info_deck(MainWindow) )

    def Map_info_deck(self, MainWindow):

        self.all_deck_centralwidget = QtWidgets.QWidget(MainWindow)
        self.all_deck_centralwidget.setObjectName("all_deck_centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.all_deck_centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.all_deck_btn_exit = QtWidgets.QPushButton(self.all_deck_centralwidget)
        self.all_deck_btn_exit.setMinimumSize(QtCore.QSize(170, 50))
        self.all_deck_btn_exit.setObjectName("all_deck_btn_exit")
        self.gridLayout.addWidget(self.all_deck_btn_exit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.all_deck_cards_scrollArea = QtWidgets.QScrollArea(self.all_deck_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_deck_cards_scrollArea.sizePolicy().hasHeightForWidth())
        self.all_deck_cards_scrollArea.setSizePolicy(sizePolicy)
        self.all_deck_cards_scrollArea.setWidgetResizable(True)
        self.all_deck_cards_scrollArea.setObjectName("all_deck_cards_scrollArea")
        self.all_deck_cards_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.all_deck_cards_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1180, 724))
        self.all_deck_cards_scrollAreaWidgetContents.setObjectName("all_deck_cards_scrollAreaWidgetContents")
        self.gridLayout_all_cards = QtWidgets.QGridLayout(self.all_deck_cards_scrollAreaWidgetContents)
        self.gridLayout_all_cards.setContentsMargins(9, -1, -1, 9)
        self.gridLayout_all_cards.setHorizontalSpacing(6)
        self.gridLayout_all_cards.setVerticalSpacing(60)
        self.gridLayout_all_cards.setObjectName("gridLayout_all_cards")

        self.deck.sort()

        for num_card_in_deck, id_card in enumerate(self.deck, 1):
            exec(f"self.card_{num_card_in_deck} = QtWidgets.QFrame(self.all_deck_cards_scrollAreaWidgetContents)")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            exec(f"sizePolicy.setHeightForWidth(self.card_{num_card_in_deck}.sizePolicy().hasHeightForWidth())")
            exec(f"self.card_{num_card_in_deck}.setSizePolicy(sizePolicy)")
            exec(f"self.card_{num_card_in_deck}.setMinimumSize(QtCore.QSize(250, 440))")
            exec(f"self.card_{num_card_in_deck}.setMaximumSize(QtCore.QSize(170, 300))")
            exec(f"self.card_{num_card_in_deck}.setStyleSheet('background-color: rgb(180, 180, 180);')")
            exec(f"self.card_{num_card_in_deck}.setFrameShape(QtWidgets.QFrame.StyledPanel)")
            exec(f"self.card_{num_card_in_deck}.setFrameShadow(QtWidgets.QFrame.Raised)")
            exec(f"self.card_{num_card_in_deck}.setObjectName('card_{num_card_in_deck}')")
            exec(f"self.gridLayout_card_{num_card_in_deck} = QtWidgets.QGridLayout(self.card_{num_card_in_deck})")
            exec(f"self.gridLayout_card_{num_card_in_deck}.setObjectName('gridLayout_card_{num_card_in_deck}')")

        for num_card, card_frame in enumerate(self.all_deck_cards_scrollAreaWidgetContents.children(), 1):
            if isinstance(card_frame, QtWidgets.QFrame):
                exec(f"self.card_cost_{num_card - 1} = QtWidgets.QLabel(self.card_{num_card - 1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_cost_{num_card - 1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_cost_{num_card - 1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_cost_{num_card - 1}.setStyleSheet('font: 75 12pt \"MS Shell Dlg 2\";')")
                exec(f"self.card_cost_{num_card - 1}.setObjectName('card_cost_{num_card - 1}')")
                exec(f"self.gridLayout_card_{num_card - 1}.addWidget(self.card_cost_{num_card - 1}, 0, 0, 1, 1)")

                exec(f"self.card_image_{num_card - 1} = QtWidgets.QLabel(self.card_{num_card - 1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_image_{num_card - 1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_image_{num_card - 1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_image_{num_card - 1}.setMinimumSize(QtCore.QSize(210, 180))")
                exec(f"self.card_image_{num_card - 1}.setStyleSheet('background-color: rgb(255, 255, 255);')")
                exec(f"self.card_image_{num_card - 1}.setText('')")
                exec(f"self.card_image_{num_card - 1}.setObjectName('card_image_{num_card - 1}')")
                exec(f"self.gridLayout_card_{num_card - 1}.addWidget(self.card_image_{num_card - 1}, 1, 0, 1, 6)")

                exec(f"self.card_text_{num_card - 1} = QtWidgets.QTextBrowser(self.card_{num_card - 1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_text_{num_card - 1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_text_{num_card - 1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_text_{num_card - 1}.setMinimumSize(QtCore.QSize(20, 20))")
                exec(f"self.card_text_{num_card - 1}.setStyleSheet('background-color: rgb(231, 231, 231);')")
                exec(f"self.card_text_{num_card - 1}.setObjectName('card_text_{num_card - 1}')")
                exec(f"self.gridLayout_card_{num_card - 1}.addWidget(self.card_text_{num_card - 1}, 2, 0, 1, 6)")

                exec(f"self.card_name_{num_card - 1} = QtWidgets.QLabel(self.card_{num_card - 1})")
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                exec(f"sizePolicy.setHeightForWidth(self.card_name_{num_card - 1}.sizePolicy().hasHeightForWidth())")
                exec(f"self.card_name_{num_card - 1}.setSizePolicy(sizePolicy)")
                exec(f"self.card_name_{num_card - 1}.setObjectName('card_name_{num_card - 1}')")
                exec(f"self.gridLayout_card_{num_card - 1}.addWidget(self.card_name_{num_card - 1}, 0, 1, 1, 3)")

        column_card = 0
        row_card = 0

        for e, card in enumerate(self.deck, 1):
            exec(f"self.gridLayout_all_cards.addWidget(self.card_{e}, {row_card}, {column_card}, 1, 1)")
            column_card += 1
            if column_card == 5:
                column_card = 0
                row_card += 1


        self.all_deck_cards_scrollArea.setWidget(self.all_deck_cards_scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.all_deck_cards_scrollArea, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.all_deck_centralwidget)

        self.Deck_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.all_deck_btn_exit.clicked.connect(lambda: self.Map_info(MainWindow))

    def Deck_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.all_deck_btn_exit.setText(_translate("MainWindow", "Назад"))
        def text_cards():
            sk1 = "{"
            sk2 = "}"
            for num_card,id_card in enumerate(self.deck, 1):
                exec(f"""self.card_cost_{num_card}.setText(_translate("MainWindow", f"{dict_all_cards.get(f"{id_card}").cost}"))""")
                exec(f"""self.card_name_{num_card}.setText(_translate("MainWindow", f"{dict_all_cards.get(f"{id_card}").name}"))""")

            for num_card, card_obj in enumerate(self.all_deck_cards_scrollAreaWidgetContents.children(), -1):
                for text_obj in card_obj.children():
                    if isinstance(text_obj, QtWidgets.QTextBrowser):
                        text_obj.setHtml(_translate("MainWindow",f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    f"p, li {sk1} white-space: pre-wrap; {sk2}\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dict_all_cards.get(f'{self.deck[num_card]}').info}</p></body></html>"))
        text_cards()

    def Map_info_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.map_info_abilites.setText(_translate("MainWindow", "Способности:"))

        def text_abilites_Html():
            abilites = game_player.ABIL
            abilites = abilites.split(";")
            try:
                self.map_info_text_abilities.setHtml(
                    f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                    "</body>""</html>")
            except:
                pass
            try:
                self.map_info_text_abilities.setHtml(
                    f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[1]}</span></p>\n"
                    "</body>""</html>")
            except:
                pass
            try:
                self.map_info_text_abilities.setHtml(
                    f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[1]}</span></p>\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[2]}</span></p>\n"
                    "</body>""</html>")
            except:
                pass
            try:
                self.map_info_text_abilities.setHtml(
                    f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[1]}</span></p>\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[2]}</span></p>\n"
                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[3]}</span></p>\n"
                    "</body>""</html>")
            except:
                pass

        text_abilites_Html()

        def text_cards():
            sk1 = "{"
            sk2 = "}"
            for num_card,id_card in enumerate(self.deck, 1):
                exec(f"""self.card_cost_{num_card}.setText(_translate("MainWindow", f"{dict_all_cards.get(f"{id_card}").cost}"))""")
                exec(f"""self.card_name_{num_card}.setText(_translate("MainWindow", f"{dict_all_cards.get(f"{id_card}").name}"))""")

            for num_card, card_obj in enumerate(self.map_info_cards_scrollAreaWidgetContents.children(), -1):
                for text_obj in card_obj.children():
                    if isinstance(text_obj, QtWidgets.QTextBrowser):
                        text_obj.setHtml(_translate("MainWindow",f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    f"p, li {sk1} white-space: pre-wrap; {sk2}\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dict_all_cards.get(f'{self.deck[num_card]}').info}</p></body></html>"))

        text_cards()

        # self.map_info_artefact_1.setText(_translate("MainWindow", "1"))

        self.map_info_pers_name.setText(_translate("MainWindow", f"Имя: {game_player.NAME}"))
        self.map_info_btn_cards.setText(_translate("MainWindow", "Карты:"))

        self.map_info_text_parameters.setHtml(_translate("MainWindow",
                                                         f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Характеристики:</span></p>\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Сила: {game_player.STR}</span></p>\n"
                                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Ловкость: {game_player.DEX}</span></p>\n"
                                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Телосложение: {game_player.CON}</span></p>\n"
                                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Мудрость: {game_player.WIZ}</span></p>\n"
                                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Интеллект: {game_player.INT}</span></p>\n"
                                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Харизма: {game_player.CHA}</span></p></body></html>"))
        self.map_info_text_info_pers.setHtml(_translate("MainWindow",
                                                        f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Информация:</span></p>\n"
                                                        f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{game_player.INFO}</span></p></body></html>"))
        self.map_info_exp.setText(_translate("MainWindow", "Опыт:"))

        self.map_info_btn_artefacts.setText(_translate("MainWindow", " Артефакты:"))
        self.map_info_btn_return_map.setText(_translate("MainWindow", "Вернуться"))

    def Shop_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shop_gold.setText(_translate("MainWindow", f" Золото: {self.gold}"))
        self.shop_groupBox_artefacts.setTitle(_translate("MainWindow", "Артефакты"))
        self.shop_artefact_1.setText(_translate("MainWindow", "PushButton"))
        self.shop_artefact_2.setText(_translate("MainWindow", "PushButton"))
        self.shop_artefact_3.setText(_translate("MainWindow", "PushButton"))
        self.shop_artefact_price_1.setText(_translate("MainWindow", "Цена"))
        self.shop_artefact_price_2.setText(_translate("MainWindow", "Цена"))
        self.shop_artefact_price_3.setText(_translate("MainWindow", "Цена"))
        self.shop_btn_delete_card.setText(_translate("MainWindow", "Удалить карту"))
        self.shop_groupBox_cards.setTitle(_translate("MainWindow", "Карты"))
        self.shop_card_1.setText(_translate("MainWindow", "PushButton"))
        self.shop_card_2.setText(_translate("MainWindow", "PushButton"))
        self.shop_card_3.setText(_translate("MainWindow", "PushButton"))
        self.shop_card_4.setText(_translate("MainWindow", "PushButton"))
        self.shop_card_5.setText(_translate("MainWindow", "PushButton"))
        self.shop_card_6.setText(_translate("MainWindow", "PushButton"))
        self.shop_card_price_1.setText(_translate("MainWindow", "Цена"))
        self.shop_card_price_2.setText(_translate("MainWindow", "Цена"))
        self.shop_card_price_3.setText(_translate("MainWindow", "Цена"))
        self.shop_card_price_4.setText(_translate("MainWindow", "Цена"))
        self.shop_card_price_5.setText(_translate("MainWindow", "Цена"))
        self.shop_card_price_6.setText(_translate("MainWindow", "Цена"))
        self.shop_btn_exit.setText(_translate("MainWindow", "Уйти"))

    def Rest_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rest_btn_rest.setText(_translate("MainWindow", "Отдых"))
        self.rest_btn_upgrade.setText(_translate("MainWindow", "Улучшение"))

    def Event_retranslateUi(self, MainWindow, name_event="Название евента", text_event="Текст евента"):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.event_text.setHtml(_translate("MainWindow",
                                           f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                           f"font-size:16pt;\">{text_event}</span></p></body></html>"))
        self.event_name.setText(_translate("MainWindow",
                                           f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{name_event}</span></p></body></html>"))

    def Main_map_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.map_btn_info.setText(_translate("MainWindow", f"{game_player.NAME}"))
        self.map_exit_in_menu.setText(_translate("MainWindow", "Выйти в меню"))
        self.map_HP_CE.setText(_translate("MainWindow", f"HP = {self.actual_HP}/{game_player.MAX_HP}  CE = {self.actual_CE}/{game_player.MAX_CE}"))
        self.map_gold.setText(_translate("MainWindow", f"Золото - {self.gold}"))
        self.map_num_floor.setText(_translate("MainWindow", f"Этаж {self.num_Floor+1}"))









if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Map()
    ui.Main_map(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())