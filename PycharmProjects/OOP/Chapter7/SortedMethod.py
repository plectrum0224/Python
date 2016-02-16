#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: SortedMethod.py
@time: 2016/2/9 9:34
"""


def min_max_indexes(seq):
    minimum = min(enumerate(seq), key=lambda s: s[1])
    maximum = max(enumerate(seq), key=lambda s: s[1])
    return minimum[0], maximum[0]


alist = [5, 0, 1, 4, 6, 3]
print(min_max_indexes(alist))  # return the index value
print(alist[1], alist[4])
