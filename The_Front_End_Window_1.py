# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'The_Front_End_Window_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import EasyspotifyAPI
from PyQt5 import QtCore, QtGui, QtWidgets
from The_Front_End_Window_2 import Ui_SecondWindow

class Ui_MusiXOXO(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def printData(self):
        textboxValue = str(self.textEdit.toPlainText())
        print(textboxValue)
        backend_api = EasyspotifyAPI.easy_API()
        # print(backend_api.get_artist_song(textboxValue))
        # backend_api.get_artist_id()
        to_print = backend_api.get_recomendation( backend_api.get_artist_id(backend_api.get_artist_song(textboxValue)), None ,10 )
        save_file = open("Savefile.txt", "w")
        for i in to_print :
            save_file.write(f"{i['song_name']} ")
            save_file.write(f"{i['artist'] } ")
            save_file.write(f"{i['link'] } \n")
        save_file.close()
        self.openWindow()                 
        
    def setupUi(self, MusiXOXO):
        MusiXOXO.setObjectName("MusiXOXO")
        MusiXOXO.resize(843, 600)
        MusiXOXO.setStyleSheet("QMainWindow {background-image: url(app_background)}")
        self.centralwidget = QtWidgets.QWidget(MusiXOXO)
        self.centralwidget.setObjectName("centralwidget")
        self.Przywitanie = QtWidgets.QLabel(self.centralwidget)
        self.Przywitanie.setGeometry(QtCore.QRect(200, 30, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Przywitanie.setFont(font)
        self.Przywitanie.setAcceptDrops(False)
        self.Przywitanie.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Przywitanie.setAutoFillBackground(False)
        self.Przywitanie.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.182, y1:0.176136, x2:0.518, y2:0.738727, stop:0 rgba(76, 0, 67, 255), stop:1 rgba(183, 0, 168, 255));")
        self.Przywitanie.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.Przywitanie.setFrameShape(QtWidgets.QFrame.Box)
        self.Przywitanie.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Przywitanie.setAlignment(QtCore.Qt.AlignCenter)
        self.Przywitanie.setObjectName("Przywitanie")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(113, 210, 581, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.182, y1:0.176136, x2:0.518, y2:0.738727, stop:0 rgba(76, 0, 67, 255), stop:1 rgba(183, 0, 168, 255));\n"
"border-color: rgb(0, 0, 0);")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")      
       # str(textboxValue)
       # backend_api = EasyspotifyAPI.easy_API()

       # backend_api.get_track_id(textboxValue)

       # to_print = backend_api.get_recomendation( backend_api.get_artist_id(textboxValue), None ,10 )
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.printData())
        self.pushButton.setGeometry(QtCore.QRect(340, 360, 121, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.182, y1:0.176136, x2:0.518, y2:0.738727, stop:0 rgba(76, 0, 67, 255), stop:1 rgba(183, 0, 168, 255));\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        MusiXOXO.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MusiXOXO)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menubar.setObjectName("menubar")
        MusiXOXO.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MusiXOXO)
        self.statusbar.setObjectName("statusbar")
        MusiXOXO.setStatusBar(self.statusbar)

        self.retranslateUi(MusiXOXO)
        QtCore.QMetaObject.connectSlotsByName(MusiXOXO)

    def retranslateUi(self, MusiXOXO):
        _translate = QtCore.QCoreApplication.translate
        MusiXOXO.setWindowTitle(_translate("MusiXOXO", "MusiXOXO"))
        self.Przywitanie.setText(_translate("MusiXOXO", "Welcome to MusiXOXO"))
        self.textEdit.setPlaceholderText(_translate("MusiXOXO", "Insert: Artist - Track"))
        self.pushButton.setText(_translate("MusiXOXO", "Szukaj"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusiXOXO = QtWidgets.QMainWindow()
    ui = Ui_MusiXOXO()
    ui.setupUi(MusiXOXO)
    MusiXOXO.show()
    sys.exit(app.exec_())
    
