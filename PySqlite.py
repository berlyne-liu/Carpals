# -*- coding: utf-8 -*-
# 这是一个sqlite入库的程序
#
#
#

import sqlite3
import pandas


class SqliteModify:
    def __init__(self, conn):
        self.connect = conn
        # 连接sqlite3
        self.cur = self.connect.cursor()
        # 创建游标

    def sqlite_creat(self, *args, **kwargs):
        """传入元组*args:用于制作创建表的脚本的表头部分
        传入字典**kwargs:用于识别需要创建的表名，格式table=xx"""
        header = ",".join("\"" + str(i) + "\"" for i in args)
        query_c = """create table if not exists """ + kwargs['table'] + """ (""" + header + """)"""
        print(query_c)
        self.cur.execute(query_c)
        # header是表头字符串，query按标准create table的格式拼接输出语句

    def sqlite_insert(self, csvpath, tablename):
        """传入源文件路径csvpath,导入的数据库表名table,源文件的文件类型"""
        cf = pandas.read_csv(csvpath, encoding='gbk')
        cf.to_sql(tablename, self.connect, if_exists='replace', index=False)
        # print(cf.head(10))
        # 5张表导入，if判断.csv或.xlsx
        # 表名：LTE_Traffic/MR/NB_Traffic/TA_RSRP/GSM_Traffic

    def sqlite_output(self, query_o):
        """把查询的数据导出到csv"""
        reader = pandas.read_sql(query_o, self.connect)
        reader.to_csv("output.csv", encoding="gbk", index=False)
        pass

    def sqlite_check(self, path):
        """读取写好的sql脚本文件，脚本字符串赋值到query_sql,并返回该字符串"""
        with open(path, 'r', encoding='utf8') as file:
            sql_text = file.readlines()
        query_sql = "".join(sql_text)
        # print(query_sql)
        self.cur.execute(query_sql)
        result = self.cur.fetchall()
        return result

    def sqlite_table(self):
        """
        查询当前数据库的table_name,返回列表，combobox可调用此方法添加item
        :return: 返回当前数据库的table_name列表
        """
        query_c = "select name from sqlite_master where type='table' order by name;"
        self.cur.execute(query_c)
        r_list = [value for (value,) in self.cur.fetchall()]
        # print(r_list)
        return r_list


# if __name__ == "__main__":
#     conn = sqlite3.connect('Carpals.db')
#     modify = SqliteModify(conn)
#     modify.sqlite_table()
