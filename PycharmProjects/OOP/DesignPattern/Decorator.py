#!/usr/bin/env python
# encoding: utf-8


# class Beverage(object):
#     def __init__(self, description):
#         self.description = description
#
#     def getDescription(self):
#         return self.description
#
#     def cost(self):
#         pass
#
#
# class HouseBlend(Beverage):
#     def cost(self):
#         return 1.99
#
#
# hb = HouseBlend("house with blend")
# print("{0}: {1}".format(hb.getDescription(), hb.cost()))


# #把每种调料加到父类里面
# class Beverage(object):
#     condiment = 0.0
#     description = ""
#     def __init__(self, **condiments):
#         for k, v in condiments.items():
#             setattr(self, k , v)
#             if condiments[k] == "milk":
#                 Beverage.condiment += 0.99
#                 Beverage.description += " add milk"
#             if condiments[k] == "soy":
#                 Beverage.condiment += 0.89
#                 Beverage.description += " add soy"
#
#
#
# class HouseBlend(Beverage):
#     def __init__(self, **condiments):
#         super(HouseBlend, self).__init__(**condiments)
#         self.description = "House Blend Coffee "
#
#     def cost(self):
#         return Beverage.condiment + 1.99
#
#     def getDescrption(self):
#         return self.description + Beverage.description
#
#
#
# hb = HouseBlend(condi1="milk")
# print(hb.cost())
# print(hb.getDescrption())

class Beverage(object):
    def __init__(self):
        self.description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    def cost(self):
        pass

class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = "HouseBlend"
    def cost(self):
        return 1.99

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
        return self.beverage.cost() + .2


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(Mocha, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + .3


beverage = HouseBlend()
beverage = Milk(beverage)
beverage = Mocha(beverage)

print (beverage.getDescription())
print ("%.3f" % beverage.cost())