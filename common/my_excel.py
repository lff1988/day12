# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/7/26 16:39
    @Project: py37-学习 
---------------------------------------
"""
from openpyxl import load_workbook


class MyExcel:

    def __init__(self, excel_path, sheet_name):
        # 1、加载一个excel，得到工作薄 Workbook
        wb = load_workbook(excel_path)
        # 2、选择一个表单- 通过表单名 Sheet
        self.sh = wb[sheet_name]

    def read_data(self):
        # 注意：接口的请求数据，读取出来是字符串。
        # 存储表单下读取到的所有数据 - 每一个成员都是一个字典
        all_data = []
        data = list(self.sh.values)
        keys = data[0]  # 获取所有的列名
        for row in data[1:]:
            row_dict = dict(zip(keys, row))
            all_data.append(row_dict)
        return all_data


if __name__ == "__main__":
    me = MyExcel(r"E:\Pycharm_workspace\py37-学习\api_auto_test\day5\testdata\lemon_testcase.xlsx", "注册接口")
    result = me.read_data()
    for item in result:
        print(item)
