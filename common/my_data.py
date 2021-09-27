# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/9/3 16:36
    @Project: py37-学习 
---------------------------------------
"""


# 存储全局变量 - 接口返回值中提取的
from common.handle_phone import is_exist_phone
from common.my_requests import MyRequests
from common.mylogger import logger


class Data:
    user = "15500000000"
    passwd = "12345678"
    admin = "15500000073"
    admin_pwd = "12345678"

    global_user = {"user": user, "admin": admin}


if __name__ == "__main__":
    for key, value in Data.global_user.items():
        res = is_exist_phone(value)
        if not res:
            logger.info("全局使用帐号 {} 不存在。现在注册一个用户".format(value))
            mr = MyRequests()
            type = 1
            if key == "admin":
                type = 0
            method = "post"
            url = "/member/register"
            req_data = {"mobile_phone": value, "pwd": "12345678", "type": type}
            result = mr.send_request(method, url, req_data)
            logger.info("注册结果为：{}".format(result.text))

