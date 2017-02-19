#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Samren'
import xlrd


def read_excel():
    data = xlrd.open_workbook('user_data.xls')
    #查看文件中所有的sheet名称
    print data.sheet_names()

    #得到第一个工作表，或者 通过索引顺序 或 工作表名称
    table1 = data.sheets()[0]
    # table1 = data.sheet_by_index(0)
    # table1 = data.sheet_by_name("Account")
    print table1

    # 获取行数和列数
    nrows = table1.nrows
    ncols = table1.ncols
    print nrows, ncols

    #获取整行和整列的值（数组）
    print table1.row_values(0)
    print table1.col_values(0)

    # 遍历sheet
    for i in range(nrows):
        print "row %s: %s" % (i, table1.row_values(i))

    # 获取单元格
    cell_A1 = table1.cell(0,0).value
    cell_C3 = table1.cell(1,1).value
    print cell_A1, cell_C3

    # 分别使用行列索引
    cell_A1 = table1.row(0)[0].value
    cell_A2 = table1.col(1)[0].value
    print cell_A1, cell_A2

if __name__ == '__main__':
    read_excel()
