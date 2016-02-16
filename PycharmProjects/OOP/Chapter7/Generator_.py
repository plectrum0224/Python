#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: Generator_.py
@time: 2016/2/9 11:13
"""

import sys

inname = sys.argv[1]
outname = sys.argv[2]


# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         # warnings = (l for l in infile if "WARNING" in l)
#         warnings = (l.replace('\tWARNING', '') for l in infile if 'WARNING' in l)
#
#         # <generator object <genexpr> at 0x01776B70>
#         for l in warnings:
#             outfile.write(l)

# using object oriented method
# class WarningFilter(object):
#     def __init__(self, insequence):
#         self.insequence = insequence
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         l = self.insequence.readline()
#         while l and 'WARNING' not in l:
#             l = self.insequence.readline()  # 读取下一行
#         if not l:
#             raise StopIteration
#         return l.replace('\tWARNING', '')
#
#
# with open(inname) as infile:
#     with open(outname, 'w') as outfile:
#         filter = WarningFilter(infile)
#         for l in filter:
#             outfile.write(l)

# using yield method
def warning_filter(seq):
    for l in seq:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')


with open(inname) as infile:
    with open(outname, 'w') as outfile:
        filter = warning_filter(infile)
        for l in filter:
            outfile.write(l)
