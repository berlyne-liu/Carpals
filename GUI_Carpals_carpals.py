# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QHeaderView
from GUI_Carpals_test import *


class Ui_carpals(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def carpals_setupUi(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tab = QtWidgets.QWidget(self.frame)
        self.tab_2 = QtWidgets.QWidget(self.frame)
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.toolButton_1 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)

        self.frame.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 10, 170, 20))
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 170, 20))
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 70, 170, 20))
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 100, 170, 20))
        self.comboBox.setGeometry(QtCore.QRect(210, 10, 120, 20))
        self.comboBox_2.setGeometry(QtCore.QRect(210, 40, 120, 20))
        self.comboBox_3.setGeometry(QtCore.QRect(210, 70, 120, 20))
        self.comboBox_4.setGeometry(QtCore.QRect(210, 100, 120, 20))
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 650, 550))
        self.tableView.setGeometry(QtCore.QRect(0, 0, 650, 550))
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 650, 550))
        self.toolButton_1.setGeometry(QtCore.QRect(170, 10, 20, 20))
        self.toolButton_2.setGeometry(QtCore.QRect(170, 40, 20, 20))
        self.toolButton_3.setGeometry(QtCore.QRect(170, 70, 20, 20))
        self.toolButton_4.setGeometry(QtCore.QRect(170, 100, 20, 20))
        self.pushButton_1.setGeometry(QtCore.QRect(340, 80, 80, 40))
        self.pushButton_2.setGeometry(QtCore.QRect(430, 80, 80, 40))
        self.frame.setEnabled(True)
        self.frame.setHidden(True)
        self.frame.setAutoFillBackground(False)
        self.tabWidget.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame.setObjectName("frame")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.setStyleSheet("color: rgb(0, 0 , 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab.setObjectName("tab")
        self.tab_2.setObjectName("tab_2")
        self.tableView.setObjectName("tableView")
        self.tableView_2.setObjectName("tableView_2")
        self.toolButton_1.setObjectName("toolButton_1")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton_1.setObjectName("pushButton")

        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.toolButton_1.setIcon(self.icon)
        self.toolButton_2.setIcon(self.icon)
        self.toolButton_3.setIcon(self.icon)
        self.toolButton_4.setIcon(self.icon)
        self.toolButton_1.setAutoRaise(True)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_4.setAutoRaise(True)

        self.tableView.horizontalHeader().setStretchLastSection(True)  # 最后一列决定充满剩下的界面
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.carpals_retranslateUi()
        self.tabWidget.setCurrentIndex(1)

    def carpals_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.toolButton_1.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_1.setText(_translate("MainWindow", "导入"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))
