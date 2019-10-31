# -*- coding: utf-8 -*-

import sqlite3
from Logic_Alarm_FileExtration import *


class Sqlite_Modify:
    def __init__(self, conn):
        # 创建连接connect, 创建游标cur
        self.connect = conn
        self.cur = self.connect.cursor()

    def sqlite_creat(self, *args, **kwargs):
        """
        *args:用于制作创建表的脚本的表头部分
        **kwargs:用于识别需要创建的表名，格式table=xx
        header是表头字符串，query按标准create table的格式拼接输出语句
        """
        table_head = ",".join("\"" + str(i) + "\"" for i in args[0])
        query_c = """create table if not exists """ + kwargs['table'] + """ (""" + table_head + """)"""
        # print(query_c)
        self.cur.execute(query_c)

    def sqlite_insert(self, i_head, *args, **kwargs):
        """
        *args:需导入的数据
        **kwargs:用于识别需要导入的表名，格式table=xx
        传入需导入的数据，传入类型为列表
        """
        # print(args)
        str_head = ",".join("\"" + str(i) + "\"" for i in i_head)
        for i, rows in enumerate(args[0]):
            try:
                str_sql = ",".join("\"" + str(i).replace("\"", "'") + "\"" for i in rows)
                query_i = """insert into """ + kwargs[
                    'table'] + """ (""" + str_head + """) values (""" + str_sql + """)"""
                # print(query_i)
                self.cur.execute(query_i)
            except Exception as e:
                print("第%s行出现异常：" % i + str(e) + "\n插入语句为：\n" + str(rows))
        self.connect.commit()

    def sqlite_output(self):
        pass

    def sqlite_query(self, path):
        """
        读取写好的sql脚本文件，脚本字符串赋值到query_sql,并返回该字符串
        """
        with open(path, 'r', encoding='utf8') as file:
            sql_text = file.readlines()
        query_sql = "".join(sql_text)
        # print(query_sql)
        self.cur.execute(query_sql)
        result = self.cur.fetchall()
        return result


if __name__ == "__main__":
    Path = "C:/Users/My-PC/Desktop/alarm/告警处理-工具/告警处理1022/FDD状态"
    Path2 = "C:/Users/My-PC/Desktop/alarm/告警处理-工具/告警处理1022/FDD告警.csv"
    Path3 = "E:/Program Files/JetBrains/PyDemo/Github_Clone/告警设置.xlsx"
    Path4 = "E:/Program Files/JetBrains/PyDemo/Github_Clone/Alarm_sql.sql"
    connect = sqlite3.connect('Carpals.db')
    modify = Sqlite_Modify(connect)
    Ae = Alarm_Extraction()
    sq = modify.sqlite_query(Path4)
    print(sq)
    # head, data, Error = Ae.textExtraction(Path)
    # head1, data1, Error1 = Ae.csvExtraction(Path2)
    # h2, d2, e3 = Ae.excelExtraction(Path3)
    # modify.sqlite_creat(h2, table="Alarm_Standard")
    # modify.sqlite_insert(h2, d2, table="Alarm_Standard")

    # modify.sqlite_creat(head1, table="Alarm_FDD_Cause")
    # modify.sqlite_insert(head1, data1, table="Alarm_FDD_Cause")
    #
    # modify.sqlite_creat(head, table="Alarm_FDD_State")
    # modify.sqlite_insert(head, data, table="Alarm_FDD_State")
