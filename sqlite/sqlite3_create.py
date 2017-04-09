#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('test.sqlite')

print "opened database successfully"
conn.execute("drop table COMPANY")

conn.execute('''CREATE TABLE COMPANY
       (ID             INT     PRIMARY KEY,
        NAME           VARCHAR(50)    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        TEXT,
        SALARY         REAL);''')

print "Table created successfully"

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
conn.close()