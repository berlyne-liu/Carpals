# -*- coding: utf-8 -*-

import sqlite3
import sys

from PySqlite import SqliteModify
from PyFile import FileModify
import pickle
import GUI_Carpals_test
from GUI_Carpals_test import *
from GUI_Carpals_carpals import *
from GUI_SignalContrl import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_signalContrl()
    ui.setupUi(mainWindow)
    ui.carpals_setupUi()
    ui.alarm_setupUi()
    ui.QtWidget_Funtion()
    mainWindow.show()
    sys.exit(app.exec_())
