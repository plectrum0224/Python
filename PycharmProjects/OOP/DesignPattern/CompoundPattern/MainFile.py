#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: MainFile.py
@time: 2016/3/3 17:28
"""


class Quackable:
    def quack(self):
        raise NotImplementedError


class MallardDuck(Quackable):
    def quack(self):
        print("Quack...")


class RedheadDuck(Quackable):
    def quack(self):
        print("Quack...")


class DuckCall(Quackable):
    def quack(self):
        print("Kwark...")


class RubberDuck(Quackable):
    def quack(self):
        print("Squack...")

class Goose:
    def honk(self):
        print("Honk...")

#===============适配器模式================#
class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose
    def quack(self):
        return self.goose.honk()
#===============适配器模式================#

#===============装饰器模式================#
class QuackCounter(Quackable):
    count = 0
    def __init__(self, duck):
        self.duck = duck
    def quack(self):
        self.duck.quack()
        QuackCounter.count += 1
    @classmethod
    def getQuack(self):
        return QuackCounter.count
#===============装饰器模式================#

class AbstractDuckFactory:






def simulator(duck):
    return duck.quack()







def main():
    mallarDuck = QuackCounter(MallardDuck())
    redheadDuck = QuackCounter(RedheadDuck())
    duckCall = QuackCounter(DuckCall())
    rubberDuck = QuackCounter(RubberDuck())
    gooseDuck = GooseAdapter(Goose())
    print("Duck Simulator\n")
    simulator(mallarDuck)
    simulator(redheadDuck)
    simulator(duckCall)
    simulator(rubberDuck)
    simulator(gooseDuck)
    print(QuackCounter.getQuack())

if __name__ == '__main__':
    main()

