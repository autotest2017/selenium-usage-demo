#!/usr/bin/env python
# encoding:utf-8
"""
文件读写是最基本的功能
"""
__author__ = 'Samren'

def read_file():
    hfile = open('data.txt', 'r')
    for i in hfile.readlines():
        print i.strip().decode('gbk')
    hfile.close()

def write_file():
    name_list = [u'李聃', u'李晓', u'陈昌成']
    hfile = open('data_write.txt', 'w')
    for i in name_list:
        hfile.write(i.encode('utf-8')+'\n')
    hfile.close()
    import os


if __name__ == '__main__':
    #read_file()
    write_file()