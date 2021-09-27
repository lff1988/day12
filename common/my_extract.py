# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/9/9 14:48
    @Project: py37-学习 
---------------------------------------
"""
import jsonpath
from common.my_data import Data
from common.mylogger import logger

"""
从响应结果当中，提取值，并设置为全局变量(Data类作为本框架的全局变量类)
1、提取表达式：放在excel当中
   (可能提取1个，可能提取多个。。以表达式个数为准)

2、提取出来之后，设置为Data类属性
"""


def extract_data_from_response(reponse_dict, extract_str, share_data):
    """
        从响应结果当中提取值，并设置为Data类的属性。
        :param extract_epr: excel当中extract列中的提取表达式。是一个字典形式的字符串。
                            key为全局变量名。value为jsonpath提取表达式。
                            '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
        :param response: http请求之后的响应结果。字典类型。
        :return:None
    """
    # 1、从excel中读取的提取表达式，转成字典对象
    extract_dict = eval(extract_str)
    # 2、遍历1中字典的key,value.key是全局变量名，value是jsonpath表达式。
    for key, value in extract_dict.items():
        # 根据jsonpath从响应结果当中，提取真正的值。value就是jsonpath表达式
        logger.info("提取的变量名是：{}，提取的jsonpath表达式是：{}".format(key, value))
        result = jsonpath.jsonpath(reponse_dict, value)
        # jsonpath找了就是列表，找不到返回False
        # 如果提取到了真正的值，那么将它设置为Data类的属性。key是全局变量名，result[0]就是提取后的值
        if result:
            setattr(share_data, key, str(result[0]))
            logger.info("提取的变量名是：{}，提取到的值是：{},并设置为Data类实例对象的属性和值。".format(key, str(result[0])))

