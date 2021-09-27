# -*- coding:utf-8 -*-

"""
--------------------------------------
    @Author :慕凡
    @Date :2021/9/14 14:28
    @Project: py37-学习 
---------------------------------------
"""
import json

import pytest

from common.my_assert import MyAssert
from common.my_excel import MyExcel
from common.my_extract import extract_data_from_response
from common.my_path import testdata_path
from common.my_replace import replace_case_with_re
from common.my_requests import MyRequests
"""
增加项目测试
    前置：登录成功
"""

me = MyExcel(testdata_path, "增加项目")
cases = me.read_data()
mr = MyRequests()
massert = MyAssert()


@pytest.mark.usefixtures("class_init")
class TestAddloan:

    @pytest.mark.parametrize("case", cases)
    def test_add_loan(self, case, class_init):
        # 获取Data类的实例对象，存放类级别的变量
        share_data = class_init
        # 下一接口的测试用例中，需要替换，替换为上一个接口中提取的数据。
        case = replace_case_with_re(case, share_data)
        # 把替换之后的请求数据(json格式的字符串)，转换成一个字典
        req_dict = json.loads(case["req_data"])
        # 发起请求，并接收响应结果
        if hasattr(share_data, "token"):
            resp = mr.send_request(case["method"], case["url"], req_dict, token=getattr(share_data, "token"))
        else:
            resp = mr.send_request(case["method"], case["url"], req_dict)

        # 结果空列表
        assert_res = []

        # 断言响应结果中的数据
        if case["assert_list"]:
            response_check_res = massert.assert_response_value(case["assert_list"], resp.json())
            assert_res.append(response_check_res)

        if False in assert_res:
            pass
        else:
            # 提取响应结果中的值设置为全局变量
            if case.get("extract"):
                # 调用提取函数
                extract_data_from_response(resp.json(), case["extract"], share_data)

        # 5、断言数据库 - sql语句、结果与实际、比对的类型
        if case["assert_db"]:
            db_check_res = massert.assert_db(case["assert_db"])
            assert_res.append(db_check_res)

        # 最终的抛AsserttionError
        if False in assert_res:
            raise AssertionError
