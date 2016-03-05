#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: pyCharmCommunityEdition
@file: operator_reload.py
@time: 2016/2/14 20:22
"""


# __getitem__
# 当实例X出现在X[i]这样的索引运算中时，Python会自动调用这个实例继承的__getitem__，
# 把X作为第一个参数传递，并且方括号内的索引值传递给第二个参数

class indexer(object):
    def __getitem__(self, item):
        return item ** 2


X = Indexer()
print(X[5])
# return 25

for i in range(5):
    print(X[i], end=" ")
# return 0 1 4 9 16


