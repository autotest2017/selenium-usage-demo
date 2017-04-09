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
cur = conn.cursor()  # 游标
print "opened database successfully"
cur.execute("drop table if exists COMPANY")

cur.execute('''CREATE TABLE COMPANY
        (ID            INT     PRIMARY KEY,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         FLOAT);''')

print "Table created successfully"

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

# 以元组的方式进行插入
sql_tpl = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(%s, %s, %s, %s, %s)"
data = (5, 'Sam', 18, 'Olloy', 3700.00)
cur.execute(sql_tpl, data)


# 以字典的方式进行插入
sql_dict = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES(%(ID)s, %(NAME)s, %(AGE)s, %(ADDRESS)s, %(SALARY)s)"
dict = {'ID': 6, 'NAME': 'Ren',
        'AGE': 19, 'ADDRESS': 'Hello',
        'SALARY': 4900.00}
cur.execute(sql_dict, dict)

cur.close()
conn.commit()
conn.close()