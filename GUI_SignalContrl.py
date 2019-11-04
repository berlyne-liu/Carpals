# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import QStringListModel, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu
import os

from GUI_Carpals_carpals import *
from GUI_Carpals_Alarm import *
from Logic_Sqlite_Modify import *


class Ui_signalContrl(Ui_carpals, Ui_alarm):
    def __init__(self):
        Ui_carpals.__init__(self)
        Ui_alarm.__init__(self)
        self.model = QStandardItemModel()
        self.connect = sqlite3.connect('Carpals.db')
        self.sm = Sqlite_Modify(self.connect)
        self.carpals_setupUi()
        self.alarm_setupUi()
        self.fm = FileModify()
        self.list_i = self.fm.contrl_tablename()
        self.file_path1 = None
        self.file_path2 = None
        self.file_path3 = None
        self.file_path4 = None
        self.file_path5 = None
        self.Path4 = "/check_01.sql"
        self.add_list = []
        self.dic_add = {}

    def QtWidget_Funtion(self):
        self.action.triggered.connect(lambda: self.frame_init(1))
        self.action_2.triggered.connect(lambda: self.frame_init(2))
        self.action_3.triggered.connect(lambda: self.frame_init(3))
        self.action_4.triggered.connect(lambda: self.frame_init(4))
        self.action_5.triggered.connect(lambda: self.frame_init(5))

        # toolbutton点击后（鼠标点击释放），打开文件目录
        self.toolButton_1.released.connect(lambda: self.openfile(1))
        self.toolButton_2.released.connect(lambda: self.openfile(2))
        self.toolButton_3.released.connect(lambda: self.openfile(3))
        self.toolButton_4.released.connect(lambda: self.openfile(4))
        self.toolButton_a1.released.connect(lambda: self.openfile(5))

        # Combobox 初始化：加入数据库的中的表名
        self.combobox_init(self.comboBox, reg_name="Carpals")
        self.combobox_init(self.comboBox_2, reg_name="Carpals")
        self.combobox_init(self.comboBox_3, reg_name="Carpals")
        self.combobox_init(self.comboBox_4, reg_name="Carpals")
        self.combobox_init(self.comboBox_a1, reg_name="Alarm")

        # combobox点击时刷新下拉菜单，每个下拉菜单选择后，后选的combobox不会重复出现选项
        self.comboBox.activated[int].connect(lambda: self.on_combo_activated(1))
        self.comboBox_2.activated[int].connect(lambda: self.on_combo_activated(2))
        self.comboBox_3.activated[int].connect(lambda: self.on_combo_activated(3))
        self.comboBox_4.activated[int].connect(lambda: self.on_combo_activated(4))

        self.listView_a1.customContextMenuRequested[QPoint].connect(self.listWidgetContext)

        self.pushButton_1.released.connect(lambda: self.button_click())
        self.pushButton_a2.released.connect(lambda: self.Alarm_Generated())
        self.pushButton_a3.released.connect(lambda: self.addToList())
        self.pushButton_a4.released.connect(lambda: self.Alarm_removedata())
        self.lineEdit_1.textChanged.connect(lambda: self.line_change(1))
        self.lineEdit_2.textChanged.connect(lambda: self.line_change(2))
        self.lineEdit_3.textChanged.connect(lambda: self.line_change(3))
        self.lineEdit_4.textChanged.connect(lambda: self.line_change(4))

    def combobox_init(self, widget, reg_name=None):
        container = []
        sq = self.sm.sqlite_query("check_01.sql")
        for num, rows in enumerate(sq):
            if rows[0][:rows[0].index("_")] == reg_name:
                container.append(rows[0])
        # print(container)
        if len(container):
            widget.clear()
            widget.addItems(container)
            widget.setCurrentIndex(-1)
        else:
            widget.clear()
            widget.addItem("数据库无相关表数据")
            # widget.setCurrentIndex(-1)

    def frame_init(self, n):
        if n == 1:
            self.frame.setHidden(True)
            self.frame_a.setHidden(True)
        elif n == 2:
            self.frame.setHidden(True)
            self.frame_a.setHidden(True)
        elif n == 3:
            self.frame.setHidden(False)
            self.frame_a.setHidden(True)
        elif n == 4:
            self.frame.setHidden(True)
            self.frame_a.setHidden(True)
        elif n == 5:
            self.frame.setHidden(True)
            self.frame_a.setHidden(False)

    def openfile(self, n):
        """
        openfile 是tool button点击后的实例方法
        功能：点击tool button后打开文件目录
        参数：n,用于将tool button与line Eidt对应起来
        """
        openfile_name = QFileDialog.getOpenFileName(self.centralwidget, '选择文件', '')
        file_name = openfile_name[0].split("/")[-1]
        print('linetext_{0}被输入数据：'.format(n) + openfile_name[0])
        print('文件名为：' + file_name)
        if n == 1:
            print(self.lineEdit_1.text())
            self.lineEdit_1.setText(openfile_name[0])
            self.file_path1 = openfile_name[0]
            # print(self.file_path1)
        elif n == 2:
            self.lineEdit_2.setText(openfile_name[0])
            self.file_path2 = openfile_name[0]
        elif n == 3:
            self.lineEdit_3.setText(openfile_name[0])
            self.file_path3 = openfile_name[0]
        elif n == 4:
            self.lineEdit_4.setText(openfile_name[0])
            self.file_path4 = openfile_name[0]
        elif n == 5:
            self.lineEdit_a1.setText(openfile_name[0])
            self.file_path5 = openfile_name[0]

    def button_click(self):
        dic = {self.lineEdit_1.text(): self.comboBox.currentText(),
               self.lineEdit_2.text(): self.comboBox_2.currentText(),
               self.lineEdit_3.text(): self.comboBox_3.currentText(),
               self.lineEdit_4.text(): self.comboBox_4.currentText()}
        f_m = FileModify()
        f_m.contrl_sqlinsert(**dic)
        self.table_view()
        # self.check_samefile()

    def addToList(self):
        add_path = self.lineEdit_a1.text()
        add_table = self.comboBox_a1.currentText()
        self.dic_add[add_path] = add_table
        print(self.dic_add)
        add_str = "将文件：" + str(add_path.split("/")[-1]) + "导入数据库：" + str(add_table)
        self.add_list.append(add_str)
        slm = QStringListModel()
        slm.setStringList(self.add_list)
        self.listView_a1.setModel(slm)

    def listWidgetContext(self, point):
        popMenu = QMenu()
        popMenu.addAction("更新")
        popMenu.addAction("修改")
        popMenu.addAction("删除")
        popMenu.exec_(QCursor.pos())

    def Alarm_Generated(self):
        Ae = Alarm_Extraction()
        for (path, table) in self.dic_add.items():
            # filetype = str(path).split(".")[-1]
            filetype = os.path.splitext(path)[-1]
            # print(filetype)
            if filetype.lower() == ".csv":
                hea, cont, err = Ae.csvExtraction(path)
                self.sm.sqlite_insert(hea, cont, table=table)
            elif filetype.lower() == ".xlsx":
                hea, cont, err = Ae.excelExtraction(path)
                self.sm.sqlite_insert(hea, cont, table=table)
            elif filetype.find(".") == -1:
                print(filetype.find("."))
                hea, cont, err = Ae.textExtraction(path)
                self.sm.sqlite_insert(hea, cont, table=table)
            else:
                print("文件错误")
        result = self.sm.sqlite_query("Alarm_sql.sql")
        self.table_view(self.tableView_a1, result)

    def Alarm_removedata(self):
        self.sm.sqlite_query(operation="delete", configure="Alarm")

    # def on_combo_activated(self, n):
    #     list_d = self.list_i
    #     nums = []
    #     coms = list(range(1, 5))
    #     c1 = self.comboBox.currentText()
    #     c2 = self.comboBox_2.currentText()
    #     c3 = self.comboBox_3.currentText()
    #     c4 = self.comboBox_4.currentText()
    #     list_c = [c1, c2, c3, c4]
    #     print(list_d + list_c)
    #     list_d = [item1 for item1 in list_d if not item1 in list_c]
    #     print('循环后：' + str(list_d))
    #     # print(n)
    #     for c in list_c:
    #         if c != '':
    #             num = list_c.index(c) + 1
    #             nums.append(num)
    #     ref = [item2 for item2 in coms if not item2 in nums]
    #     for r in ref:
    #         # print(r)
    #         self.init_combobox(r, *list_d)

    def check_samefile(self):
        # 判断是否重复选择文件,以字典形式保存lineEdit与comboBox的对应关系
        dic = {self.lineEdit_1.text(): self.comboBox.currentText(),
               self.lineEdit_2.text(): self.comboBox_2.currentText(),
               self.lineEdit_3.text(): self.comboBox_3.currentText(),
               self.lineEdit_4.text(): self.comboBox_4.currentText()}
        print(dic)
        pass

    def table_view(self, widget, result):
        desc = self.sm.cur.description
        print(desc)
        h = [data[0] for data in desc]
        self.model.setHorizontalHeaderLabels(h)
        print(result)
        for row, data in enumerate(result):
            for column, item in enumerate(data):
                i = QStandardItem(str(item)) if item is not None else QStandardItem('')
                self.model.setItem(row, column, i)
        widget.setModel(self.model)

    def line_change(self, n):
        line_item = [self.lineEdit_1.text(),
                     self.lineEdit_2.text(),
                     self.lineEdit_3.text(),
                     self.lineEdit_4.text()
                     ]
        # 去line_item中的除空值
        line_item = [var for var in line_item if var != '']
        if len(line_item) != len(set(line_item)):
            print("重复选择文件，请重新选择")
            print(len(line_item))
            print(len(set(line_item)))
            if n == 1:
                self.lineEdit_1.clear()
            elif n == 2:
                self.lineEdit_2.clear()
            elif n == 3:
                self.lineEdit_3.clear()
            elif n == 4:
                self.lineEdit_4.clear()
        else:
            if n == 1:
                c_item = self.fm.match_header(self.lineEdit_1.text())
                # print(c_item)
                self.comboBox.setCurrentText(c_item)
            elif n == 2:
                c_item = self.fm.match_header(self.lineEdit_2.text())
                self.comboBox_2.setCurrentText(c_item)
            elif n == 3:
                c_item = self.fm.match_header(self.lineEdit_3.text())
                self.comboBox_3.setCurrentText(c_item)
            elif n == 4:
                c_item = self.fm.match_header(self.lineEdit_4.text())
                self.comboBox_4.setCurrentText(c_item)
