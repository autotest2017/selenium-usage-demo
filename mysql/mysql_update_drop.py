#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
安装MySQL-Connector,MySQL官方的DB-API适配器，支持Python3
"""
import mysql.connector

conn = mysql.connector.connect(user='root',
                              password='123456',
                              host='127.0.0.1',
                              database='test')
cur = conn.cursor()
print "opened database successfully"

#cur.execute("UPDATE company set name='Paul Graham' where id=1;")
#cur.execute("drop table if exists COMPANY")
cur.execute("SELECT * FROM COMPANY;")

for item in cur.fetchall():
    print "这个人员的姓名是: ", item[1]

cur.close()
conn.commit()
conn.close()
