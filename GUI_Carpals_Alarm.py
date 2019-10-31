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
        self.frame_a = QtWidgets.QFrame(self.centralwidget)
        self.lineEdit_a1 = QtWidgets.QLineEdit(self.frame_a)
        self.toolButton_a1 = QtWidgets.QToolButton(self.frame_a)
        self.pushButton_a1 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a2 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a3 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a4 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a5 = QtWidgets.QPushButton(self.frame_a)
        self.pushButton_a6 = QtWidgets.QPushButton(self.frame_a)
        self.comboBox_a1 = QtWidgets.QComboBox(self.frame_a)
        self.listView_a1 = QtWidgets.QListView(self.frame_a)
        self.tableView_a1 = QtWidgets.QTableView(self.frame_a)

        self.frame_a.setGeometry(QtCore.QRect(0, 0, 725, 635))
        self.lineEdit_a1.setGeometry(QtCore.QRect(10, 30, 261, 30))
        self.toolButton_a1.setGeometry(QtCore.QRect(260, 30, 30, 30))
        self.pushButton_a1.setGeometry(QtCore.QRect(670, 40, 40, 40))
        self.pushButton_a2.setGeometry(QtCore.QRect(670, 100, 40, 40))
        self.pushButton_a3.setGeometry((QtCore.QRect(670, 160, 40, 40)))
        self.pushButton_a4.setGeometry(QtCore.QRect(190, 190, 110, 40))
        self.pushButton_a5.setGeometry(QtCore.QRect(310, 190, 110, 40))
        self.pushButton_a6.setGeometry(QtCore.QRect(395, 30, 30, 30))
        self.comboBox_a1.setGeometry(QtCore.QRect(295, 30, 95, 30))
        self.listView_a1.setGeometry(QtCore.QRect(430, 30, 220, 210))
        self.tableView_a1.setGeometry(QtCore.QRect(10, 260, 705, 320))

        # self.frame_a.setObjectName("frame_a")
        # self.lineEdit_a1.setObjectName("lineEdit_a1")
        # self.toolButton_a1.setObjectName("toolButton_a1")
        # self.listView_a1.setObjectName("listView_a1")
        # self.pushButton_a1.setObjectName("pushButton_a1")
        # self.pushButton_a2.setObjectName("pushButton_a2")
        # self.pushButton_a3.setObjectName("pushButton_a3")
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
        self.alarm_retranslateUi()

    def alarm_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.toolButton_a1.setText(_translate("MainWindow", "文件"))
        self.pushButton_a1.setText(_translate("MainWindow", "删除"))
        self.pushButton_a2.setText(_translate("MainWindow", "修改"))
        self.pushButton_a3.setText(_translate("MainWindow", "导入"))
        self.pushButton_a4.setText(_translate("MainWindow", "清空"))
        self.pushButton_a5.setText(_translate("MainWindow", "查询"))
        self.pushButton_a6.setText(_translate("MainWindow", ">>"))


