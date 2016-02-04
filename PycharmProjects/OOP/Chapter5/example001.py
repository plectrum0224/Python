#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: example001.py
@time: 2016/2/4 21:50
"""
import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Polygon(object):
    def __init__(self, points=None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def perimeter(self):
        perimeter = 0

        # 第一个点需要重复使用两次，所以列表里需要增加一个多边形的第一个顶点
        # 列表里存放的是Point对象实例
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            # 调用Point对象的distance方法，计算相邻两个点之间的距离
            perimeter += points[i].distance(points[i + 1])
        return perimeter


if __name__ == '__main__':
    square = Polygon([(1,1),(1,2),(4,2),(3,1)])
    print (square.perimeter())
