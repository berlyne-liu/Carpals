# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QListView
from GUI_Carpals_test import *


class Ui_alarm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def alarm_setupUi(self):
        self.frame_a = QtWidgets.QFrame(self.centralwidget)
        self.lineEdit_a1 = QtWidgets.QLineEdit(self.frame_a)
        self.toolButton_a1 = QtWidgets.QToolButton(self.frame_a)
        self.pushButton_a1 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a2 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a3 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a4 = QtWidgets.QPushButton(self.frame_a)
        self.comboBox_a1 = QtWidgets.QComboBox(self.frame_a)
        self.listView_a1 = QtWidgets.QListView(self.frame_a)
        self.tableView_a1 = QtWidgets.QTableView(self.frame_a)

        self.frame_a.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.lineEdit_a1.setGeometry(QtCore.QRect(20, 30, 590, 30))
        self.toolButton_a1.setGeometry(QtCore.QRect(610, 30, 30, 30))
        self.pushButton_a1.setGeometry(QtCore.QRect(480, 190, 200, 40))
        self.pushButton_a2.setGeometry(QtCore.QRect(690, 190, 200, 40))
        self.pushButton_a3.setGeometry(QtCore.QRect(860, 30, 30, 30))
        self.pushButton_a4.setGeometry(QtCore.QRect(270, 190, 200, 40))
        self.comboBox_a1.setGeometry(QtCore.QRect(650, 30, 200, 30))
        self.listView_a1.setGeometry(QtCore.QRect(930, 30, 520, 210))
        self.tableView_a1.setGeometry(QtCore.QRect(10, 260, 1480, 560))

        # self.frame_a.setObjectName("frame_a")
        # self.lineEdit_a1.setObjectName("lineEdit_a1")
        # self.toolButton_a1.setObjectName("toolButton_a1")
        # self.listView_a1.setObjectName("listView_a1")
        # self.tableView_a1.setObjectName("tableView_a1")
        # self.pushButton_a4.setObjectName("pushButton_a4")
        # self.pushButton_a5.setObjectName("pushButton_a5")

        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_a.setEnabled(True)
        self.frame_a.setHidden(True)
        self.frame_a.setAutoFillBackground(False)
        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolButton_a1.setIcon(self.icon)
        self.lineEdit_a1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listView_a1.setViewMode(QListView.ListMode)
        self.listView_a1.setResizeMode(QListView.Adjust)
        self.listView_a1.setContextMenuPolicy(3)
        self.alarm_retranslateUi()

    def alarm_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.toolButton_a1.setText(_translate("MainWindow", "文件"))
        self.pushButton_a1.setText(_translate("MainWindow", "初始化界面"))
        self.pushButton_a2.setText(_translate("MainWindow", "生成告警表"))
        self.pushButton_a3.setText(_translate("MainWindow", ">>"))
        self.pushButton_a4.setText(_translate("MainWindow", "清空数据表"))


