'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/29 20:43
@Software: PyCharm
@File    : demo1.py
'''
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='1234',
                       database='pymysql_demo',port=3306)

cursor = conn.cursor()

cursor.execute('select 1')
result = cursor.fetchone()
print(result)

cursor.close()