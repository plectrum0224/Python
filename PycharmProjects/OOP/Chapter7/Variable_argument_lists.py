#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: Variable_argument_lists.py
@time: 2016/2/9 19:16
"""

# class Option(object):
#     default_option = {
#         'port': 21,
#         'host': 'localhost',
#         'username': None,
#         'password': None,
#         'debug': False,
#     }
#
#     def __init__(self, **kwargs):
#         self.option = dict(Option.default_option)
#         self.option.update(kwargs)
#
#     def __getitem__(self, key):
#         return self.option[key]
#
# option = Option(username="dusty", password="drowssap", debug=True)
# print(option['debug'])
# print(option['port'])
# print(option['username'])

# import shutil
# import os.path
#
#
# def argumented_move(target_folder, *filenames, verbose=False, **specific):
#     """
#     Move all filenames into the target_folder, allowing
#     specific treatment of certain files.
#     :param verbose:
#     :param target_folder:
#     """
#
#     def print_verbose(message, filename):
#         """
#         print the message only if verbose is enabled
#         :param filename:
#         :param message:
#         """
#         if verbose:
#             print(message.format(filename))
#
#     for filename in filenames:
#         target_path = os.path.join(target_folder, filename)
#         # print(target_path)
#         if filename in specific:
#             if specific[filename] == 'ignore':
#                 print_verbose("Ignoring {0}", filename)
#             elif specific[filename] == 'copy':
#                 print_verbose("Copying {0}", filename)
#                 # shutil.copyfile(filename, target_path)
#         else:
#             print_verbose("Moving {0}", filename)
#             # shutil.move(filename, target_path)
#
# # argumented_move("D:\move_here", "log_file", verbose=True)
# argumented_move("D:\move_here", "one", "two", "four", "five",  four="copy", five="ignore", verbose=True)


# def show_args(arg1, arg2, arg3="THREE"):
#     print(arg1, arg2, arg3)
#
# some_args = range(3)
# print(some_args)
# more_args = {
#     "arg1": "ONE",
#     "arg2": "TWO"
# }
#
# print("Unpacking a sequence: ", end="")
# show_args(0, 1, 2)
# print("Unpacking a dict: ", end="")
# show_args(**more_args)
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
# contacts = []
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
        contact_map = dict(zip(header, line))
        # {'last': 'smith', 'email': 'jsmith@example.com', 'first': 'john'},
        # {'last': 'doan', 'email': 'janed@example.com', 'first': 'jane'},
        # {'last': 'neilson', 'email': 'dn@example.com', 'first': 'david'}
        contacts = Contact(**contact_map)
        print("email: {0} -- {1}, {2}".format(contacts.email, contacts.last, contacts.first))
        # email: jsmith@example.com -- smith, john
        # email: janed@example.com -- doan, jane
        # email: dn@example.com -- neilson, david
