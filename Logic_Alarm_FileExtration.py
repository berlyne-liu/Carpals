# -*- coding: utf-8 -*-

import csv


class Alarm_Extraction:
    def __init__(self):
        pass

    def textExtraction(self, filepath):
        with open(filepath, 'r') as file:
            file_list = file.readlines()
            container = []
            error = "扫描文件发现以下不符合规则的数据行（可忽略）：\n"
            header = file_list[3].strip('\n').split('\t')
            column_h = len(header)
            for row in range(len(file_list)):
                package = file_list[row].strip('\n').split('\t')
                if len(package) == column_h:
                    container.append(package)
                else:
                    error = error + ("第%s行的字段数为%s,不符合规则！\n" % (row, len(package)))
        return container, error

    def csvExtraction(self, csvpath):
        with open(csvpath, 'r', newline='') as file:
            cr = csv.reader(file, delimiter="|")
            container = []
            for i, rows in enumerate(cr):
                container.append(rows)
        return container


if __name__ == "__main__":
    Path = "C:/Users/My-PC/Desktop/alarm/告警处理-工具/告警处理1022/FDD状态"
    Path2 = "C:/Users/My-PC/Desktop/alarm/告警处理-工具/告警处理1022/FDD告警.csv"
    Ae = Alarm_Extraction()
    li, Error = Ae.textExtraction(Path)
    print(li, Error)
    ce = Ae.csvExtraction(Path2)
    print(ce)
