# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QFileDialog, QApplication, QStyleFactory
from PyFile import *


class Ui_MainWindow(object):
    # def __init__(self):
    #     self.fm = FileModify()
    #     self.list_i = self.fm.contrl_tablename()
    #     self.file_path1 = None
    #     self.file_path2 = None
    #     self.file_path3 = None
    #     self.file_path4 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        # palette = QtGui.QPalette()
        # MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu2_1 = QtWidgets.QMenu(self.menu_2)
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.action = QtWidgets.QAction(MainWindow)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_5 = QtWidgets.QAction(MainWindow)

        MainWindow.resize(1500, 900)
        # brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 70))
        self.menu.setGeometry(QtCore.QRect(256, 129, 120, 70))

        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))

        self.centralwidget.setObjectName("centralwidget")
        self.menubar.setObjectName("menubar")
        self.menu.setObjectName("menu")
        self.menu_2.setObjectName("menu_2")
        self.menu2_1.setObjectName("menu2_1")
        self.menu_3.setObjectName("menu_3")
        self.statusbar.setObjectName("statusbar")
        self.action.setObjectName("action")
        self.action_2.setObjectName("action_2")
        self.action_3.setObjectName("action_3")
        self.action_4.setObjectName("action_4")
        self.action_5.setObjectName("action_5")

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.menu2_1.menuAction())
        self.menu2_1.addAction(self.action_3)
        self.menu2_1.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.menubar.setEnabled(True)
        self.menubar.setTabletTracking(False)
        self.menubar.setDefaultUp(False)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("File.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网优日常小工具-专用版"))
        self.menu.setTitle(_translate("MainWindow", "数据空间"))
        self.action.setText(_translate("MainWindow", "初始化"))
        self.action_2.setText(_translate("MainWindow", "清理数据库"))
        self.menu_2.setTitle(_translate("MainWindow", "指标体系"))
        self.menu2_1.setTitle(_translate("MainWindow", "导入数据"))
        self.action_3.setText(_translate("MainWindow", "固定格式导入"))
        self.action_4.setText(_translate("MainWindow", "自定义格式导入"))
        self.menu_3.setTitle(_translate("MainWindow", "告警处理"))
        self.action_5.setText(_translate("MainWindow", "LTE告警解析"))

