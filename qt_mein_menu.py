from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random

inventar_pers=[]
kol_vo=0

class Main_menu(object):
    def mein_menu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("background-color: rgb(2, 13, 53);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.label.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                 "font: 16pt \"MS Shell Dlg 2\";"
                                 "background-image: url(Backgrounds/jjk_mein_menu.png)")
        self.label.setObjectName("label")

        self.btn_new_game = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new_game.setGeometry(QtCore.QRect(50, 421, 601, 61))
        self.btn_new_game.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 24pt \"Arial\";")
        self.btn_new_game.setObjectName("pushButton")
        self.btn_continue_game = QtWidgets.QPushButton(self.centralwidget)
        self.btn_continue_game.setGeometry(QtCore.QRect(50, 511, 521, 61))
        self.btn_continue_game.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 24pt \"Arial\";")
        self.btn_continue_game.setObjectName("pushButton_2")
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setGeometry(QtCore.QRect(50, 601, 241, 51))
        self.btn_settings.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 24pt \"Arial\";")
        self.btn_settings.setObjectName("pushButton_3")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(50, 680, 341, 61))
        self.btn_exit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 24pt \"Arial\";")
        self.btn_exit.setObjectName("pushButton_4")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 210, 491, 411))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.save_1 = QtWidgets.QPushButton(self.groupBox)
        self.save_2 = QtWidgets.QPushButton(self.groupBox)
        self.save_3 = QtWidgets.QPushButton(self.groupBox)
        for i, r in zip((self.save_1, self.save_2, self.save_3), (60, 130, 200)):
            i.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                            "font: 14pt \"MS Shell Dlg 2\";")
            i.setGeometry(QtCore.QRect(70, r, 371, 61))
            i.setObjectName(f"{i}")

        self.btn_hide_continue = QtWidgets.QPushButton(self.groupBox)
        self.btn_hide_continue.setGeometry(QtCore.QRect(270, 310, 171, 31))
        self.btn_hide_continue.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";"
                                             "background-color: rgb(255, 255, 255);")
        self.btn_hide_continue.setObjectName("btn_hide_continue")

        self.save_1.setText("Cохранение 1")
        self.save_2.setText("Cохранение 2")
        self.save_3.setText("Cохранение 3")
        self.btn_hide_continue.setText("Закрыть")
        self.groupBox.setVisible(False)

        self.btn_new_game.setText("Новая игра")
        self.btn_continue_game.setText("Продолить игру")
        self.btn_settings.setText("Настройки")
        self.btn_exit.setText("Выйти из игры")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_hide_continue.clicked.connect(lambda: self.groupBox.setVisible(False))
        self.btn_new_game.clicked.connect(lambda: self.gacha_menu(MainWindow))
        self.btn_continue_game.clicked.connect(lambda: self.groupBox.setVisible(True))
        self.btn_exit.clicked.connect(exit)

    index = 0
    result_index = []
    def random_cherecter(self):
        global kol_vo, colors, names
        file = open("cherecters.txt", "r", encoding="utf-8")
        lines = file.readlines()
        colors = []
        names = []
        for i in range(10):
            j = random.randint(1, 1000)
            if j <= 10:
                # 5*
                k = random.randint(0, 5)
                names.append((lines[k].split(';')[1]).replace('\n', ''))
                colors.append("yellow")
                self.result_index.append(lines[k].split(';')[0])
                inventar_pers.append(lines[k].split(';')[0])
                kol_vo = 0
            elif kol_vo >= 80:
                # 5*
                k = random.randint(0, 5)
                names.append((lines[k].split(';')[1]).replace('\n', ''))
                colors.append("yellow")
                self.result_index.append(lines[k].split(';')[0])
                inventar_pers.append(lines[k].split(';')[0])
                kol_vo = 0
            elif j > 10 and j < 250:
                # 4*
                kol_vo += 1
                k = random.randint(6, 17)
                names.append((lines[k].split(';')[1]).replace('\n', ''))
                colors.append("orange")
                self.result_index.append(lines[k].split(';')[0])
                inventar_pers.append(lines[k].split(';')[0])
            elif j >= 250 and j < 550:
                # 3*
                kol_vo += 1
                k = random.randint(18, 29)
                names.append((lines[k].split(';')[1]).replace('\n', ''))
                colors.append("blue")
                self.result_index.append(lines[k].split(';')[0])
                inventar_pers.append(lines[k].split(';')[0])
            elif j >= 550 and j < 850:
                # 2*
                kol_vo += 1
                k = random.randint(30, 34)
                names.append((lines[k].split(';')[1]).replace('\n', ''))
                colors.append("green")
                self.result_index.append(lines[k].split(';')[0])
                inventar_pers.append(lines[k].split(';')[0])
            else:
                # 1*
                kol_vo += 1
                k = random.randint(35, 40)
                names.append((lines[k].split(';')[1]).replace('\n', ''))
                colors.append("grey")
                self.result_index.append(lines[k].split(';')[0])
                inventar_pers.append(lines[k].split(';')[0])

        self.okno_s_perel(MainWindow)
        print(self.result_index)
        print(names)
        print(colors)
        print(kol_vo)

    def gacha_menu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 730, 101, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1271, 671))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(241, 241, 241);\n"
                                     "font: 12pt \"MS Shell Dlg 2\";")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleDescription("")
        self.tab.setObjectName("tab")
        self.backg_1 = QtWidgets.QLabel(self.tab)
        self.backg_1.setGeometry(QtCore.QRect(0, 0, 1271, 651))
        self.backg_1.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.backg_1.setText("")
        self.backg_1.setObjectName("backg_1")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(1060, 590, 201, 41))
        self.pushButton_6.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.backg_2 = QtWidgets.QLabel(self.tab_2)
        self.backg_2.setGeometry(QtCore.QRect(0, 0, 1271, 651))
        self.backg_2.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.backg_2.setText("")
        self.backg_2.setObjectName("backg_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(1060, 590, 201, 41))
        self.pushButton_7.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 730, 151, 41))
        self.label.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_5.setText("Выйти")
        self.pushButton_6.setText("Крутить гачу")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Классическая гача")
        self.pushButton_7.setText("Крутить гачу")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Временная гача")
        self.label.setText("Валюта: ")

        for i,im in zip((self.backg_1, self.backg_2),('Backgrounds/gacha1_foto.png','Backgrounds/gacha2_foto.png')):
            self.pix = QtGui.QPixmap(im)
            self.pix1 = self.pix.scaled(2271, 1000, QtCore.Qt.KeepAspectRatio)
            i.setPixmap(self.pix1)

        self.pushButton_5.clicked.connect(lambda: self.mein_menu(MainWindow))
        self.pushButton_6.clicked.connect(lambda: self.random_cherecter())
        self.pushButton_7.clicked.connect(lambda: self.random_cherecter())

    def okno_s_perel(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(440, 50, 400, 600))
        self.frame.setStyleSheet(f"background-color: rgb(255, 255, 255);"
                                 f"background-image: url(CherectersFoto/{self.result_index[self.index]}.png)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(660, 580, 165, 30))
        self.name_label.setStyleSheet(f"background-color: {colors[self.index]} ;font: 12pt \"MS Shell Dlg 2\";")
        self.name_label.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.name_label.setFrameShadow(QtWidgets.QLabel.Raised)
        self.name_label.setObjectName("name_label")
        self.name_label.setText(f"{names[self.index]}")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(720, 660, 121, 41))
        self.pushButton_1.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_1.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 660, 121, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def change_img():
            if self.index < 9:
                self.index += 1
                self.frame.setStyleSheet(f"background-color: rgb(255, 255, 255);"
                                         f"background-image: url(CherectersFoto/{self.result_index[self.index]}.png)")
                self.name_label.setStyleSheet(f"background-color: {colors[self.index]} ;font: 12pt \"MS Shell Dlg 2\";")
                self.name_label.setText(f"{names[self.index]}")
            else:
                self.index = 0
                self.okno(MainWindow)

        self.pushButton_1.clicked.connect(change_img)
        self.pushButton_2.clicked.connect(lambda: self.okno(MainWindow))

        self.pushButton_1.setText( "Далее")
        self.pushButton_2.setText( "Пропустить")

    def okno(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.index_1=list(range(0,10))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1170, 740, 101, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1170, 690, 101, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_2")
        _translate = QtCore.QCoreApplication.translate

        self.frame_6 = QtWidgets.QLabel(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(30, 420, 211, 361))
        self.frame_6.setStyleSheet(f"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_1 = QtWidgets.QLabel(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(30, 20, 211, 361))
        self.frame_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_1.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_1.setObjectName("frame_1")
        self.frame_2 = QtWidgets.QLabel(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(260, 20, 211, 361))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_7 = QtWidgets.QLabel(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(260, 420, 211, 361))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_9 = QtWidgets.QLabel(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(720, 420, 211, 361))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_3 = QtWidgets.QLabel(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(490, 20, 211, 361))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QLabel(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(720, 20, 211, 361))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_8 = QtWidgets.QLabel(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(490, 420, 211, 361))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_5 = QtWidgets.QLabel(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(950, 20, 211, 361))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_10 = QtWidgets.QLabel(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(950, 420, 211, 361))
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QLabel.Raised)
        self.frame_10.setObjectName("frame_10")

        self.name_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_9 = QtWidgets.QLabel(self.centralwidget)
        self.name_label_10 = QtWidgets.QLabel(self.centralwidget)

        k=0
        r=0
        count=0
        for i in (self.name_label_1,self.name_label_2,self.name_label_3,self.name_label_4,self.name_label_5,
                  self.name_label_6,self.name_label_7,self.name_label_8,self.name_label_9,self.name_label_10):
            i.setGeometry(QtCore.QRect(65+k, 340+r, 165, 30))
            i.setStyleSheet(f"background-color: {colors[count]} ;font: 12pt \"MS Shell Dlg 2\";")
            i.setFrameShape(QtWidgets.QLabel.StyledPanel)
            i.setFrameShadow(QtWidgets.QLabel.Raised)
            i.setObjectName(f"{i}")
            i.setText(f"{names[count]}")
            k+=230
            if count==4:
                r = 400
                k=0
            else:
                pass
            count += 1
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def okno_v_mein():
            self.result_index = []
            self.gacha_menu(MainWindow)

        def restart():
            self.result_index = []
            self.random_cherecter()
            self.okno_s_perel(MainWindow)

        self.pushButton_3.clicked.connect(okno_v_mein)
        self.pushButton_4.clicked.connect(restart)

        self.pushButton_3.setText("Выйти")
        self.pushButton_4.setText("Заново")

        e=0
        for i in (self.frame_1,self.frame_2,self.frame_3,self.frame_4,self.frame_5,
                  self.frame_6,self.frame_7,self.frame_8,self.frame_9,self.frame_10):
            self.pix = QtGui.QPixmap(f"CherectersFoto/{self.result_index[e]}.png")
            self.pix1 = self.pix.scaled(250, 361, QtCore.Qt.KeepAspectRatio)
            i.setPixmap(self.pix1)
            e+=1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    ui = Main_menu()
    ui.mein_menu(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())

