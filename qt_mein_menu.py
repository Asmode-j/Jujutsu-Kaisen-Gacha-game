from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, datetime
from CherectersClass import *

inventar_pers = []
kol_vo_do_SSR_classic = 0
kol_vo_do_SR_classic = 0
kol_vo_do_SSR_vrem = 0
kol_vo_do_SR_vrem = 0

resolution_weight = 1280
resolution_height = 800
######################################
# file = open("cherecters.txt", "r", encoding="utf-8")
# lines = file.readlines()
# for i in lines:
#    ind = i.split(';')[0]
#    inventar_pers.append(ind)
#####################################

# for ind,pers in zip(ind_pers, list_all_cherecters):
#    print(ind, pers.name)
    
#GG=list_all_cherecters[5]
#print(GG.name)

class Main_menu(object):
    def main_menu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(resolution_weight, resolution_height)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_menu_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.main_menu_btn_exit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 24pt \"Arial\";\n"
                                              "color: rgb(255, 255, 255);")
        self.main_menu_btn_exit.setObjectName("main_menu_btn_exit")
        self.gridLayout.addWidget(self.main_menu_btn_exit, 6, 0, 1, 1)
        self.main_menu_btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.main_menu_btn_settings.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 24pt \"Arial\";\n"
                                                  "color: rgb(255, 255, 255);")
        self.main_menu_btn_settings.setObjectName("main_menu_btn_settings")
        self.gridLayout.addWidget(self.main_menu_btn_settings, 5, 0, 1, 1)
        self.main_menu_space_1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu_space_1.sizePolicy().hasHeightForWidth())
        self.main_menu_space_1.setSizePolicy(sizePolicy)
        self.main_menu_space_1.setMinimumSize(QtCore.QSize(0, 400))
        self.main_menu_space_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_menu_space_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_menu_space_1.setObjectName("main_menu_space_1")
        self.gridLayout.addWidget(self.main_menu_space_1, 0, 0, 1, 2)
        self.main_menu_btn_new_game = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu_btn_new_game.sizePolicy().hasHeightForWidth())
        self.main_menu_btn_new_game.setSizePolicy(sizePolicy)
        self.main_menu_btn_new_game.setMinimumSize(QtCore.QSize(0, 0))
        self.main_menu_btn_new_game.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 24pt \"Arial\";\n"
                                                  "color: rgb(255, 255, 255);")
        self.main_menu_btn_new_game.setObjectName("main_menu_btn_new_game")
        self.gridLayout.addWidget(self.main_menu_btn_new_game, 1, 0, 1, 1)
        self.main_menu_btn_save_game = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu_btn_save_game.sizePolicy().hasHeightForWidth())
        self.main_menu_btn_save_game.setSizePolicy(sizePolicy)
        self.main_menu_btn_save_game.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 24pt \"Arial\";\n"
                                                   "color: rgb(255, 255, 255);")
        self.main_menu_btn_save_game.setObjectName("main_menu_btn_save_game")
        self.gridLayout.addWidget(self.main_menu_btn_save_game, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.mein_menu_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.main_menu_btn_new_game.clicked.connect(lambda: self.menu_info_pers(MainWindow))
        self.main_menu_btn_save_game.clicked.connect(lambda: self.save_menu(MainWindow))
        self.main_menu_btn_settings.clicked.connect(lambda: self.setting_menu(MainWindow))
        self.main_menu_btn_exit.clicked.connect(lambda: sys.exit())

    def setting_menu(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.setting_menu_check_resolution = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_menu_check_resolution.sizePolicy().hasHeightForWidth())
        self.setting_menu_check_resolution.setSizePolicy(sizePolicy)
        self.setting_menu_check_resolution.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_menu_check_resolution.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                         "font: 24pt \"Arial\";\n"
                                                         "color: rgb(255, 255, 255);")
        self.setting_menu_check_resolution.setObjectName("setting_menu_check_resolution")
        self.gridLayout_2.addWidget(self.setting_menu_check_resolution, 1, 1, 1, 1)
        self.setting_menu_windowed = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_menu_windowed.sizePolicy().hasHeightForWidth())
        self.setting_menu_windowed.setSizePolicy(sizePolicy)
        self.setting_menu_windowed.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_menu_windowed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 24pt \"Arial\";\n"
                                                 "color: rgb(255, 255, 255);background: transparent")
        self.setting_menu_windowed.setObjectName("setting_menu_windowed")
        self.gridLayout_2.addWidget(self.setting_menu_windowed, 3, 0, 1, 2)
        self.setting_menu_resolution = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_menu_resolution.sizePolicy().hasHeightForWidth())
        self.setting_menu_resolution.setSizePolicy(sizePolicy)
        self.setting_menu_resolution.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_menu_resolution.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 24pt \"Arial\";\n"
                                                   "color: rgb(0, 0, 0);")
        self.setting_menu_resolution.setObjectName("setting_menu_resolution")
        self.setting_menu_resolution.addItem("", "800;600")
        self.setting_menu_resolution.addItem("", "1024;768")
        self.setting_menu_resolution.addItem("", "1280;1024")
        self.setting_menu_resolution.addItem("", "1360;768")
        self.setting_menu_resolution.addItem("", "1366;768")
        self.setting_menu_resolution.addItem("", "1600;1200")
        self.setting_menu_resolution.addItem("", "1920;1080")
        self.gridLayout_2.addWidget(self.setting_menu_resolution, 0, 0, 1, 2)
        self.setting_menu_change_resolution = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_menu_change_resolution.sizePolicy().hasHeightForWidth())
        self.setting_menu_change_resolution.setSizePolicy(sizePolicy)
        self.setting_menu_change_resolution.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_menu_change_resolution.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                          "font: 24pt \"Arial\";\n"
                                                          "color: rgb(255, 255, 255);")
        self.setting_menu_change_resolution.setObjectName("setting_menu_change_resolution")
        self.gridLayout_2.addWidget(self.setting_menu_change_resolution, 4, 0, 1, 1)
        self.setting_menu_hide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_menu_hide.sizePolicy().hasHeightForWidth())
        self.setting_menu_hide.setSizePolicy(sizePolicy)
        self.setting_menu_hide.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_menu_hide.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "font: 24pt \"Arial\";\n"
                                             "color: rgb(255, 255, 255);")
        self.setting_menu_hide.setObjectName("setting_menu_hide")
        self.gridLayout_2.addWidget(self.setting_menu_hide, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "font: 24pt \"Arial\";\n"
                                 "color: rgb(255, 255, 255);background: transparent")
        self.label.setText(f"Выбранное разрешение: {resolution_weight};{resolution_height}")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.setting_menu_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def chek_resolution():
            global new_resolution_weight, new_resolution_height
            new_resolution = self.setting_menu_resolution.currentData()
            self.label.setText(f"Выбранное разрешение:{new_resolution}")
            new_resolution_weight = new_resolution.split(";")[0]
            new_resolution_height = new_resolution.split(";")[1]

        def change_resolution():
            global resolution_weight, resolution_height
            windowed = self.setting_menu_windowed.isChecked()
            resolution_weight = int(new_resolution_weight)
            resolution_height = int(new_resolution_height)
            self.main_menu(MainWindow)
            if windowed == True:
                MainWindow.showMaximized()
            elif windowed == False:
                MainWindow.showNormal()


        self.setting_menu_change_resolution.clicked.connect(lambda: change_resolution())
        self.setting_menu_check_resolution.clicked.connect(lambda: chek_resolution())
        self.setting_menu_hide.clicked.connect(lambda: self.main_menu(MainWindow))

    def save_menu(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.save_menu_btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.save_menu_btn_save.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 24pt \"Arial\";\n"
                                              "color: rgb(255, 255, 255);")
        self.save_menu_btn_save.setObjectName("save_menu_btn_save")
        self.gridLayout.addWidget(self.save_menu_btn_save, 3, 0, 1, 1)
        self.save_menu_save_2 = QtWidgets.QPushButton(self.centralwidget)
        self.save_menu_save_2.setMinimumSize(QtCore.QSize(0, 150))
        self.save_menu_save_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 42pt \"Arial\";\n"
                                            "color: rgb(255, 255, 255);")
        self.save_menu_save_2.setObjectName("save_menu_save_2")
        self.gridLayout.addWidget(self.save_menu_save_2, 1, 0, 1, 3)
        self.save_menu_save_3 = QtWidgets.QPushButton(self.centralwidget)
        self.save_menu_save_3.setMinimumSize(QtCore.QSize(0, 150))
        self.save_menu_save_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 42pt \"Arial\";\n"
                                            "color: rgb(255, 255, 255);")
        self.save_menu_save_3.setObjectName("save_menu_save_3")
        self.gridLayout.addWidget(self.save_menu_save_3, 2, 0, 1, 3)
        self.save_menu_btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.save_menu_btn_download.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 24pt \"Arial\";\n"
                                                  "color: rgb(255, 255, 255);")
        self.save_menu_btn_download.setObjectName("save_menu_btn_download")
        self.gridLayout.addWidget(self.save_menu_btn_download, 3, 1, 1, 1)
        self.save_menu_save_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.save_menu_save_1.sizePolicy().hasHeightForWidth())
        self.save_menu_save_1.setSizePolicy(sizePolicy)
        self.save_menu_save_1.setMinimumSize(QtCore.QSize(0, 150))
        self.save_menu_save_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 42pt \"Arial\";\n"
                                            "color: rgb(255, 255, 255);")
        self.save_menu_save_1.setObjectName("save_menu_save_1")
        self.gridLayout.addWidget(self.save_menu_save_1, 0, 0, 1, 3)
        self.save_menu_btn_hide = QtWidgets.QPushButton(self.centralwidget)
        self.save_menu_btn_hide.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 24pt \"Arial\";\n"
                                              "color: rgb(255, 255, 255);")
        self.save_menu_btn_hide.setObjectName("save_menu_btn_hide")
        self.gridLayout.addWidget(self.save_menu_btn_hide, 3, 2, 1, 1)

        self.save_menu_save_1.setText("Сохранение 1")
        self.save_menu_save_2.setText("Сохранение 2")
        self.save_menu_save_3.setText("Сохранение 3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.save_menu_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def change_save_text():
            try:
                save_file_1 = open(f"save1.txt", "r")
                self.save_menu_save_1.setText(f"Cохранение 1: {save_file_1.readlines()[0]}")
                self.save_menu_save_1.setStyleSheet("font: 42pt \"Arial\";"
                                                    "color: rgb(255, 255, 255);"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png');"
                                                    "background-position: center")
                save_file_1.close()
            except:
                pass
            try:
                save_file_2 = open(f"save2.txt", "r")
                self.save_menu_save_2.setText(f"Cохранение 2: {save_file_2.readlines()[0]}")
                self.save_menu_save_2.setStyleSheet("font: 42pt \"Arial\";"
                                                    "color: rgb(255, 255, 255);"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png');"
                                                    "background-position: center")
                save_file_2.close()
            except:
                pass
            try:
                save_file_3 = open(f"save3.txt", "r")
                self.save_menu_save_3.setText(f"Cохранение 3: {save_file_3.readlines()[0]}")
                self.save_menu_save_3.setStyleSheet("font: 42pt \"Arial\";"
                                                    "color: rgb(255, 255, 255);"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png');"
                                                    "background-position: center")
                save_file_3.close()
            except:
                pass
        change_save_text()

        def save_game(button):
            global button_save, name_save, save_index
            button_save = button
            if button == self.save_menu_save_1:
                name_save = "save1"
                save_index = '1'
            elif button == self.save_menu_save_2:
                name_save = "save2"
                save_index = '2'
            elif button == self.save_menu_save_3:
                name_save = "save3"
                save_index = '3'

        def save_menu_click():
            global inventar_pers, kol_vo_do_SSR_classic, kol_vo_do_SR_classic, kol_vo_do_SSR_vrem, kol_vo_do_SR_vrem
            button = MainWindow.sender()
            if button == self.save_menu_save_1 or button == self.save_menu_save_2 or button == self.save_menu_save_3:
                save_game(button)
            elif button == self.save_menu_btn_save:
                date = datetime.date.today()
                button_save.setText(f"Cохранение {save_index}: {date}")
                button_save.setStyleSheet("font: 24pt \"Arial\";"
                                          "color: rgb(255, 255, 255)")
                save_file = open(f"{name_save}.txt", "w+")
                save_file.write(f"{date}\n{inventar_pers}\n{kol_vo_do_SSR_classic}\n{kol_vo_do_SR_classic}\n"
                                f"{kol_vo_do_SSR_vrem}\n{kol_vo_do_SR_vrem}")
            elif button == self.save_menu_btn_download:
                try:
                    if button_save == self.save_menu_save_1:
                        save_file_1 = open(f"save1.txt", "r", encoding="utf-8")
                        line = save_file_1.readlines()
                        for i in line[1][1:-2:].split(','):
                            i = i.replace(' ',"")
                            inventar_pers.append(str(i[1:-1:]))
                        save_file_1 = open(f"save1.txt", "r", encoding="utf-8")
                        line = save_file_1.readlines()
                        kol_vo_do_SSR_classic = int(line[2])
                        kol_vo_do_SR_classic = int(line[3])
                        kol_vo_do_SSR_vrem = int(line[4])
                        kol_vo_do_SR_vrem = int(line[5])
                    if button_save == self.save_menu_save_2:
                        save_file_2 = open(f"save2.txt", "r", encoding="utf-8")
                        line = save_file_2.readlines()
                        for i in line[1][1:-2:].split(','):
                            i = i.replace(' ', "")
                            inventar_pers.append(str(i[1:-1:]))
                        kol_vo_do_SSR_classic = int(line[2])
                        kol_vo_do_SR_classic = int(line[3])
                        kol_vo_do_SSR_vrem = int(line[4])
                        kol_vo_do_SR_vrem = int(line[5])
                    if button_save == self.save_menu_save_3:
                        save_file_3 = open(f"save3.txt", "r", encoding="utf-8")
                        line = save_file_3.readlines()
                        for i in line[1][1:-2:].split(','):
                            i = i.replace(' ', "")
                            inventar_pers.append(str(i[1:-1:]))
                        kol_vo_do_SSR_classic = int(line[2])
                        kol_vo_do_SR_classic = int(line[3])
                        kol_vo_do_SSR_vrem = int(line[4])
                        kol_vo_do_SR_vrem = int(line[5])
                except:
                    pass

        self.save_menu_btn_hide.clicked.connect(lambda: self.main_menu(MainWindow))
        self.save_menu_btn_save.clicked.connect(save_menu_click)
        self.save_menu_btn_download.clicked.connect(save_menu_click)
        self.save_menu_save_1.clicked.connect(save_menu_click)
        self.save_menu_save_2.clicked.connect(save_menu_click)
        self.save_menu_save_3.clicked.connect(save_menu_click)

    def menu_info_pers(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png');font: 18pt \"MS Shell Dlg 2\";")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.info_pers_parametr_WIZ = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parametr_WIZ.sizePolicy().hasHeightForWidth())
        self.info_pers_parametr_WIZ.setSizePolicy(sizePolicy)
        self.info_pers_parametr_WIZ.setMinimumSize(QtCore.QSize(100, 30))
        self.info_pers_parametr_WIZ.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_parametr_WIZ.setObjectName("info_pers_parametr_WIZ")
        self.gridLayout_2.addWidget(self.info_pers_parametr_WIZ, 8, 4, 1, 1)

        self.info_pers_text_info_pers = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_text_info_pers.sizePolicy().hasHeightForWidth())
        self.info_pers_text_info_pers.setSizePolicy(sizePolicy)
        self.info_pers_text_info_pers.setMinimumSize(QtCore.QSize(300, 0))
        self.info_pers_text_info_pers.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";background: rgba(0,0,0,100) ;color: white")
        self.info_pers_text_info_pers.setObjectName("info_pers_text_info_pers")
        self.gridLayout_2.addWidget(self.info_pers_text_info_pers, 2, 4, 1, 1)


        self.info_pers_info_image_pers = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_info_image_pers.sizePolicy().hasHeightForWidth())
        self.info_pers_info_image_pers.setSizePolicy(sizePolicy)
        self.info_pers_info_image_pers.setMinimumSize(QtCore.QSize(400, 600))
        self.info_pers_info_image_pers.setMaximumSize(QtCore.QSize(400, 600))
        self.info_pers_info_image_pers.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.info_pers_info_image_pers.setAcceptDrops(False)
        self.info_pers_info_image_pers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_pers_info_image_pers.setAutoFillBackground(False)
        self.info_pers_info_image_pers.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.info_pers_info_image_pers.setText("")
        self.info_pers_info_image_pers.setObjectName("info_pers_info_image_pers")
        self.gridLayout_2.addWidget(self.info_pers_info_image_pers, 0, 3, 9, 1)
        self.info_pers_parameters = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parameters.sizePolicy().hasHeightForWidth())
        self.info_pers_parameters.setSizePolicy(sizePolicy)
        self.info_pers_parameters.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";background: rgba(0,0,0,100); color: white")
        self.info_pers_parameters.setObjectName("info_pers_parameters")
        self.gridLayout_2.addWidget(self.info_pers_parameters, 3, 4, 1, 1)
        self.info_pers_btn_exit_in_mein_menu = QtWidgets.QPushButton(self.centralwidget)
        self.info_pers_btn_exit_in_mein_menu.setStyleSheet("font: 18pt; background-color: rgb(197, 197, 197); color: white")
        self.info_pers_btn_exit_in_mein_menu.setObjectName("info_pers_btn_exit_in_mein_menu")
        self.gridLayout_2.addWidget(self.info_pers_btn_exit_in_mein_menu, 12, 0, 1, 1)
        self.info_pers_btn_gacha_mein_menu = QtWidgets.QPushButton(self.centralwidget)
        self.info_pers_btn_gacha_mein_menu.setStyleSheet("font: 18pt; background-color: rgb(197, 197, 197); color: white")
        self.info_pers_btn_gacha_mein_menu.setObjectName("info_pers_btn_gacha_mein_menu")
        self.gridLayout_2.addWidget(self.info_pers_btn_gacha_mein_menu, 12, 1, 1, 1)

        self.info_pers_text_abilities = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_text_abilities.sizePolicy().hasHeightForWidth())
        self.info_pers_text_abilities.setSizePolicy(sizePolicy)
        self.info_pers_text_abilities.setMinimumSize(QtCore.QSize(300, 0))
        self.info_pers_text_abilities.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";background: rgba(0,0,0,100) ;color: white")
        self.info_pers_text_abilities.setObjectName("info_pers_text_abilities")
        self.gridLayout_2.addWidget(self.info_pers_text_abilities, 11, 4, 1, 1)


        self.info_pers_abilities = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_abilities.sizePolicy().hasHeightForWidth())
        self.info_pers_abilities.setSizePolicy(sizePolicy)
        self.info_pers_abilities.setMinimumSize(QtCore.QSize(0, 0))
        self.info_pers_abilities.setMouseTracking(True)
        self.info_pers_abilities.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";background: rgba(0,0,0,100) ;color: white")
        self.info_pers_abilities.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.info_pers_abilities.setObjectName("info_pers_abilities")
        self.gridLayout_2.addWidget(self.info_pers_abilities, 10, 4, 1, 1)
        self.info_pers_parametr_DEX = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parametr_DEX.sizePolicy().hasHeightForWidth())
        self.info_pers_parametr_DEX.setSizePolicy(sizePolicy)
        self.info_pers_parametr_DEX.setMinimumSize(QtCore.QSize(100, 30))
        self.info_pers_parametr_DEX.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_parametr_DEX.setObjectName("info_pers_parametr_DEX")
        self.gridLayout_2.addWidget(self.info_pers_parametr_DEX, 5, 4, 1, 1)
        self.info_pers_btn_start_game = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_btn_start_game.sizePolicy().hasHeightForWidth())
        self.info_pers_btn_start_game.setSizePolicy(sizePolicy)
        self.info_pers_btn_start_game.setMinimumSize(QtCore.QSize(300, 0))
        self.info_pers_btn_start_game.setStyleSheet("background-color: rgb(197, 197, 197);font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_btn_start_game.setObjectName("info_pers_btn_start_game")
        self.gridLayout_2.addWidget(self.info_pers_btn_start_game, 12, 4, 1, 1)
        self.info_pers_parametr_INT = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parametr_INT.sizePolicy().hasHeightForWidth())
        self.info_pers_parametr_INT.setSizePolicy(sizePolicy)
        self.info_pers_parametr_INT.setMinimumSize(QtCore.QSize(100, 30))
        self.info_pers_parametr_INT.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_parametr_INT.setObjectName("info_pers_parametr_INT")
        self.gridLayout_2.addWidget(self.info_pers_parametr_INT, 7, 4, 1, 1)
        self.info_pers_parametr_CHA = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parametr_CHA.sizePolicy().hasHeightForWidth())
        self.info_pers_parametr_CHA.setSizePolicy(sizePolicy)
        self.info_pers_parametr_CHA.setMinimumSize(QtCore.QSize(100, 30))
        self.info_pers_parametr_CHA.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_parametr_CHA.setObjectName("info_pers_parametr_CHA")
        self.gridLayout_2.addWidget(self.info_pers_parametr_CHA, 9, 4, 1, 1)
        self.info_pers_parametr_CON = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parametr_CON.sizePolicy().hasHeightForWidth())
        self.info_pers_parametr_CON.setSizePolicy(sizePolicy)
        self.info_pers_parametr_CON.setMinimumSize(QtCore.QSize(100, 30))
        self.info_pers_parametr_CON.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_parametr_CON.setObjectName("info_pers_parametr_CON")
        self.gridLayout_2.addWidget(self.info_pers_parametr_CON, 6, 4, 1, 1)
        self.info_pers_name = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_name.sizePolicy().hasHeightForWidth())
        self.info_pers_name.setSizePolicy(sizePolicy)
        self.info_pers_name.setMinimumSize(QtCore.QSize(300, 50))
        self.info_pers_name.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";background: rgba(0,0,0,100) ;color: white")
        self.info_pers_name.setObjectName("info_pers_name")
        self.gridLayout_2.addWidget(self.info_pers_name, 0, 4, 1, 1)
        self.info_pers_parametr_STR = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_parametr_STR.sizePolicy().hasHeightForWidth())
        self.info_pers_parametr_STR.setSizePolicy(sizePolicy)
        self.info_pers_parametr_STR.setMinimumSize(QtCore.QSize(100, 30))
        self.info_pers_parametr_STR.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_parametr_STR.setObjectName("info_pers_parametr_STR")
        self.gridLayout_2.addWidget(self.info_pers_parametr_STR, 4, 4, 1, 1)
        self.info_pers_info_about_pers = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_info_about_pers.sizePolicy().hasHeightForWidth())
        self.info_pers_info_about_pers.setSizePolicy(sizePolicy)
        self.info_pers_info_about_pers.setMinimumSize(QtCore.QSize(300, 0))
        self.info_pers_info_about_pers.setMouseTracking(True)
        self.info_pers_info_about_pers.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";background: rgba(0,0,0,100) ;color: white")
        self.info_pers_info_about_pers.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.info_pers_info_about_pers.setObjectName("info_pers_info_about_pers")
        self.gridLayout_2.addWidget(self.info_pers_info_about_pers, 1, 4, 1, 1)
        self.info_pers_btn_evolution_pers = QtWidgets.QPushButton(self.centralwidget)
        self.info_pers_btn_evolution_pers.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: white")
        self.info_pers_btn_evolution_pers.setObjectName("info_pers_btn_evolution_pers")
        self.gridLayout_2.addWidget(self.info_pers_btn_evolution_pers, 9, 3, 1, 1)


        self.info_pers_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pers_scrollArea.sizePolicy().hasHeightForWidth())
        self.info_pers_scrollArea.setSizePolicy(sizePolicy)
        self.info_pers_scrollArea.setMinimumSize(QtCore.QSize(540, 0))
        self.info_pers_scrollArea.setMaximumSize(QtCore.QSize(520, 1677))
        self.info_pers_scrollArea.setWidgetResizable(False)
        self.info_pers_scrollArea.setObjectName("info_pers_scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 729))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        file = open("cherecters.txt", "r", encoding="utf-8")
        lines = file.readlines()
        ind_pers = []
        name_pers = []
        for i in lines:
            ind = i.split(';')[0]
            nam = i.split(';')[1].replace('\n', '')
            ind_pers.append(ind)
            name_pers.append(nam)

        def create_ikons():
            self.ikonka_01 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_02 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_03 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_04 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_05 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_06 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_07 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_08 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_09 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_33 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_34 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_35 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_36 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_37 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_38 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_39 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_40 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ikonka_41 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            c=0
            r=0
            inde=0
            for ind,i in zip(ind_pers,(self.ikonka_01,self.ikonka_02,self.ikonka_03,self.ikonka_04,self.ikonka_05,
                      self.ikonka_06,self.ikonka_07,self.ikonka_08,self.ikonka_09,self.ikonka_10,
                      self.ikonka_11,self.ikonka_12,self.ikonka_13,self.ikonka_14,self.ikonka_15,
                      self.ikonka_16,self.ikonka_17,self.ikonka_18,self.ikonka_19,self.ikonka_20,
                      self.ikonka_21,self.ikonka_22,self.ikonka_23,self.ikonka_24,self.ikonka_25,
                      self.ikonka_26,self.ikonka_27,self.ikonka_28,self.ikonka_29,self.ikonka_30,
                      self.ikonka_31,self.ikonka_32,self.ikonka_33,self.ikonka_34,self.ikonka_35,
                      self.ikonka_36,self.ikonka_37,self.ikonka_38,self.ikonka_39,self.ikonka_40,
                      self.ikonka_41)):
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(i.sizePolicy().hasHeightForWidth())
                i.setSizePolicy(sizePolicy)
                i.setMinimumSize(QtCore.QSize(75, 75))
                i.setStyleSheet("background-color: rgb(197, 197, 197);")
                if ind in inventar_pers:
                    i.setStyleSheet(f"background-image: url(CherectersFoto/ikons/{ind_pers[inde]}.png)")
                i.setObjectName(f"{i}")
                if c==5:
                    c = 0
                    r += 1
                self.gridLayout.addWidget(i, r, c, 1, 1)
                c += 1
                inde += 1
        create_ikons()


        self.info_pers_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.info_pers_scrollArea, 0, 0, 12, 2)

        btn_ikons = (self.ikonka_01, self.ikonka_02, self.ikonka_03, self.ikonka_04, self.ikonka_05,
                     self.ikonka_06,self.ikonka_07,self.ikonka_08,self.ikonka_09,self.ikonka_10,
                     self.ikonka_11,self.ikonka_12,self.ikonka_13,self.ikonka_14,self.ikonka_15,
                     self.ikonka_16,self.ikonka_17,self.ikonka_18,self.ikonka_19,self.ikonka_20,
                     self.ikonka_21,self.ikonka_22,self.ikonka_23,self.ikonka_24,self.ikonka_25,
                     self.ikonka_26,self.ikonka_27,self.ikonka_28,self.ikonka_29,self.ikonka_30,
                     self.ikonka_31,self.ikonka_32,self.ikonka_33,self.ikonka_34,self.ikonka_35,
                     self.ikonka_36,self.ikonka_37,self.ikonka_38,self.ikonka_39,self.ikonka_40,
                     self.ikonka_41)

        def ikons_cliced():
            button = MainWindow.sender()
            for e,i in enumerate(zip(ind_pers, btn_ikons)):
                if button==i[1]:
                    self.pix = QtGui.QPixmap(f"CherectersFoto/{i[0]}.png")
                    self.pix1 = self.pix.scaled(600, 600, QtCore.Qt.KeepAspectRatio)
                    self.info_pers_info_image_pers.setPixmap(self.pix1)
                    char = list_all_cherecters[e]

                    self.info_pers_name.setText(f"Имя: {char.name}")
                    self.info_pers_parametr_STR.setText(f"Сила: {char.STR}")
                    self.info_pers_parametr_DEX.setText(f"Ловкость:{char.DEX}")
                    self.info_pers_parametr_CON.setText(f"Телосложение:{char.CON}")
                    self.info_pers_parametr_INT.setText(f"Интеллект:{char.INT}")
                    self.info_pers_parametr_WIZ.setText(f"Мудрость:{char.WIZ}")
                    self.info_pers_parametr_CHA.setText(f"Харизма:{char.CHA}")
                    self.info_pers_text_info_pers.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                                                          f" text-indent:0px;\"><span style=\" font-size:14pt;\">{lines[e].split(';')[2]}</span></p></body></html>")
                    def text_abilites_Html():
                        abilites = lines[e].split(';')[3].split(",")
                        try:
                            self.info_pers_text_abilities.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                      f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                                                                      "</body>""</html>")
                        except:
                            pass
                        try:
                            self.info_pers_text_abilities.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                      f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                                                                      f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[1]}</span></p>\n"
                                                                      "</body>""</html>")
                        except:
                            pass
                        try:
                            self.info_pers_text_abilities.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
                            self.info_pers_text_abilities.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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

        for ind,i in zip(ind_pers,btn_ikons):
            i.clicked.connect(ikons_cliced)
            i.setEnabled(False)
            if ind in inventar_pers:
                i.setEnabled(True)

        self.info_pers_btn_exit_in_mein_menu.clicked.connect(lambda: self.main_menu(MainWindow))
        self.info_pers_btn_gacha_mein_menu.clicked.connect(lambda: self.gacha_menu(MainWindow))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menu_info_pers_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.info_pers_parametr_WIZ.setText("Мудрость:")
        self.info_pers_parametr_DEX.setText("Ловкость:")
        self.info_pers_parametr_INT.setText("Интеллект:")
        self.info_pers_parametr_CHA.setText("Харизма:")
        self.info_pers_parametr_CON.setText("Телосложение:")
        self.info_pers_name.setText("Имя:")
        self.info_pers_parametr_STR.setText("Сила:")
        self.info_pers_text_info_pers.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                                              " text-indent:0px;\"><span style=\" font-size:14pt;\"> </span></p></body></html>")
        self.info_pers_text_abilities.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                                              " text-indent:0px;\"><span style=\" font-size:14pt;\"></span></p></body></html>")
        def first_info_pers():

            for e,i in enumerate(zip(ind_pers,btn_ikons)):
                x = i[1].isEnabled()
                if x == True:
                    self.pix = QtGui.QPixmap(f"CherectersFoto/{i[0]}.png")
                    self.pix1 = self.pix.scaled(600, 600, QtCore.Qt.KeepAspectRatio)
                    self.info_pers_info_image_pers.setPixmap(self.pix1)
                    char = list_all_cherecters[e]

                    self.info_pers_name.setText(f"Имя: {char.name}")
                    self.info_pers_parametr_STR.setText(f"Сила: {char.STR}")
                    self.info_pers_parametr_DEX.setText(f"Ловкость:{char.DEX}")
                    self.info_pers_parametr_CON.setText(f"Телосложение:{char.CON}")
                    self.info_pers_parametr_INT.setText(f"Интеллект:{char.INT}")
                    self.info_pers_parametr_WIZ.setText(f"Мудрость:{char.WIZ}")
                    self.info_pers_parametr_CHA.setText(f"Харизма:{char.CHA}")
                    self.info_pers_text_info_pers.setHtml(
                        f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        f" text-indent:0px;\"><span style=\" font-size:14pt;\">{lines[e].split(';')[2]}</span></p></body></html>")

                    def text_abilites_Html():
                        abilites = lines[e].split(';')[3].split(",")
                        try:
                            self.info_pers_text_abilities.setHtml(
                                f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                "p, li { white-space: pre-wrap; }\n"
                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">{abilites[0]}</span></p>\n"
                                "</body>""</html>")
                        except:
                            pass
                        try:
                            self.info_pers_text_abilities.setHtml(
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
                            self.info_pers_text_abilities.setHtml(
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
                            self.info_pers_text_abilities.setHtml(
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
                    break
        first_info_pers()

    def random_cherecter(self, x1_or_x10, gacha):
        global kol_vo_do_SSR_classic, kol_vo_do_SR_classic, kol_vo_do_SSR_vrem, kol_vo_do_SR_vrem,\
            colors, names, result_index, zamena_texta_v_okno_s_perekl
        file = open("cherecters.txt", "r", encoding="utf-8")
        lines = file.readlines()
        result_index = []
        colors = []
        names = []

        def classic_random(x1_or_x10):
            global kol_vo_do_SSR_classic, kol_vo_do_SR_classic,colors, names, result_index
            for i in range(x1_or_x10):
                kol_vo_do_SR_classic+=1
                kol_vo_do_SSR_classic+=1
                j = random.randint(1, 1000)
                if j <= 10:
                    # 5*
                    k = random.randint(0, 5)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("yellow")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                    kol_vo_do_SSR_classic = 0
                elif kol_vo_do_SSR_classic >= 80:
                    # 5*
                    k = random.randint(0, 5)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("yellow")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                    kol_vo_do_SSR_classic = 0
                elif j > 10 and j < 150:
                    # 4*
                    kol_vo_do_SR_classic = 0
                    k = random.randint(6, 17)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("orange")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                elif kol_vo_do_SR_classic >= 10:
                    # 4*
                    kol_vo_do_SR_classic = 0
                    k = random.randint(6, 17)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("orange")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                elif j >= 250 and j < 550:
                    # 3*
                    k = random.randint(18, 29)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("lightblue")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                elif j >= 550 and j < 850:
                    # 2*
                    k = random.randint(30, 34)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("lightgreen")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                else:
                    # 1*
                    k = random.randint(35, 40)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("white")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])

        def vrem_random(x1_or_x10):
            global kol_vo_do_SSR_vrem, kol_vo_do_SR_vrem, colors, names, result_index
            for i in range(x1_or_x10):
                kol_vo_do_SR_vrem += 1
                kol_vo_do_SSR_vrem += 1
                j = random.randint(1, 1000)
                if j <= 10:
                    # 5*
                    v = random.randint(0, 1)
                    if v == 0:
                        k = random.randint(0, 5)
                        names.append((lines[k].split(';')[1]).replace('\n', ''))
                        colors.append("yellow")
                        result_index.append(lines[k].split(';')[0])
                        inventar_pers.append(lines[k].split(';')[0])
                        kol_vo_do_SSR_vrem = 0
                    elif v == 1:
                        names.append((lines[5].split(';')[1]).replace('\n', ''))
                        colors.append("yellow")
                        result_index.append(lines[5].split(';')[0])
                        inventar_pers.append(lines[5].split(';')[0])
                        kol_vo_do_SSR_vrem = 0
                elif kol_vo_do_SSR_vrem >= 80:
                    # 5*
                    v = random.randint(0, 1)
                    if v == 0:
                        k = random.randint(0, 5)
                        names.append((lines[k].split(';')[1]).replace('\n', ''))
                        colors.append("yellow")
                        result_index.append(lines[k].split(';')[0])
                        inventar_pers.append(lines[k].split(';')[0])
                        kol_vo_do_SSR_vrem = 0
                    elif v == 1:
                        names.append((lines[5].split(';')[1]).replace('\n', ''))
                        colors.append("yellow")
                        result_index.append(lines[5].split(';')[0])
                        inventar_pers.append(lines[5].split(';')[0])
                        kol_vo_do_SSR_vrem = 0
                elif j > 10 and j < 150:
                    # 4*
                    kol_vo_do_SR_vrem = 0
                    k = random.randint(6, 17)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("orange")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                elif kol_vo_do_SR_vrem >= 10:
                    # 4*
                    kol_vo_do_SR_vrem = 0
                    k = random.randint(6, 17)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("orange")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                elif j >= 250 and j < 550:
                    # 3*
                    k = random.randint(18, 29)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("lightblue")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                elif j >= 550 and j < 850:
                    # 2*
                    k = random.randint(30, 34)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("lightgreen")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])
                else:
                    # 1*
                    k = random.randint(35, 40)
                    names.append((lines[k].split(';')[1]).replace('\n', ''))
                    colors.append("white")
                    result_index.append(lines[k].split(';')[0])
                    inventar_pers.append(lines[k].split(';')[0])

        if x1_or_x10 == 1:
            zamena_texta_v_okno_s_perekl = 1
        elif x1_or_x10 == 10:
            zamena_texta_v_okno_s_perekl = 10

        def change_gacha(x1_or_x10,gacha):
            if gacha =="classic":
                classic_random(x1_or_x10)
            elif gacha == "vrem":
                vrem_random(x1_or_x10)

        change_gacha(x1_or_x10,gacha)
        # print(result_index)
        #print(gacha)
        #print(kol_vo_do_SSR_vrem, kol_vo_do_SR_vrem)
        # print(colors)

        self.okno_s_perekl(MainWindow, gacha)

    def gacha_menu(self, MainWindow):
        global gacha
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png');font: 18pt \"MS Shell Dlg 2\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gacha_menu_valyta = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_valyta.sizePolicy().hasHeightForWidth())
        self.gacha_menu_valyta.setSizePolicy(sizePolicy)
        self.gacha_menu_valyta.setMinimumSize(QtCore.QSize(200, 30))
        self.gacha_menu_valyta.setStyleSheet("background: rgba(0, 0, 0,0);\n"
                                             "font: 16pt \"MS Shell Dlg 2\";color: white")
        self.gacha_menu_valyta.setObjectName("gacha_menu_valyta")
        self.gridLayout.addWidget(self.gacha_menu_valyta, 1, 1, 1, 1)
        self.gacha_menu_exit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_exit.sizePolicy().hasHeightForWidth())
        self.gacha_menu_exit.setSizePolicy(sizePolicy)
        self.gacha_menu_exit.setMinimumSize(QtCore.QSize(200, 30))
        self.gacha_menu_exit.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                           "font: 16pt \"MS Shell Dlg 2\";color: white")
        self.gacha_menu_exit.setIconSize(QtCore.QSize(16, 16))
        self.gacha_menu_exit.setObjectName("gacha_menu_exit")
        self.gridLayout.addWidget(self.gacha_menu_exit, 1, 0, 1, 1)
        self.gacha_menu_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_tabWidget.sizePolicy().hasHeightForWidth())
        self.gacha_menu_tabWidget.setSizePolicy(sizePolicy)
        self.gacha_menu_tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.gacha_menu_tabWidget.setAutoFillBackground(False)
        self.gacha_menu_tabWidget.setStyleSheet("background-color: rgb(241, 241, 241);\n"
                                                "font: 12pt \"MS Shell Dlg 2\";")
        self.gacha_menu_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.gacha_menu_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.gacha_menu_tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.gacha_menu_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.gacha_menu_tabWidget.setUsesScrollButtons(True)
        self.gacha_menu_tabWidget.setDocumentMode(True)
        self.gacha_menu_tabWidget.setTabsClosable(False)
        self.gacha_menu_tabWidget.setMovable(False)
        self.gacha_menu_tabWidget.setTabBarAutoHide(False)
        self.gacha_menu_tabWidget.setObjectName("gacha_menu_tabWidget")
        self.gacha_menu_tab = QtWidgets.QWidget()
        self.gacha_menu_tab.setAccessibleDescription("")
        self.gacha_menu_tab.setStyleSheet("background-image: url(Backgrounds/gacha1_foto.png);")
        self.gacha_menu_tab.setObjectName("gacha_menu_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gacha_menu_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gacha_menu_btn_gacha_x10 = QtWidgets.QPushButton(self.gacha_menu_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_btn_gacha_x10.sizePolicy().hasHeightForWidth())
        self.gacha_menu_btn_gacha_x10.setSizePolicy(sizePolicy)
        self.gacha_menu_btn_gacha_x10.setMinimumSize(QtCore.QSize(200, 0))
        self.gacha_menu_btn_gacha_x10.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                    "font: 16pt \"MS Shell Dlg 2\";color: white;"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.gacha_menu_btn_gacha_x10.setIconSize(QtCore.QSize(16, 16))
        self.gacha_menu_btn_gacha_x10.setObjectName("gacha_menu_btn_gacha_x10")
        self.gridLayout_2.addWidget(self.gacha_menu_btn_gacha_x10, 1, 2, 1, 1)
        self.gacha_menu_backg_1 = QtWidgets.QLabel(self.gacha_menu_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_backg_1.sizePolicy().hasHeightForWidth())
        self.gacha_menu_backg_1.setSizePolicy(sizePolicy)
        self.gacha_menu_backg_1.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.gacha_menu_backg_1.setText("")
        self.gacha_menu_backg_1.setObjectName("gacha_menu_backg_1")
        self.gridLayout_2.addWidget(self.gacha_menu_backg_1, 0, 0, 1, 3)
        self.gacha_menu_btn_gacha_x1 = QtWidgets.QPushButton(self.gacha_menu_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_btn_gacha_x1.sizePolicy().hasHeightForWidth())
        self.gacha_menu_btn_gacha_x1.setSizePolicy(sizePolicy)
        self.gacha_menu_btn_gacha_x1.setMinimumSize(QtCore.QSize(200, 0))
        self.gacha_menu_btn_gacha_x1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                    "font: 16pt \"MS Shell Dlg 2\";color: white;"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.gacha_menu_btn_gacha_x1.setObjectName("gacha_menu_btn_gacha_x1")
        self.gridLayout_2.addWidget(self.gacha_menu_btn_gacha_x1, 1, 1, 1, 1)
        self.gacha_menu_tabWidget.addTab(self.gacha_menu_tab, "")
        self.gacha_menu_tab_2 = QtWidgets.QWidget()
        self.gacha_menu_tab_2.setStyleSheet("background-image: url(Backgrounds/gacha2_foto.png);")
        self.gacha_menu_tab_2.setObjectName("gacha_menu_tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gacha_menu_tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gacha_menu_btn_gacha_x10_2 = QtWidgets.QPushButton(self.gacha_menu_tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_btn_gacha_x10_2.sizePolicy().hasHeightForWidth())
        self.gacha_menu_btn_gacha_x10_2.setSizePolicy(sizePolicy)
        self.gacha_menu_btn_gacha_x10_2.setMinimumSize(QtCore.QSize(200, 0))
        self.gacha_menu_btn_gacha_x10_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                    "font: 16pt \"MS Shell Dlg 2\";color: white;"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.gacha_menu_btn_gacha_x10_2.setIconSize(QtCore.QSize(16, 16))
        self.gacha_menu_btn_gacha_x10_2.setObjectName("gacha_menu_btn_gacha_x10_2")
        self.gridLayout_3.addWidget(self.gacha_menu_btn_gacha_x10_2, 1, 2, 1, 1)
        self.gacha_menu_backg_2 = QtWidgets.QLabel(self.gacha_menu_tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_backg_2.sizePolicy().hasHeightForWidth())
        self.gacha_menu_backg_2.setSizePolicy(sizePolicy)
        self.gacha_menu_backg_2.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.gacha_menu_backg_2.setText("")
        self.gacha_menu_backg_2.setObjectName("gacha_menu_backg_2")
        self.gridLayout_3.addWidget(self.gacha_menu_backg_2, 0, 0, 1, 3)
        self.gacha_menu_btn_gacha_x1_2 = QtWidgets.QPushButton(self.gacha_menu_tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gacha_menu_btn_gacha_x1_2.sizePolicy().hasHeightForWidth())
        self.gacha_menu_btn_gacha_x1_2.setSizePolicy(sizePolicy)
        self.gacha_menu_btn_gacha_x1_2.setMinimumSize(QtCore.QSize(200, 0))
        self.gacha_menu_btn_gacha_x1_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                    "font: 16pt \"MS Shell Dlg 2\";color: white;"
                                                    "background-image: url('Backgrounds/jjk_mein_menu.png')")
        self.gacha_menu_btn_gacha_x1_2.setObjectName("gacha_menu_btn_gacha_x1_2")
        self.gridLayout_3.addWidget(self.gacha_menu_btn_gacha_x1_2, 1, 1, 1, 1)
        self.gacha_menu_tabWidget.addTab(self.gacha_menu_tab_2, "")
        self.gridLayout.addWidget(self.gacha_menu_tabWidget, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gacha_menu_retranslateUi(MainWindow)
        self.gacha_menu_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # for i, im in zip((self.gacha_menu_backg_1, self.gacha_menu_backg_2), ('Backgrounds/gacha1_foto.png', 'Backgrounds/gacha2_foto.png')):
        #      self.pix = QtGui.QPixmap(im)
        #      self.pix1 = self.pix.scaled(1360, 768, QtCore.Qt.KeepAspectRatio)
        #      i.setPixmap(self.pix1)

        self.gacha_menu_exit.clicked.connect(lambda: self.menu_info_pers(MainWindow))
        self.gacha_menu_btn_gacha_x1.clicked.connect(lambda: self.random_cherecter(1,"classic"))
        self.gacha_menu_btn_gacha_x10.clicked.connect(lambda: self.random_cherecter(10,"classic"))
        self.gacha_menu_btn_gacha_x1_2.clicked.connect(lambda: self.random_cherecter(1,"vrem"))
        self.gacha_menu_btn_gacha_x10_2.clicked.connect(lambda: self.random_cherecter(10,"vrem"))

    def okno_s_perekl(self, MainWindow, gacha):
        index=0
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png');font: 18pt \"MS Shell Dlg 2\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.okno_s_perekl_btn_skip = QtWidgets.QPushButton(self.centralwidget)
        self.okno_s_perekl_btn_skip.setMinimumSize(QtCore.QSize(150, 0))
        self.okno_s_perekl_btn_skip.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                                  "font: 16pt \"MS Shell Dlg 2\";color: white")
        self.okno_s_perekl_btn_skip.setObjectName("okno_s_perekl_btn_skip")
        self.gridLayout.addWidget(self.okno_s_perekl_btn_skip, 1, 2, 1, 1)
        self.okno_s_perekl_btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.okno_s_perekl_btn_next.setMinimumSize(QtCore.QSize(150, 0))
        self.okno_s_perekl_btn_next.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                                  "font: 16pt \"MS Shell Dlg 2\";color: white")
        self.okno_s_perekl_btn_next.setObjectName("okno_s_perekl_btn_next")
        self.gridLayout.addWidget(self.okno_s_perekl_btn_next, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.okno_s_perekl_image = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_s_perekl_image.sizePolicy().hasHeightForWidth())
        self.okno_s_perekl_image.setSizePolicy(sizePolicy)
        self.okno_s_perekl_image.setMinimumSize(QtCore.QSize(400, 600))
        self.okno_s_perekl_image.setStyleSheet(f"background-color: rgb(255, 255, 255);"
                                      f"background-image: url(CherectersFoto/{result_index[index]}.png)")
        self.okno_s_perekl_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.okno_s_perekl_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.okno_s_perekl_image.setObjectName("okno_s_perekl_image")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.okno_s_perekl_image)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.okno_s_perekl_name = QtWidgets.QLabel(self.okno_s_perekl_image)
        self.okno_s_perekl_name.setStyleSheet(f"color: {colors[index]} ;font: 16pt \"MS Shell Dlg 2\";"
                                              f"background-image: url(CherectersFoto/12.png)")
        self.okno_s_perekl_name.setText(f"{names[index]}")
        self.okno_s_perekl_name.setObjectName("okno_s_perekl_name")
        self.gridLayout_2.addWidget(self.okno_s_perekl_name, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_s_perekl_image, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.index = 1
        def okno_s_perekl_click():
            button = MainWindow.sender()
            if button == self.okno_s_perekl_btn_next:
                if self.index < 9:
                    self.index += 1
                    self.okno_s_perekl_image.setStyleSheet(f"background-color: rgb(255, 255, 255);"
                                                           f"background-image: url(CherectersFoto/{result_index[self.index]}.png)")
                    self.okno_s_perekl_name.setStyleSheet(f"color: {colors[self.index]} ;font: 16pt \"MS Shell Dlg 2\";"
                                                          f"background-image: url(CherectersFoto/12.png)")
                    self.okno_s_perekl_name.setText(f"{names[self.index]}")
                elif self.index == 9:
                    self.okno_all_pers(MainWindow, gacha)
            if button == self.okno_s_perekl_btn_skip:
                self.okno_all_pers(MainWindow, gacha)

        def zamena_text_in_x1():
            if zamena_texta_v_okno_s_perekl == 1:
                self.okno_s_perekl_btn_skip.setText("Заново")
                self.okno_s_perekl_btn_next.setText("Выйти")
                self.okno_s_perekl_btn_skip.clicked.connect(lambda: self.random_cherecter(1,gacha))
                self.okno_s_perekl_btn_next.clicked.connect(lambda: self.gacha_menu(MainWindow))
            else:
                self.okno_s_perekl_btn_skip.setText("Пропустить")
                self.okno_s_perekl_btn_next.setText("Далее")
                self.okno_s_perekl_btn_next.clicked.connect(okno_s_perekl_click)
                self.okno_s_perekl_btn_skip.clicked.connect(okno_s_perekl_click)
        zamena_text_in_x1()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def okno_all_pers(self, MainWindow, gacha):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url('Backgrounds/jjk_mein_menu.png');font: 18pt \"MS Shell Dlg 2\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.okno_all_pers_image_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_2.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_2.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_2.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_2.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_2.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_2.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_2.setObjectName("okno_all_pers_image_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.okno_all_pers_image_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.okno_all_pers_name_2 = QtWidgets.QLabel(self.okno_all_pers_image_2)
        self.okno_all_pers_name_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_2.setText("")
        self.okno_all_pers_name_2.setObjectName("okno_all_pers_name_2")
        self.gridLayout_4.addWidget(self.okno_all_pers_name_2, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_2, 0, 1, 1, 1)
        self.okno_all_pers_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image.setSizePolicy(sizePolicy)
        self.okno_all_pers_image.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image.setObjectName("okno_all_pers_image")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.okno_all_pers_image)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.okno_all_pers_name = QtWidgets.QLabel(self.okno_all_pers_image)
        self.okno_all_pers_name.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name.setText("")
        self.okno_all_pers_name.setObjectName("okno_all_pers_name")
        self.gridLayout_3.addWidget(self.okno_all_pers_name, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem5, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image, 0, 0, 1, 1)
        self.okno_all_pers_image_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_4.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_4.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_4.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_4.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_4.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_4.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_4.setObjectName("okno_all_pers_image_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.okno_all_pers_image_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.okno_all_pers_name_4 = QtWidgets.QLabel(self.okno_all_pers_image_4)
        self.okno_all_pers_name_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_4.setText("")
        self.okno_all_pers_name_4.setObjectName("okno_all_pers_name_4")
        self.gridLayout_6.addWidget(self.okno_all_pers_name_4, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem8, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_4, 0, 3, 1, 1)
        self.okno_all_pers_image_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_5.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_5.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_5.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_5.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_5.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_5.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_5.setObjectName("okno_all_pers_image_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.okno_all_pers_image_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.okno_all_pers_name_5 = QtWidgets.QLabel(self.okno_all_pers_image_5)
        self.okno_all_pers_name_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_5.setText("")
        self.okno_all_pers_name_5.setObjectName("okno_all_pers_name_5")
        self.gridLayout_7.addWidget(self.okno_all_pers_name_5, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_7.addItem(spacerItem11, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_5, 0, 4, 1, 1)
        self.okno_all_pers_image_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_6.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_6.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_6.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_6.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_6.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_6.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_6.setObjectName("okno_all_pers_image_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.okno_all_pers_image_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.okno_all_pers_name_6 = QtWidgets.QLabel(self.okno_all_pers_image_6)
        self.okno_all_pers_name_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_6.setText("")
        self.okno_all_pers_name_6.setObjectName("okno_all_pers_name_6")
        self.gridLayout_8.addWidget(self.okno_all_pers_name_6, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem12, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem13, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_8.addItem(spacerItem14, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_6, 1, 0, 1, 1)
        self.okno_all_pers_image_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_3.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_3.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_3.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_3.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_3.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_3.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_3.setObjectName("okno_all_pers_image_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.okno_all_pers_image_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.okno_all_pers_name_3 = QtWidgets.QLabel(self.okno_all_pers_image_3)
        self.okno_all_pers_name_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_3.setText("")
        self.okno_all_pers_name_3.setObjectName("okno_all_pers_name_3")
        self.gridLayout_5.addWidget(self.okno_all_pers_name_3, 1, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem16, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem17, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_3, 0, 2, 1, 1)
        self.okno_all_pers_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.okno_all_pers_btn_exit.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_btn_exit.setObjectName("okno_all_pers_btn_exit")
        self.gridLayout.addWidget(self.okno_all_pers_btn_exit, 2, 4, 1, 1)
        self.okno_all_pers_btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.okno_all_pers_btn_restart.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_btn_restart.setObjectName("okno_all_pers_btn_restart")
        self.gridLayout.addWidget(self.okno_all_pers_btn_restart, 2, 3, 1, 1)
        self.okno_all_pers_image_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_7.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_7.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_7.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_7.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_7.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_7.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_7.setObjectName("okno_all_pers_image_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.okno_all_pers_image_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.okno_all_pers_name_7 = QtWidgets.QLabel(self.okno_all_pers_image_7)
        self.okno_all_pers_name_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_7.setText("")
        self.okno_all_pers_name_7.setObjectName("okno_all_pers_name_7")
        self.gridLayout_9.addWidget(self.okno_all_pers_name_7, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem18, 1, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem19, 0, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_9.addItem(spacerItem20, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_7, 1, 1, 1, 1)
        self.okno_all_pers_image_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_8.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_8.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_8.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_8.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_8.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_8.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_8.setObjectName("okno_all_pers_image_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.okno_all_pers_image_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.okno_all_pers_name_8 = QtWidgets.QLabel(self.okno_all_pers_image_8)
        self.okno_all_pers_name_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_8.setText("")
        self.okno_all_pers_name_8.setObjectName("okno_all_pers_name_8")
        self.gridLayout_10.addWidget(self.okno_all_pers_name_8, 1, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem21, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem22, 0, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_10.addItem(spacerItem23, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_8, 1, 2, 1, 1)
        self.okno_all_pers_image_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_9.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_9.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_9.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_9.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_9.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_9.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_9.setObjectName("okno_all_pers_image_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.okno_all_pers_image_9)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.okno_all_pers_name_9 = QtWidgets.QLabel(self.okno_all_pers_image_9)
        self.okno_all_pers_name_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_9.setText("")
        self.okno_all_pers_name_9.setObjectName("okno_all_pers_name_9")
        self.gridLayout_11.addWidget(self.okno_all_pers_name_9, 1, 2, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem24, 1, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem25, 0, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_11.addItem(spacerItem26, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_9, 1, 3, 1, 1)
        self.okno_all_pers_image_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okno_all_pers_image_10.sizePolicy().hasHeightForWidth())
        self.okno_all_pers_image_10.setSizePolicy(sizePolicy)
        self.okno_all_pers_image_10.setMinimumSize(QtCore.QSize(200, 300))
        self.okno_all_pers_image_10.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.okno_all_pers_image_10.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.okno_all_pers_image_10.setFrameShadow(QtWidgets.QLabel.Raised)
        self.okno_all_pers_image_10.setObjectName("okno_all_pers_image_10")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.okno_all_pers_image_10)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.okno_all_pers_name_10 = QtWidgets.QLabel(self.okno_all_pers_image_10)
        self.okno_all_pers_name_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.okno_all_pers_name_10.setText("")
        self.okno_all_pers_name_10.setObjectName("okno_all_pers_name_10")
        self.gridLayout_12.addWidget(self.okno_all_pers_name_10, 1, 2, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem27, 1, 0, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem28, 0, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_12.addItem(spacerItem29, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okno_all_pers_image_10, 1, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.okno_all_pers_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        for i in (self.okno_all_pers_image,self.okno_all_pers_image_2,self.okno_all_pers_image_3,self.okno_all_pers_image_4,
                  self.okno_all_pers_image_5,self.okno_all_pers_image_6,self.okno_all_pers_image_7,self.okno_all_pers_image_8,
                  self.okno_all_pers_image_9,self.okno_all_pers_image_10):
            i.setMaximumSize(QtCore.QSize(200, 300))

        for count,i in enumerate((self.okno_all_pers_name,self.okno_all_pers_name_2,self.okno_all_pers_name_3,self.okno_all_pers_name_4,self.okno_all_pers_name_5,
                                  self.okno_all_pers_name_6,self.okno_all_pers_name_7,self.okno_all_pers_name_8,self.okno_all_pers_name_9,self.okno_all_pers_name_10)):
            i.setStyleSheet(f"color: {colors[count]} ;font: 12pt \"MS Shell Dlg 2\";"
                            f"background-image: url(CherectersFoto/12.png)")
            i.setText(f"{names[count]}")

        for e, i in enumerate((self.okno_all_pers_image, self.okno_all_pers_image_2, self.okno_all_pers_image_3,
                               self.okno_all_pers_image_4, self.okno_all_pers_image_5,
                               self.okno_all_pers_image_6,self.okno_all_pers_image_7,self.okno_all_pers_image_8,
                               self.okno_all_pers_image_9,self.okno_all_pers_image_10)):
            self.pix = QtGui.QPixmap(f"CherectersFoto/{result_index[e]}.png")
            self.pix1 = self.pix.scaled(200, 300, QtCore.Qt.KeepAspectRatio)
            i.setPixmap(self.pix1)

        self.okno_all_pers_btn_exit.clicked.connect(lambda: self.gacha_menu(MainWindow))
        self.okno_all_pers_btn_restart.clicked.connect(lambda: self.random_cherecter(10, gacha))



    def mein_menu_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jujutsu Kaisen"))
        self.main_menu_btn_exit.setText(_translate("MainWindow", "Выйти из игры"))
        self.main_menu_btn_settings.setText(_translate("MainWindow", "Настройки"))
        self.main_menu_btn_new_game.setText(_translate("MainWindow", "Начать игру"))
        self.main_menu_btn_save_game.setText(_translate("MainWindow", "Сохранить/Загрузить игру"))

    def save_menu_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save_menu_btn_save.setText(_translate("MainWindow", "Созранить/Перезаписать"))
        self.save_menu_btn_download.setText(_translate("MainWindow", "Загрузить"))
        self.save_menu_btn_hide.setText(_translate("MainWindow", "Назад"))

    def setting_menu_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setting_menu_check_resolution.setText(_translate("MainWindow", "Подтвердить"))
        self.setting_menu_windowed.setText(_translate("MainWindow", "Полноэкранный режим"))
        self.setting_menu_resolution.setItemText(0, _translate("MainWindow", "800x600"))
        self.setting_menu_resolution.setItemText(1, _translate("MainWindow", "1024x768"))
        self.setting_menu_resolution.setItemText(2, _translate("MainWindow", "1280x1024"))
        self.setting_menu_resolution.setItemText(3, _translate("MainWindow", "1360x768"))
        self.setting_menu_resolution.setItemText(4, _translate("MainWindow", "1366x768"))
        self.setting_menu_resolution.setItemText(5, _translate("MainWindow", "1600x1200"))
        self.setting_menu_resolution.setItemText(6, _translate("MainWindow", "1920x1080"))
        self.setting_menu_change_resolution.setText(_translate("MainWindow", "Применить"))
        self.setting_menu_hide.setText(_translate("MainWindow", "Назад"))

    def menu_info_pers_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.info_pers_parameters.setText(_translate("MainWindow", "Характеристики:"))
        self.info_pers_btn_exit_in_mein_menu.setText(_translate("MainWindow", "Вернуться в меню"))
        self.info_pers_btn_gacha_mein_menu.setText(_translate("MainWindow", "Крутить гачу"))
        self.info_pers_abilities.setText(_translate("MainWindow", "Способносоти:"))
        self.info_pers_btn_start_game.setText(_translate("MainWindow", "Начать игру"))
        self.info_pers_info_about_pers.setText(_translate("MainWindow", "Информация:"))
        self.info_pers_btn_evolution_pers.setText(_translate("MainWindow", "Развитие персонажа"))

    def gacha_menu_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.gacha_menu_valyta.setText(_translate("MainWindow", "Валюта: "))
        self.gacha_menu_exit.setText(_translate("MainWindow", "Выйти"))
        self.gacha_menu_btn_gacha_x10.setText(_translate("MainWindow", "Крутить гачу x10"))
        self.gacha_menu_btn_gacha_x1.setText(_translate("MainWindow", "Крутить гачу x1"))
        self.gacha_menu_tabWidget.setTabText(self.gacha_menu_tabWidget.indexOf(self.gacha_menu_tab),
                                             _translate("MainWindow", "Классическая гача"))
        self.gacha_menu_btn_gacha_x10_2.setText(_translate("MainWindow", "Крутить гачу x10"))
        self.gacha_menu_btn_gacha_x1_2.setText(_translate("MainWindow", "Крутить гачу х1"))
        self.gacha_menu_tabWidget.setTabText(self.gacha_menu_tabWidget.indexOf(self.gacha_menu_tab_2),
                                             _translate("MainWindow", "Временная гача"))

    def okno_all_pers_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.okno_all_pers_btn_exit.setText(_translate("MainWindow", "Выйти"))
        self.okno_all_pers_btn_restart.setText(_translate("MainWindow", "Заново"))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    ui = Main_menu()
    ui.main_menu(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())

