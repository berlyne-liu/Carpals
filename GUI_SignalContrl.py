# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from GUI_Carpals_carpals import *
from GUI_Carpals_Alarm import *


class Ui_signalContrl(Ui_carpals, Ui_alarm):
    def __init__(self):
        Ui_carpals.__init__(self)
        Ui_alarm.__init__(self)
        self.carpals_setupUi()
        self.alarm_setupUi()
        self.fm = FileModify()
        self.list_i = self.fm.contrl_tablename()
        self.file_path1 = None
        self.file_path2 = None
        self.file_path3 = None
        self.file_path4 = None
        self.file_path5 = None

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
        self.init_combobox(1, *self.list_i)
        self.init_combobox(2, *self.list_i)
        self.init_combobox(3, *self.list_i)
        self.init_combobox(4, *self.list_i)
        # combobox点击时刷新下拉菜单，每个下拉菜单选择后，后选的combobox不会重复出现选项
        self.comboBox.activated[int].connect(lambda: self.on_combo_activated(1))
        self.comboBox_2.activated[int].connect(lambda: self.on_combo_activated(2))
        self.comboBox_3.activated[int].connect(lambda: self.on_combo_activated(3))
        self.comboBox_4.activated[int].connect(lambda: self.on_combo_activated(4))

        self.pushButton_1.released.connect(lambda: self.button_click())
        self.lineEdit_1.textChanged.connect(lambda: self.line_change(1))
        self.lineEdit_2.textChanged.connect(lambda: self.line_change(2))
        self.lineEdit_3.textChanged.connect(lambda: self.line_change(3))
        self.lineEdit_4.textChanged.connect(lambda: self.line_change(4))

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

    def init_combobox(self, n, *args):
        """
        init_combobox方法用于初始化combobox的可选项item,将数据库可用表名在初始化时赋值到item
        :param n: 用于识别对应的combobox被点击
        :param args: 传入列表元素，增加到combobox的item上
        :return: 无返回值
        """
        list_o = args
        if n == 1:
            self.comboBox.clear()
            self.comboBox.addItems(list_o)
            # 设置comboBox的默认值为空，
            self.comboBox.setCurrentIndex(-1)
        elif n == 2:
            self.comboBox_2.clear()
            self.comboBox_2.addItems(list_o)
            # 设置comboBox的默认值为空，
            self.comboBox_2.setCurrentIndex(-1)
        elif n == 3:
            self.comboBox_3.clear()
            self.comboBox_3.addItems(list_o)
            # 设置comboBox的默认值为空，
            self.comboBox_3.setCurrentIndex(-1)
        elif n == 4:
            self.comboBox_4.clear()
            self.comboBox_4.addItems(list_o)
            # 设置comboBox的默认值为空，
            self.comboBox_4.setCurrentIndex(-1)

    def on_combo_activated(self, n):
        list_d = self.list_i
        nums = []
        coms = list(range(1, 5))
        c1 = self.comboBox.currentText()
        c2 = self.comboBox_2.currentText()
        c3 = self.comboBox_3.currentText()
        c4 = self.comboBox_4.currentText()
        list_c = [c1, c2, c3, c4]
        print(list_d + list_c)
        list_d = [item1 for item1 in list_d if not item1 in list_c]
        print('循环后：' + str(list_d))
        # print(n)
        for c in list_c:
            if c != '':
                num = list_c.index(c) + 1
                nums.append(num)
        ref = [item2 for item2 in coms if not item2 in nums]
        for r in ref:
            # print(r)
            self.init_combobox(r, *list_d)

    def check_samefile(self):
        # 判断是否重复选择文件,以字典形式保存lineEdit与comboBox的对应关系

        dic = {self.lineEdit_1.text(): self.comboBox.currentText(),
               self.lineEdit_2.text(): self.comboBox_2.currentText(),
               self.lineEdit_3.text(): self.comboBox_3.currentText(),
               self.lineEdit_4.text(): self.comboBox_4.currentText()}
        print(dic)
        pass

    def table_view(self):
        fm = FileModify()
        title, data = fm.contrl_sqlcheck()
        print(enumerate(data))
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(title)
        for row, data in enumerate(data):
            for column, item in enumerate(data):
                i = QStandardItem(str(item)) if item is not None else QStandardItem('')
                self.model.setItem(row, column, i)
        self.tableView.setModel(self.model)

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
