from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, datetime
from FloorClass import create_all_Floors
from CherectersClass import list_all_cherecters


GG = list_all_cherecters[0]
print(GG.NAME)
class Ui_Map(object):
    num_Floor = 0
    gold = 10

    HP = GG.HP
    actual_HP = HP
    CE = GG.CE
    actual_CE = CE

    actual_pers_row = 0
    all_Floors = create_all_Floors()
    column_start = list(range(4))
    random.shuffle(column_start)
    otmetka_rooms = []
    map_floor = []
    dict_Floor = {}

    events = open(f"Data/events_{num_Floor + 1}.txt", "r", encoding="utf8")
    all_events = [event for event in events.readlines()]
    random.shuffle(all_events)

    def Main_map(self, MainWindow):
        print(self.actual_pers_row)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.map_your_deck = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_your_deck.sizePolicy().hasHeightForWidth())
        self.map_your_deck.setSizePolicy(sizePolicy)
        self.map_your_deck.setMinimumSize(QtCore.QSize(250, 0))
        self.map_your_deck.setObjectName("map_your_deck")
        self.gridLayout.addWidget(self.map_your_deck, 3, 14, 1, 1)
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

            self.map_event_0_start = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.map_event_0_start.sizePolicy().hasHeightForWidth())
            self.map_event_0_start.setSizePolicy(sizePolicy)
            self.map_event_0_start.setMinimumSize(QtCore.QSize(100, 100))
            self.map_event_0_start.setObjectName("map_event_0_start")
            self.gridLayout_2.addWidget(self.map_event_0_start, 0, self.column_start[0], 1, 1)
            self.map_floor.append(['map_event_0_start'])

            k = 1
            for i in self.all_Floors[num_Floor][1:12:]:
                for o in i:
                    exec(f"self.map_event_{k} = QtWidgets.QPushButton(self.scrollAreaWidgetContents)")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    exec(f"sizePolicy.setHeightForWidth(self.map_event_{k}.sizePolicy().hasHeightForWidth())")
                    exec(f"self.map_event_{k}.setSizePolicy(sizePolicy)")
                    exec(f"self.map_event_{k}.setMinimumSize(QtCore.QSize(100, 100))")
                    exec(f"self.map_event_{k}.setObjectName('map_event_{k}')")
                    k+=1

            if len(self.dict_Floor) == 0:
                row = 0
                name_event = 1
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
                        exec(f"self.gridLayout_2.addWidget(self.map_event_{name_event}, {row}, {column[column_index]}, 1, 1)")
                        exec(f"self.map_event_{name_event}.setText('{k}')")
                        v_map_floor.append(f"map_event_{name_event}")

                        self.dict_Floor[f"map_event_{name_event}"] = [row, column[column_index], k]

                        column_index += 1
                        name_event += 1
                self.map_floor.append(v_map_floor)

            elif len(self.dict_Floor) > 0:
                for widget in self.scrollAreaWidgetContents.children():
                    if isinstance(widget, QtWidgets.QPushButton):
                        if widget.objectName() == 'map_event_0_start' or widget.objectName() == "map_event_boss":
                            pass
                        else:
                            row_column_text = self.dict_Floor.get(widget.objectName(), 0)
                            self.gridLayout_2.addWidget(widget, row_column_text[0], row_column_text[1], 1, 1)
                            widget.setText(f"{row_column_text[2]}")

            self.map_event_boss = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.map_event_boss.setMinimumSize(QtCore.QSize(0, 150))
            self.map_event_boss.setObjectName("map_event_boss")
            self.gridLayout_2.addWidget(self.map_event_boss, 12, 0, 1, 4)
            self.map_floor.append(['map_event_boss'])

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
            print(button.objectName())
            self.otmetka_rooms.append(button.objectName())
            button.setStyleSheet("QWidget {"
                                 "border: 5px solid black;"
                                 "border-radius: 5px;"
                                 "}")
            if button == self.map_event_boss:
                self.Event(MainWindow)
                self.num_Floor+=1
                self.dict_Floor = {}
                self.otmetka_rooms = []
                self.map_floor = []
                self.actual_pers_row = 0
                random.shuffle(self.column_start)

            elif button == self.map_event_0_start:
                self.actual_pers_row = 0
                self.Event(MainWindow)

            if button.text() == 'Событие':
                self.Event(MainWindow)
            elif button.text() == 'Враг':
                self.Event(MainWindow)
            elif button.text() == 'Элитный враг':
                self.Event(MainWindow)
            elif button.text() == 'Магазин':
                self.Shop(MainWindow)
            elif button.text() == 'Отдых':
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

            for widgets_on_floor in all_button_in_floor[0:self.actual_pers_row+1:]:
                for widget in widgets_on_floor:
                    widget.setEnabled(True)

            for widgets_on_floor in all_button_in_floor[0:self.actual_pers_row:]:
                for widget in widgets_on_floor:
                    widget.setEnabled(False)

        btn_enebled()


    def Event(self, MainWindow):
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

        # event = self.all_events.pop(0).split(";")
        random.shuffle(self.all_events)
        event = self.all_events[0].split(";")

        name_event = event[0]
        text_event = event[1]
        count_answer = len(event[2].split("/"))
        text_answer = event[2].split("/")

        def create_event():
            for create_btn in range(count_answer):
                exec(f"self.event_btn_{create_btn} = QtWidgets.QPushButton(self.event_centralwidget)")
                exec(f"self.event_btn_{create_btn}.setStyleSheet('font: 14pt \"MS Shell Dlg 2\";')")
                exec(f"self.event_btn_{create_btn}.setObjectName('event_btn_{create_btn}')")
                exec(f"self.gridLayout.addWidget(self.event_btn_{create_btn}, {create_btn + 3}, 3, 1, 1)")
            for e,text_in_answer in enumerate(text_answer):
                exec(f"self.event_btn_{e}.setText(f'{text_answer[e]}')")

            if self.num_Floor+1 == 1:
                if 'Восполнение хп' == name_event:
                    def click():
                        button = MainWindow.sender()
                        if button.objectName() == "event_btn_0":
                            self.actual_HP += 10
                            if self.actual_HP > self.HP:
                                self.actual_HP = self.HP
                    self.event_btn_0.clicked.connect(click)
                elif 'Ловушка' == name_event:
                    def click():
                        button = MainWindow.sender()
                        if button.objectName() == "event_btn_0":
                            self.actual_HP -= 10
                    self.event_btn_0.clicked.connect(click)
                elif 'Сокровище' == name_event:
                    def click():
                        button = MainWindow.sender()
                        if button.objectName() == "event_btn_0":
                            self.gold += 20

                    self.event_btn_0.clicked.connect(click)
            elif self.num_Floor+1 == 2:
                if '' == name_event:
                    for create_btn in range(count_answer):
                        print(create_btn)
            elif self.num_Floor+1 == 3:
                if '' == name_event:
                    for create_btn in range(count_answer):
                        print(create_btn)

            for btn_in_event in self.event_centralwidget.children():
                if isinstance(btn_in_event, QtWidgets.QPushButton):
                    btn_in_event.clicked.connect(lambda: self.Main_map(MainWindow))

        create_event()

        self.Event_retranslateUi(MainWindow, name_event=name_event, text_event=text_event)
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
            self.actual_HP += self.HP//3
            if self.actual_HP > self.HP:
                self.actual_HP = self.HP

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
        self.map_your_deck.setText(_translate("MainWindow", f"{GG.NAME}"))
        self.map_exit_in_menu.setText(_translate("MainWindow", "Выйти в меню"))
        self.map_HP_CE.setText(_translate("MainWindow", f"HP = {self.actual_HP}/{self.HP}  CE = {self.actual_CE}/{self.CE}"))
        self.map_gold.setText(_translate("MainWindow", f"Золото - {self.gold}"))
        self.map_event_boss.setText(_translate("MainWindow", "Босс"))
        self.map_event_0_start.setText(_translate("MainWindow", "Начало"))
        self.map_num_floor.setText(_translate("MainWindow", f"Этаж {self.num_Floor+1}"))









if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Map()
    ui.Main_map(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())