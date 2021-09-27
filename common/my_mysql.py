# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/7/28 11:28
    @Project: py37-学习 
---------------------------------------
"""
import pymysql
import os

from common.myConf import MyConf
from common.my_path import mysql_path


class MyMysql:

    def __init__(self):
        # 实例化配置类对象
        conf = MyConf(mysql_path)
        # 1、连接mysql数据库 - 占用数据库资源
        self.db = pymysql.connect(
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            host=conf.get("mysql", "host"),
            database=conf.get("mysql", "database"),
            port=conf.getint("mysql", "port"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 2、创建游标
        self.cur = self.db.cursor()

    def get_count(self, sql):
        return self.cur.execute(sql)

    def get_one_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_many_data(self, sql, size=None):
        self.cur.execute(sql)
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()

    def close_conn(self):
        self.cur.close()
        self.db.close()

    def update_data(self):
        # 事务
        # 提交commit  回滚 rollback
        self.cur.execute()


if __name__ == '__main__':
    conn = MyMysql()
    num = conn.get_count("select * from member where mobile_phone = '18243051705'")
    print(num)
    conn.close_conn()

