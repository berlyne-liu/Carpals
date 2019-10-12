# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QFileDialog, QHeaderView
from PyFile import *


class Ui_MainWindow(object):
    def __init__(self):
        self.fm = FileModify()
        self.list_i = self.fm.contrl_tablename()
        self.file_path1 = None
        self.file_path2 = None
        self.file_path3 = None
        self.file_path4 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        palette = QtGui.QPalette()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.tab = QtWidgets.QWidget()
        self.tab_2 = QtWidgets.QWidget()
        self.menu = QtWidgets.QMenu(self.menubar)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.toolButton_1 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame)
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)

        MainWindow.resize(725, 635)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        self.menu.setGeometry(QtCore.QRect(256, 129, 120, 50))
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 23))
        self.frame.setGeometry(QtCore.QRect(0, 0, 725, 635))
        self.comboBox.setGeometry(QtCore.QRect(210, 10, 120, 21))
        self.comboBox_2.setGeometry(QtCore.QRect(210, 40, 120, 21))
        self.comboBox_3.setGeometry(QtCore.QRect(210, 70, 120, 21))
        self.comboBox_4.setGeometry(QtCore.QRect(210, 100, 120, 21))
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 10, 171, 21))
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 171, 21))
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 70, 171, 21))
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 100, 171, 21))
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 650, 550))
        self.toolButton_2.setGeometry(QtCore.QRect(170, 40, 21, 21))
        self.toolButton_3.setGeometry(QtCore.QRect(170, 70, 21, 21))
        self.toolButton_4.setGeometry(QtCore.QRect(170, 100, 21, 21))
        self.toolButton_1.setGeometry(QtCore.QRect(170, 10, 21, 21))
        self.pushButton_1.setGeometry(QtCore.QRect(340, 80, 81, 41))
        self.tableView.setGeometry(QtCore.QRect(0, 0, 650, 550))
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 650, 550))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.centralwidget.setObjectName("centralwidget")
        self.frame.setObjectName("frame")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.setObjectName("tabWidget")
        self.tableView.setObjectName("tableView")
        self.tableView_2.setObjectName("tableView_2")
        self.tab.setObjectName("tab")
        self.tab_2.setObjectName("tab_2")
        self.toolButton_1.setObjectName("toolButton_1")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton_1.setObjectName("pushButton")
        self.menubar.setObjectName("menubar")
        self.menu.setObjectName("menu")
        self.statusbar.setObjectName("statusbar")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("File.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        MainWindow.setAcceptDrops(True)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        self.tabWidget.setAutoFillBackground(True)
        self.toolButton_1.setAutoRaise(True)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_1.setIcon(icon)
        self.toolButton_2.setIcon(icon)
        self.toolButton_3.setIcon(icon)
        self.toolButton_4.setIcon(icon)
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.setEnabled(True)
        self.menubar.setTabletTracking(False)
        self.menubar.setDefaultUp(False)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tableView.horizontalHeader().setStretchLastSection(True)  # 最后一列决定充满剩下的界面
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)

        # toolbutton点击后（鼠标点击释放），打开文件目录
        self.toolButton_1.released.connect(lambda: self.openfile(1))
        self.toolButton_2.released.connect(lambda: self.openfile(2))
        self.toolButton_3.released.connect(lambda: self.openfile(3))
        self.toolButton_4.released.connect(lambda: self.openfile(4))

        # combobox点击时刷新下拉菜单，每个下拉菜单选择后，后选的combobox不会重复出现选项
        self.comboBox.activated[int].connect(lambda: self.on_combo_activated(1))
        self.comboBox_2.activated[int].connect(lambda: self.on_combo_activated(2))
        self.comboBox_3.activated[int].connect(lambda: self.on_combo_activated(3))
        self.comboBox_4.activated[int].connect(lambda: self.on_combo_activated(4))

        self.init_combobox(1, *self.list_i)
        self.init_combobox(2, *self.list_i)
        self.init_combobox(3, *self.list_i)
        self.init_combobox(4, *self.list_i)

        self.pushButton_1.released.connect(lambda: self.button_click())
        self.lineEdit_1.textChanged.connect(lambda: self.line_change(1))
        self.lineEdit_2.textChanged.connect(lambda: self.line_change(2))
        self.lineEdit_3.textChanged.connect(lambda: self.line_change(3))
        self.lineEdit_4.textChanged.connect(lambda: self.line_change(4))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.toolButton_1.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_1.setText(_translate("MainWindow", "导入"))
        self.menu.setTitle(_translate("MainWindow", "指标体系"))

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
                i = QStandardItem(str(item)) if item != None else QStandardItem('')
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

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())