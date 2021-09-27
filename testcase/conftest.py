# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/9/14 8:59
    @Project: py37-学习 
---------------------------------------
"""
import pytest

from common.my_data import Data
from common.handle_phone import is_exist_phone
from common.my_requests import MyRequests
from common.mylogger import logger


@pytest.fixture(scope="session", autouse=True)
def global_init():
    # 配置的全局用户信息 - 要确保一定是存在的
    # 1、从Data里拿出来用户数据
    # 2、调用sql从数据库查询。如果不存在则注册
    for key, value in Data.global_user.items():
        res = is_exist_phone(value)
        if not res:
            logger.info("全局使用帐号 {} 不存在。现在注册一个用户".format(value))
            mr = MyRequests()
            type = 1
            if key == "admin":
                type = 0
            method = "post"
            url = "http://api.lemonban.com/futureloan//member/register"
            req_data = {"mobile_phone": value, "pwd": "12345678", "type": type}
            result = mr.send_request(method, url, req_data)
            logger.info("注册结果为：{}".format(result.text))


@pytest.fixture(scope="class")
def class_init():
    # 实例化Data类对象，作为每一个测试类的类级别的变量。
    class_share_data = Data()
    yield class_share_data
