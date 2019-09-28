'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/1 10:57
@Software: PyCharm
@File    : demo1.py
'''
import pymongo

#获取连接mongodb的对象
client = pymongo.MongoClient("127.0.0.1",port=27017)

#获取数据库，数据库不存在则自动创建该数据库
db = client.lizhichao

#获取数据库中的集合（即mysql中的表），不存在则创建
collection = db.qa

#写入数据
collection.insert({"username":"lixiao","age":"18"})

collection.insert_many(#写入多条数据
    {
        "username":"lixiao",
        "age":"18"
    } ,
    {
        "username":"wangxiao",
        "age":"19"
    }
)

#查找数据
cursor = collection.find()#获取集合中所有数据，返回游标对象
for x in cursor:
    print(x)

result = collection.find_one()#获取一条数据，返回字典对象
# result = collection.find_one({'age':18})#获取一条数据，可指定条件，返回字典对象
print(result)

#更新数据
collection.update_one({"username":"lixiao"},{"$set":{
    "username":"wangle"}})#更新一条数据，指定条件与更新内容，前一个为条件，后一个为更新内容
collection.update_many({"username":"lixiao"},{"$set":{
    "username":"wangle"}})#更新多条数据

#删除数据
collection.delete_one({"username":"lixiao"})#删除一条数据
collection.delete_many({"username":"lixiao"})#删除多条数据