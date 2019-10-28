# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow
from GUI_Carpals_test import *


class Ui_alarm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def alarm_setupUi(self):
        self.centralwidget.setObjectName("centralwidget")
        self.frame_a = QtWidgets.QFrame(self.centralwidget)
        self.frame_a.setGeometry(QtCore.QRect(0, 0, 725, 635))
        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_a.setObjectName("frame_a")
        self.lineEdit_a1 = QtWidgets.QLineEdit(self.frame_a)
        self.lineEdit_a1.setGeometry(QtCore.QRect(40, 50, 281, 31))
        self.lineEdit_a1.setObjectName("lineEdit_a1")
        self.toolButton_a1 = QtWidgets.QToolButton(self.frame_a)
        self.toolButton_a1.setGeometry(QtCore.QRect(290, 50, 31, 31))
        self.toolButton_a1.setObjectName("toolButton_a1")
        self.listView_a1 = QtWidgets.QListView(self.frame_a)
        self.listView_a1.setGeometry(QtCore.QRect(440, 30, 281, 211))
        self.listView_a1.setObjectName("listView_a1")
        self.pushButton_a1 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a1.setGeometry(QtCore.QRect(730, 40, 41, 41))
        self.pushButton_a1.setObjectName("pushButton_a1")
        self.pushButton_a2 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a2.setGeometry(QtCore.QRect(730, 100, 41, 41))
        self.pushButton_a2.setObjectName("pushButton_a2")
        self.pushButton_a3 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a3.setGeometry(QtCore.QRect(730, 160, 41, 41))
        self.pushButton_a3.setObjectName("pushButton_a3")
        self.tableView_a1 = QtWidgets.QTableView(self.frame_a)
        self.tableView_a1.setGeometry(QtCore.QRect(20, 260, 761, 271))
        self.tableView_a1.setObjectName("tableView_a1")
        self.pushButton_a4 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a4.setGeometry(QtCore.QRect(190, 190, 111, 41))
        self.pushButton_a4.setObjectName("pushButton_a4")
        self.pushButton_a5 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a5.setGeometry(QtCore.QRect(310, 190, 111, 41))
        self.pushButton_a5.setObjectName("pushButton_a5")
        self.frame_a.setEnabled(True)
        self.frame_a.setHidden(True)
        self.frame_a.setAutoFillBackground(False)
        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alarm_retranslateUi()

    def alarm_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.toolButton_a1.setText(_translate("MainWindow", "..."))
        self.pushButton_a1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_a2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_a3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_a4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_a5.setText(_translate("MainWindow", "PushButton"))


