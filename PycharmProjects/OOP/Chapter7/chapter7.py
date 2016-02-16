#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: chapter7.py
@time: 2016/2/8 0:22
"""

normal_list = [1, 2, 3, 4, 5]


class CustomSeq(object):
    def __len__(self):
        return 10

    def __getitem__(self, index):
        return "x{}".format(index)


class FunkyBackwards(CustomSeq):
    def __reversed__(self):
        return "BACKWARDS!"


for seq in normal_list, CustomSeq(), FunkyBackwards():
    # print(seq)
    #     [1, 2, 3, 4, 5]
    #     <__main__.CustomSeq object at 0x01D14810>
    #     <__main__.FunkyBackwards object at 0x01D14850>
    print("\n{}: ".format(seq.__class__.__name__), end="")
    # list:
    # CustomSeq:
    # FunkyBackwards:
    for item in reversed(seq):
        print(item, end=" ")
    # list: 5 4 3 2 1
    # CustomSeq: x4 x3 x2 x1 x0
    # FunkyBackwards: B A C K W A R D S !
