'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/30 15:17
@Software: PyCharm
@File    : demo2.py
'''
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='1234',
                       database='pymysql_demo',port=3306)

cursor = conn.cursor()

#插入数据
#insert into user(id,username,age,password) values (2,'wangxiaoxiao',19,'123456')
# sql = """
#     insert into user(id,username,age,password) values (2,'wangxiaoxiao',19,'123456')
# """
# cursor.execute(sql)
# conn.commit()

sql = """
    insert into user(id,username,age,password) values (NULL,%s,%s,%s)
"""
username = 'spider'
age = 20
password = '123456'
cursor.execute(sql,(username,age,password))
conn.commit()

cursor.close()