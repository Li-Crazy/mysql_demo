'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/30 16:55
@Software: PyCharm
@File    : demo3.py
'''
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='1234',
                       database='pymysql_demo',port=3306)

cursor = conn.cursor()

#select username,age from user where id = 1
#select * from user
# sql = """
#     select username,age from user where id = 1
# """

sql = """
    select * from user
"""

cursor.execute(sql)
###########fetchone()###################
# result = cursor.fetchone()#返回一条数据，第一次调用返回第一条数据
# print(result)
# result = cursor.fetchone()#返回一条数据，第二次调用返回第二条数据
# print(result)
# while True:#利用result = cursor.fetchone()循环打印所有数据
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break

###########fetchall()###################
# results = cursor.fetchall()#获取所有数据
# for result in results:
#     print(result)

###########fetchall()###################
results = cursor.fetchmany(3)#指定参数，获取指定条数据
for result in results:
    print(result)

cursor.close()