#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('test.sqlite')

print "opened database successfully"

cur = conn.cursor() #current 当前光标

cur.execute("SELECT id,name,age FROM COMPANY;")

#fetch 拿 取
for item in cur.fetchall():
    print item

conn.commit() #可有可无
conn.close()