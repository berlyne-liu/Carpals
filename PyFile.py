# -*- coding: utf-8 -*-

# 这是一个sqlite入库的程序
#
#
#

import pickle
from PySqlite import *
import xlrd


class FileModify:
    def file_type(self, f_path):
        """
        读取文件的文件类型，返回文件类型
        :param :h_path 输入的文件路径
        :return: 返回文件类型
        """
        f_p = f_path
        namelist = f_p.split('.')
        # print(namelist[-1])
        return namelist[-1]

    def read_header(self, f_path):
        """
        读取输入文件的表头（根据不同文件类型选择读取方式），返回包含表头元素的列表
        :param f_path:  输入的文件路径
        :return: 包含表头元素的列表
        """
        f = f_path
        f_type = self.file_type(f)
        if f_type in ['CSV', 'csv', '']:
            with open(f, 'r', errors='ignore') as file:
                text = file.readline()
                header_list = text.strip('\n').split(',')
            # print(header_list)
            return header_list
        elif f_type in ['xlsx']:
            x1 = xlrd.open_workbook(f)
            sheet1 = x1.sheet_by_index(1)
            header_list = sheet1.row_values(0)
            # print(header_list)
            return header_list
        else:
            error = False
            message = '错误文件类型'
            print(message)
            return error

    def match_header(self, m_file):
        """
        根据function:read_header返回的表头列表，与‘header’文件中保存的目标表头进行循环对比，
        判断是否属于目标表，匹配成功返回表名，匹配失败返回"match_fail"
        :param m_file:
        :return:
        bug:如果表头不匹配,无法抛出异常,需增加异常条件判断
        """
        h_list = self.read_header(m_file)
        print("2:", h_list)
        h_dict = self.to_load()
        print(h_dict)
        # print(h_dict)
        if h_list != '':
            for i in h_dict:
                print(1)
                if sorted(h_list) == sorted(list(h_dict[i])):
                    print(sorted(h_list))
                    print(sorted(list(h_dict[i])))
                    print("相同列表,表名为%s" % i)
                    # t_name = i
                    break
            return i
        else:
            error = False
            i = 'match_fail'
            print(i)
            return i

    # def read_sql(self, f_path):
    #     # 打开文件，把文件存在reader容器供调用
    #     with open(self.f_path, mode='r', encoding='utf-8') as file:
    #         reader = csv.reader(file)
    #         # print(reader)
    #     return reader

    def to_dump(self, data):
        """把数据序列化，保存到header文件中"""
        # pd = pickle.dumps(data)
        with open('header', 'wb') as f:
            pickle.dump(data, f)

    def to_load(self):
        # 用序列化把表头信息保存到二进制文件
        with open('header', 'rb') as f:
            d = pickle.load(f)
        return d

    def contrl_sqlconn(self):
        conn = sqlite3.connect('Carpals.db')
        modify = SqliteModify(conn)
        return conn, modify

    def contrl_tablename(self):
        conn, modify = self.contrl_sqlconn()
        t_list = modify.sqlite_table()
        return t_list

    def contrl_sqlinsert(self, **kwargs):
        conn, modify = self.contrl_sqlconn()
        dic = kwargs
        for p, t in dic.items():
            if p != '' and t != '':
                modify.sqlite_insert(p, t)

    def contrl_sqlcheck(self):
        conn, modify = self.contrl_sqlconn()
        result = modify.sqlite_check('指标体系-综合版业务.sql')
        desc = modify.cur.description
        h = [data[0] for data in desc]
        # print(h)
        return h, result


if __name__ == "__main__":
    # path1 = "F:/PycharmProjects/Carpals/09110917/益阳GSM2.CSV"
    # path2 = 'F:/PycharmProjects/Carpals/09110917/物理表20190522.xlsx'
    # path3 = 'F:/PycharmProjects/Carpals/header'
    # path4 = 'F:/PycharmProjects/Carpals/09110917/common-files-NB指标201909190946185d82ddeaccdbe.csv'
    fm = FileModify()
    # # mf = fm.read_header(path1)
    # # mf2 = fm.read_header(path2)
    # fb = fm.to_load()
    # print(fb)
    # mh = fm.match_header(path1)
    # print(mh)
    # tl = fm.to_load()
    # for k,v in tl.items():
    #     print(k,v)
    # fm.match_header(path4)
    fm.contrl_sqlcheck()
