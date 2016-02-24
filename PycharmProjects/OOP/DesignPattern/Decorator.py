#!/usr/bin/env python
# encoding: utf-8


# class Beverage(object):
#     def __init__(self):
#         self.description = "Unknown description"
#
#     def getDescription(self):
#         return self.description
#
#     def cost(self):
#         pass
#
#
# class HouseBlend(Beverage):
#     def __init__(self):
#         super(HouseBlend, self).__init__()
#         self.description = "HouseBlend coffee"
#     def cost(self):
#         return 1.99
#
#
# class DarkRoast(Beverage):
#     def __init__(self):
#         super(DarkRoast, self).__init__()
#         self.description = "DarkRoast coffee"
#     def cost(self):
#         return 1.79
#
#
# class Decaf(Beverage):
#     def __init__(self):
#         super(Decaf, self).__init__()
#         self.description = "Decaf coffee"
#     def cost(self):
#         return 2.99
#
#
# class Espresso(Beverage):
#     def __init__(self):
#         super(Espresso, self).__init__()
#         self.description = "Espresso coffee"
#     def cost(self):
#         return 1.39
#
# for item in [HouseBlend(), DarkRoast(), Decaf(), Espresso()]:
#     print("{0}: {1}".format(item.getDescription(), item.cost()))


# class Beverage(object):
#     #定义两个类属性，作为初始值
#     condiment = 0.0
#     description = ""
#     #定义一个dict，用来存放调料
#     def __init__(self, **condiments):
#         for k, v in condiments.items():
#             setattr(self, k , v)
#             #下面是判断哪些调料使用了，之后加上这种调料的价格和描述
#             if condiments[k] == "milk":
#                 Beverage.condiment += 0.99
#                 Beverage.description += " add milk"
#             if condiments[k] == "soy":
#                 Beverage.condiment += 0.89
#                 Beverage.description += " add soy"
#             #下面可以不停的增加调料种类
#     def getDescription(self):
#         return self.description + Beverage.description
#
# class HouseBlend(Beverage):
#     def __init__(self, **condiments):
#         super(HouseBlend, self).__init__(**condiments)
#         self.description = "HouseBlend Coffee "
#     #cost现在就为调料与本身的价格之和
#     def cost(self):
#         return Beverage.condiment + 1.99
# #这个实例里增加了milk调料，打印最终的价格和描述
# hb = HouseBlend(condi1="milk", condi2="soy", condi3="soy")
# print("{0}: {1}".format(hb.getDescription(), hb.cost()))


class Beverage(object):
    def __init__(self):
        self.description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    def cost(self):
        pass

    def getSize(self):
        return self.size

    def setSize(self, cupSize):
        self.size = cupSize

class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = "HouseBlend"
    def cost(self):
        if self.getSize() == "TALL":
            return 1.99
        elif self.getSize() == "GRANDE":
            return 2.99
        elif self.getSize() == "VENTI":
            return 3.99

class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self).__init__()
        self.description = "Espresso"
    def cost(self):
        return 1.39

    def getDescription(self):
        return self.description

class CondimentDecorator(Beverage):
    def getDescription(self):
        pass

class Milk(CondimentDecorator):
    def __init__(self, beverage):
        super(Milk, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"

    def cost(self):
        if self.beverage.getSize() == "TALL":
            return self.beverage.cost() + .2
        elif self.beverage.getSize() == "GRANDE":
            return self.beverage.cost() + .25
        elif self.beverage.getSize() == "VENTI":
            return self.beverage.cost() + .30


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(Mocha, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        if self.beverage.getSize() == "TALL":
            return self.beverage.cost() + .3
        elif self.beverage.getSize() == "GRANDE":
            return self.beverage.cost() + .35
        elif self.beverage.getSize() == "VENTI":
            return self.beverage.cost() + .40


beverage = HouseBlend()
beverage.setSize("GRANDE")
beverage = Milk(beverage)


print("{0}: {1}".format(beverage.getDescription(), "%.3f" % beverage.cost()))