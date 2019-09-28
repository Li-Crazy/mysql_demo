'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/30 17:33
@Software: PyCharm
@File    : demo4.py
'''
import pymysql


conn = pymysql.connect(host='localhost',user='root',password='1234',
                       database='pymysql_demo',port=3306)

cursor = conn.cursor()
#删除数据
#delete from user where id = 4
# sql = """
#     delete from user where id = 4
# """
#更新数据
#update user set username = 'limaomao' where id = 3
sql = """
    update user set username = 'limaomao' where id = 3
"""
cursor.execute(sql)
conn.commit()
cursor.close()