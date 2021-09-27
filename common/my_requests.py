# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/7/23 9:17
    @Project: py37-学习 
---------------------------------------
"""
import requests
from common.mylogger import logger
from common.my_path import conf_path
from common.myConf import MyConf


class MyRequests:

    def __init__(self):
        # 请求头
        self.headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        # 读取配置文件中的server地址
        self.base_url = MyConf(conf_path).get("server", "host")

    # 方法 post/put.. json=XXX, get.. params=XXX
    def send_request(self, method, api_url, data, token=None):
        # 处理请求头
        self.__deal_headers(token)
        # 处理url
        url = self.__deal_url(api_url)

        logger.info("请求地址：\n{}".format(url))
        logger.info("请求方法：\n{}".format(method))
        logger.info("请求数据：\n{}".format(data))

        # 调用requests的方法去发起一个请求。并得到响应结果
        if method.upper() == "GET":
            resp = requests.request(method, url, params=data, headers=self.headers)
        else:
            resp = requests.request(method, url, json=data, headers=self.headers)
        logger.info("响应结果：\n{}".format(resp.text))
        return resp

    def __deal_headers(self, token=None):
        if token:
            self.headers["Authorization"] = "Bearer {}".format(token)
        logger.info("请求为：\n{}".format(self.headers))

    def __deal_url(self, api_url):
        url = self.base_url + api_url
        return url


if __name__ == "__main__":
    mr = MyRequests()
    # ==============注册接口======================================
    url = "http://api.lemonban.com/futureloan/member/register"
    req_data = {
        "mobile_phone": "15000000002",
        "pwd": "12345678",
        "type": "0"
    }
    resp = mr.send_request("post", url, json=req_data)
    print(resp.text)

    # ===============登录接口=====================================
    url = "http://api.lemonban.com/futureloan/member/login"
    req_data = {
        "mobile_phone": "15000000002",
        "pwd": "12345678"
    }
    resp = mr.send_request("post", url, json=req_data)
    json_result = resp.json()
    id = json_result["data"]["id"]
    token = json_result["data"]["token_info"]["token"]
    print(resp.text)
    # ===================充值接口=============================
    url = "http://api.lemonban.com/futureloan/member/recharge"
    req_data = {
        "member_id": id,
        "amount": 1000
    }
    resp = mr.send_request("post", url, token, json=req_data)
    print(resp.text)
