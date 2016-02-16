#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: listParse.py
@time: 2016/2/9 10:10
"""


with open("contact.txt") as file:
    header = file.readline().strip().split('\t')
    contact = [
                    dict(
                        zip(header, line.strip().split('\t'))
                    ) for line in file
    ]

    print(contact)
    # [{'first': 'john', 'email': 'jsmith@example.com', 'last': 'smith'},
    #  {'first': 'jane', 'email': 'janed@example.com', 'last': 'doan'},
    #  {'first': 'david', 'email': 'dn@example.com', 'last': 'neilson'}]