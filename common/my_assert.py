# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/7/27 11:25
    @Project: py37-学习 
---------------------------------------
"""
import ast
from decimal import Decimal

import jsonpath
from common.mylogger import logger
from common.my_mysql import MyMysql


class MyAssert:

    def assert_response_value(self, check_str, response_dict):
        """
        1、把字符串转换成列表
        2、使用列表中expr中的jsonpath表达式提取response_dict中的数据
        3、实际结果与预期值对比
        :param check_str: 从测试用例excel中读取出的assert_list列的字符串。是一个列表形式的字符串。里面的成员是一个断言。
        :param response_dict: 实际的响应结果，是字典类型。
        :return:None
        """
        # 所有断言的比对结果列表
        check_res = []
        # 把字符串转换成列表
        # check_list = ast.literal_eval(check_str)
        check_list = eval(check_str)

        for check in check_list:
            logger.info("要断言的内容为：\n{}".format(check))
            # 通过jsonpath表达式，从响应结果当中拿到了实际结果
            actual = jsonpath.jsonpath(response_dict, check["expr"])
            if isinstance(actual, list):
                actual = actual[0]
                logger.info("从响应结果当中提取到的值为:\n{}".format(actual))
                logger.info("期望结果为:\n{}".format(check["expected"]))
            # 与实际结果做比对
            if check["type"] == "==":
                logger.info("比对2个值是否相等。")
                logger.info("比对结果为：\n{}".format(actual == check["expected"]))
                check_res.append(actual == check["expected"])
            elif check["type"] == "gt":
                logger.info("比对2个值的大小。")
                logger.info("比对结果为：\n{}".format(actual > check["expected"]))

        if False in check_res:
            logger.error("部分断言失败！，请查看比对结果为False的")
            # raise AssertionError
            return False
        else:
            logger.info("所有断言成功！")
            return True

    def assert_db(self, check_db_str):
        """
        1、把字符串转换成列表
        2、遍历1中的列表
            2.1 执行sql语句（根据type的类型决定使用哪个方法），得到实际结果
            2.2 与期望结果比对
        :param check_db_str: 从测试用例excel中读取出的assert_db列的字符串
        :return:
        """
        # 所有断言的比对结果列表
        check_db_res = []
        # 把字符串转换成列表
        # check_db_list = ast.literal_eval(check_db_str)  # 比eval安全一点。转成列表。
        check_db_list = eval(check_db_str)
        # 实例化操作数据库类
        db = MyMysql()

        # 遍历check_db_list
        for check_db_dict in check_db_list:
            logger.info("当前要比对的sql语句：\n{}".format(check_db_dict["sql"]))
            logger.info("当前执行sql的查询类型(查询结果条数/查询某个值.)：\n{}".format(check_db_dict["db_type"]))
            logger.info("期望结果为：{}".format(check_db_dict["expected"]))
            # 根据type来调用不同的方法来执行sql语句。
            if check_db_dict["db_type"] == "count":
                logger.info("比对数据库查询的结果条数，是否符合期望")
                # 执行sql语句
                res = db.get_count(check_db_dict["sql"])
                logger.info("sql的执行结果为：{}".format(res))
            elif check_db_dict["db_type"] == "eq":
                logger.info("比对数据库查询的结果，是否相等")
                # 执行sql语句.查询结果是一个字典key-value
                res = db.get_one_data(check_db_dict["sql"])
                logger.info("sql的执行结果为：{}".format(res))
                # 对于数据库查询结果当中，如果有Decimal类型，则转换为float类型
                for key, value in res.items():
                    if isinstance(value, Decimal):
                        res[key] = float(value)
            else:
                logger.error("不支持的数据库比对类型！！，请检查你的断言写法！！")
                raise Exception

            # 将比对结果添加到结果列表当中
            check_db_res.append(res == check_db_dict["expected"])
            logger.info("比对结果为：{}".format(res == check_db_dict["expected"]))

        if False in check_db_res:
            logger.error("部分断言失败！，请查看比对结果为False的")
            # raise AssertionError
            return False
        else:
            logger.info("所有断言成功！")
            return True


if __name__ == "__main__":
    check_db_str = """[{"sql":"select id from member where mobile_phone = '15500000000'",
                    "expected":1,"type":"count"}]"""
    MyAssert().assert_db(check_db_str)
