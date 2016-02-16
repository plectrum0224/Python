#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: Enumberate001.py
@time: 2016/2/8 12:01
"""


import sys
filename = sys.argv[0]

with open(filename) as file:
    for index, line in enumerate(file):
        if index < 9:
            print("{0}: {1}".format('0'+str(index+1), line), end='')
        else:
            print("{0}: {1}".format(index+1, line), end='')

