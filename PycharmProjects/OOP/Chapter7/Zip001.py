#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: Zip001.py
@time: 2016/2/8 21:48
"""
import sys


class Contact(object):
    def __init__(self, email="", last="", first="", **kwargs):
        self.email = email
        self.last = last
        self.first = first


filename = sys.argv[1]
# first	last	email
# john	smith	jsmith@example.com
# jane	doan	janed@example.com
# david	neilson	dn@example.com
contacts = []
with open(filename) as file:
    # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）
    # Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
    # str.split(str="", num=string.count(str)).
    header = file.readline().strip().split('\t')
    # ['first', 'last', 'email']
    for line in file:
        line = line.strip().split('\t')
        # ['john', 'smith', 'jsmith@example.com']
        # ['jane', 'doan', 'janed@example.com']
        # ['david', 'neilson', 'dn@example.com']
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))
        # [{'last': 'smith', 'email': 'jsmith@example.com', 'first': 'john'},
        # {'last': 'doan', 'email': 'janed@example.com', 'first': 'jane'},
        # {'last': 'neilson', 'email': 'dn@example.com', 'first': 'david'}]
    for contact in contacts:
        print("email: {email} -- {last}, {first}".format(**contact))
        # email: jsmith@example.com -- smith, john
        # email: janed@example.com -- doan, jane
        # email: dn@example.com -- neilson, david
