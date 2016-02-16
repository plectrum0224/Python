#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: closure.py
@time: 2016/2/13 10:33
"""


#
# def calc_sum(lst):
#     def lazy_sum():
#         return sum(lst)
#
#     return lazy_sum
#
# f = calc_sum([1, 2, 3, 4, 5, 6])
#
# print(f)


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        r = f(i)
        fs.append(r)
    return f

f1 = count()
f2 = count()
f3 = count()

print(f1)
print(f2)
print(f3)
