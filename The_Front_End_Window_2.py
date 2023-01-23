# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'The_Front_End_Window_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.setFixedSize(850, 600)
        SecondWindow.setStyleSheet("QMainWindow {background-image: url(app_background)}")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Lista = QtWidgets.QLabel(self.centralwidget)
        self.Lista.setGeometry(QtCore.QRect(180, 30, 541, 421))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lista.setFont(font)
        self.Lista.setAcceptDrops(False)
        self.Lista.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Lista.setAutoFillBackground(False)
        self.Lista.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.182, y1:0.176136, x2:0.518, y2:0.738727, stop:0 rgba(76, 0, 67, 255), stop:1 rgba(183, 0, 168, 255));")
        self.Lista.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.Lista.setFrameShape(QtWidgets.QFrame.Box)
        self.Lista.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Lista.setAlignment(QtCore.Qt.AlignCenter)
        self.Lista.setObjectName("Lista")
        self.Lista.setWordWrap(True)
        
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)
        
        
        
    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MusiXOXO"))
        self.Lista.setText(_translate("SecondWindow", ""))
        saved_file = open("Savefile.txt", "r")
        for line in saved_file:
            saved_line = saved_file.read()
        self.Lista.setText(saved_line)
        saved_file.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
