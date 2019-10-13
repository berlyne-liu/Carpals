# -*- coding: utf-8 -*-
#
#
#
#


import sqlite3
from PySqlite import SqliteModify
from PyFile import FileModify
import pickle
import GUI_Carpals_test
from GUI_Carpals_test import *

if __name__ == '__main__':
    # filepath_2 = GUI_Carpals_test.Ui_MainWindow.lineEdit_1.text()
    # filepath_1 = u"F:\\PycharmProjects\\Carpals\\09110917\\LTE话务流量.csv"
    # filepath_3 = u"F:\\PycharmProjects\\Carpals\\09110917\\益阳GSM.CSV"
    # filepath_4 = u"F:\\PycharmProjects\\Carpals\\09110917\\益阳GSM.CSV"
    # filepath_5 = u"F:\\PycharmProjects\\Carpals\\09110917\\益阳GSM.CSV"

    # query_1 = "select count(*) from LTE_Traffic"
    # query_2 = "select count(*) from GSM_Traffic_Y"

    # conn = sqlite3.connect('Carpals.db')
    # modify = SqliteModify(conn)
    # print(filepath_2)
    # modify.sqlite_creat(*LTE_Traffic, table='LTE_Traffic')
    # modify.sqlite_creat(*GSM_Traffic_Y, table='GSM_Traffic_Y')
    # modify.sqlite_insert(filepath_1, "LTE_Traffic")
    # modify.sqlite_insert(filepath_2, "GSM_Traffic_Y")
    # modify.sqlite_output(query_1)
    # modify.sqlite_output(query_2)
    # query = modify.sqlite_check('指标体系-综合版业务.sql')
    # print(query)
    # modify.sqlite_output(query)

    # dic = FileModify().to_load(file='header')
    # print(type(dic))
    # for key, value in dic.items():
    #     # modify.sqlite_creat(*value, table=key)
    #     print(key + ':' + str(value))
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.Qweiget_function()
    mainWindow.show()
    sys.exit(app.exec_())
