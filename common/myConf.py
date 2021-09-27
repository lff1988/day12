# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/4/20 16:55
    @Project: py37-学习 
---------------------------------------
"""
from configparser import ConfigParser


class MyConf(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf-8")

