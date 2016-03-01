#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: StatusPattern.py
@time: 2016/3/1 20:34
"""


# class GumballMachine:
#     def __init__(self, count):
#         self.SOLD_OUT = 0
#         self.NO_QUARTER = 1
#         self.HAS_QUARTER = 2
#         self.SOLD = 3
#         self.state = self.SOLD_OUT
#         self.count = count
#         if self.count > 0:
#             self.state = self.NO_QUARTER
#
#     def insertQuarter(self):
#         if self.state == self.HAS_QUARTER:
#             print("You cannot insert another quarter")
#         elif self.state == self.NO_QUARTER:
#             self.state = self.HAS_QUARTER
#             print("You insert a quarter")
#         elif self.state == self.SOLD_OUT:
#             print("You can't insert a quarter, the machine is sold out")
#         elif self.state == self.SOLD:
#             print("Please wait, we're already giving you a gumball")
#
#     def ejectQuarter(self):
#         if self.state == self.HAS_QUARTER:
#             print("Quarter returned")
#             self.state = self.NO_QUARTER
#         elif self.state == self.NO_QUARTER:
#             print("You haven't inserted a quarter")
#         elif self.state == self.SOLD:
#             print("Sorry, you already turned the crank")
#         elif self.state == self.SOLD_OUT:
#             print("You can't eject, you haven't inserted a quarter yet")
#
#     def turnCrank(self):
#         if self.state == self.SOLD:
#             print("Turning twice doesn't get you another gumball!")
#         elif self.state == self.NO_QUARTER:
#             print("You turned, but there's no quarter")
#         elif self.state == self.SOLD_OUT:
#             print("You turned, but there's no gumball")
#         elif self.state == self.HAS_QUARTER:
#             print("You turned....")
#             self.state = self.SOLD
#             self.dispense()
#
#     def dispense(self):
#         if self.state == self.SOLD:
#             print("A gumball comes rolling out the slot")
#             self.count = self.count - 1
#             if self.count == 0:
#                 print("Oops, out of gumballs")
#                 self.state = self.SOLD_OUT
#             else:
#                 self.state = self.NO_QUARTER
#         elif self.state == self.NO_QUARTER:
#             print("You need to pay first")
#         elif self.state == self.SOLD_OUT:
#             print("No gumball dispense")
#         elif self.state == self.HAS_QUARTER:
#             print("No gumball dispense")
#     def getCount(self):
#         print(self.count)

class SoldOutState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")
    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")
    def turnCrank(self):
        print("You turned, but there's no gumball")
    def dispense(self):
        print("No gumball dispense")


class NoQuarterState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
    def ejectQuarter(self):
        print("You haven't inserted a quarter")
    def turnCrank(self):
        print("You turned, but there's no quarter")
    def dispense(self):
        print("You need to pay first")


class HasQuarterState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("You cannot insert another quarter")
    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    def turnCrank(self):
        print("You turned....")
        self.gumballMachine.setState(self.gumballMachine.getSoldState())
    def dispense(self):
        print("No gumball dispense")


class SoldState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount()>0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class GumballMachine:
    def __init__(self, numberGumballs):
        self.count = numberGumballs
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        if self.count > 0:
            self.state = self.noQuarterState
    def setState(self, state):
        self.state = state
    def getSoldOutState(self):
        return self.soldOutState
    def getNoQuarterState(self):
        return self.noQuarterState
    def getHasQuarterState(self):
        return self.hasQuarterState
    def getSoldState(self):
        return self.soldState
    def getCount(self):
        return self.count
    def insertQuarter(self):
        self.state.insertQuarter()
    def ejectQuarter(self):
        self.state.ejectQuarter()
    def turnCrank(self):
        if self.state == self.hasQuarterState:
            self.state.turnCrank()
            self.state.dispense()
        else:
            self.state.turnCrank()
    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1
    def getState(self):
        print(self.state)













def main():
    gumballMachine = GumballMachine(2)
    print(gumballMachine.getCount())
    gumballMachine.getState()
    print("=====================================================")
    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    print(gumballMachine.getCount())
    print("=====================================================")
    gumballMachine.turnCrank()






if __name__ == '__main__':
    main()



