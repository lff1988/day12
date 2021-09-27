# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/5/31 11:17
    @Project: py37-学习 
---------------------------------------
"""
import os

# 管理项目下的路径
# 当前文件路径
config_path = os.path.abspath(__file__)
# 项目根目录
base_dir = os.path.dirname(os.path.dirname(config_path))
# 找到mysql.ini
mysql_path = os.path.join(base_dir, "conf", "mysql.ini")
# conf.ini
conf_path = os.path.join(base_dir, "conf", "conf.ini")
# 找到data.ini
data_path = os.path.join(base_dir, "conf", "data.ini")
# 找到测试数据
testdata_path = os.path.join(base_dir, "testdata", "lemon_testcase.xlsx")
# 日志路径
log_dir = os.path.join(base_dir, "outputs", "logs")
# 报告路径
report_dir = os.path.join(base_dir, "outputs", "reports")


