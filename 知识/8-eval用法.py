"""
======================
Author: 柠檬班-小简
Time: 2021/5/7 21:36
Project: day9
Company: 湖南零檬信息技术有限公司
======================
"""
import ast
import json


# strr = '{"expected":2500+2000}'
#
# res = eval(strr)
# print(res)

# ress = ast.literal_eval(strr)
# print(ress)

# # json串和python对象的转换。
# ress = json.loads(strr)
# print(ress)

# strr = """
# [{"expr":"$.code","expected":0,"type":"eq"},
# {"expr":"$.msg","expected":"OK","type":"eq"},
# {"expr":"$..leave_amount","expected":2000.55+2000,"type":"eq"}
# ]
# """
#
# res = eval(strr)
# print(res)

str1 = '[{"sql":"select leave_amount from member where id =123507754","expected":{"leave_amount":4068300.75+2000},"db_type":"eq"}]'

res = eval(str1)
print(res)
# print(type(res[0]["expected"]))
