# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:47:41 2021

@author: ChengAi
"""

import os
import xlrd
from xlrd import xldate_as_datetime
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import requests
import bs4 as bs


def parse_excel():
    # 打开文件，并获取第一个工作簿的内容
    file_name = os.path.join(os.getcwd(), 'number.xlsx')
    work_book = xlrd.open_workbook(file_name)
    work_sheet = work_book.sheet_by_index(0)

    # 获取总行数
    total_rows = work_sheet.nrows

    # 定义一个列表，用于存放每一行的内容
    data_list = []
    key_list = None
    for i in range(total_rows):
        # 获取每一行的内容
        row_data = work_sheet.row_values(i)
        if i == 0:
            # 将第一行的作为字典的key
            key_list = row_data
        else:

            data_dict = dict()
            for index, cel_data in enumerate(row_data):
                # 获取字典的key
                key = key_list[index]

                # 注意点01 : 如果该单元格存放的是日期类型，读入的时候，需要借助 xldate_as_datetime 模块
                if index == 3:
                    if cel_data:
                        cel_data = xldate_as_datetime(cel_data, 0)
                else:
                    # 注意点02: 单元格是数字的，读取时会识别为浮点数，特此处理一下
                    if isinstance(cel_data, float):
                        cel_data = int(cel_data)

                # 字典赋值
                data_dict[key] = cel_data
            # 将字典加入需要返回的列表中
            data_list.append(data_dict)
    for data in data_list:
        print(data)
    return(data_list)

def get_stock_history(stock_name, stock_code, save_dir, start_date):#当然你可以在参数里加上起始日期，start_date, end_date,在DataReader()里替换'2012-01-01'和'2020-05-08'
    if stock_code[-2:] != 'ss':
        stock_code = str(stock_code) + '.ss'
    df = web.DataReader(stock_code, data_source='yahoo', start=start_date, end='2021-06-14')
    df.to_csv(save_dir + '/{}{}.csv'.format(stock_name, stock_code))

if __name__ == '__main__':
    data_list = parse_excel()
    for data in data_list:
        get_stock_history(data[1], data[2], 'D:/ChengAi/作业/Python作业/大作业', data[3])
    