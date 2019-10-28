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
        # ******************以下是控件的创建******************* #
        self.frame_a = QtWidgets.QFrame(self.centralwidget)
        self.lineEdit_a1 = QtWidgets.QLineEdit(self.frame_a)

        # ******************以下是控件尺寸定义******************* #
        self.frame_a.setGeometry(QtCore.QRect(0, 0, 725, 635))
        self.lineEdit_a1.setGeometry(QtCore.QRect(20, 10, 170, 20))

        # ******************以下是控件属性定义******************* #
        self.frame_a.setEnabled(True)
        self.frame_a.setHidden(True)
        self.frame_a.setAutoFillBackground(False)
        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_a.setObjectName("frame_a")
        self.lineEdit_a1.setObjectName("lineEdit_a1")
        self.carpals_retranslateUi()

    def alarm_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
