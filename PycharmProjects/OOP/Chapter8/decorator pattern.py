#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: decorator pattern.py
@time: 2016/2/13 12:15
"""

import time


def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(func.__name__, time.time() - now))
        return return_value

    return wrapper


def test1(a, b, c):
    print("\ttest1 called")


test1 = log_calls(test1)

test1(1, 2, 3)
