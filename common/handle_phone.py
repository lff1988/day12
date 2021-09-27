# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/7/28 16:23
    @Project: py37-学习 
---------------------------------------
"""
from faker import Faker
from common.my_mysql import MyMysql


def get_new_phone():
    """
    1.faker生成手机号
    2.判断该手机号是否存在数据库中
    3.如果不存在直接返回该手机号；如果存在，重新生成一个手机号，直至该手机号不存在于数据库中；
    :return: phone
    """
    while True:
        f = Faker("zh_CN")
        phone = f.phone_number()
        mm = MyMysql()
        sql = "select id from member where mobile_phone = '{}'".format(phone)
        num = mm.get_count(sql)
        if num == 0:
            return phone


def is_exist_phone(phone):
    """
    判断该手机号是否已经注册
    :param phone:
    :return:
    """
    mm = MyMysql()
    sql = "select id from member where mobile_phone = '{}'".format(phone)
    num = mm.get_count(sql)
    if num == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    print(get_new_phone())
