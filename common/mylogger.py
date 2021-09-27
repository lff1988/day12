# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/4/20 16:09
    @Project: py37-学习 
---------------------------------------
"""


import logging
from logging import Logger
from common.my_path import conf_path
from common.myConf import MyConf

"""
1、设置日志的收集级别
2、可以将日志输出到文件和控制台

3、以下这些方法：
   info()
   debug()
   error()
   warning()
   critical()

额外拓展：单例模式
"""


class MyLogger(Logger):

    def __init__(self):
        mc = MyConf(conf_path)
        file = mc.get("log", "file")
        super().__init__(mc.get("log", "name"), mc.get("log", "level"))
        # 3.定义日志格式
        format_str = "%(asctime)s %(name)s %(levelname)s %(filename)s [%(lineno)d] %(message)s"
        # 实例化一个日志格式类
        formatter = logging.Formatter(format_str)
        # 4.定义输出渠道
        handler = logging.StreamHandler()
        # 设置渠道中的显示格式
        handler.setFormatter(formatter)
        # 5.绑定日志收集器与渠道
        self.addHandler(handler)

        if file:
            file_list = [file, ".log"]
            result = "".join(file_list)
            handler2 = logging.FileHandler(result, encoding="utf-8")
            handler2.setFormatter(formatter)
            # 7.绑定日志收集器与文件类输出渠道
            self.addHandler(handler2)


logger = MyLogger()

# if __name__ == "__main__":
#     logger.info("这是一个基本问题")
#     logger.warning("这是一个警告")
#     logger.error("这是一个错误")

