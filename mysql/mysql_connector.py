#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
安装MySQL-Connector,MySQL官方的DB-API适配器，支持Python3
"""
import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='123456',
                              host='127.0.0.1',
                              database='test')
if cnx is not None:
    print "connect ok"
    cnx.close()
else:
    print "connect fail"