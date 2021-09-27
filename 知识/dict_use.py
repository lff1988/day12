# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/9/14 17:29
    @Project: py37-学习 
---------------------------------------
"""
dict_1 = {"extract": "1234"}
# print(dict_1["pre_sql"])  # 报错  KeyError: 'pre_sql'
print(dict_1.get("pre_sql"))  # 不会报错 没有该key返回None
print(dict_1.get("extract"))
if dict_1.get("extract"):
    print("进来了")