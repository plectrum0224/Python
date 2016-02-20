#!/usr/bin/env python
# encoding: utf-8


class FlyBehavior(object):

    def fly(self):
        pass


class QuackBehavior(object):

    def quack(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("can fly")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("can't fly")


class Quack(QuackBehavior):
    def quack(self):
        print("quacccccck")


class Squeak(QuackBehavior):
    def quack(self):
        print("squeaaaaak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("mute")


class Duck(object):
    def __init__(self, *behavior):
        self.flyBehavior, self.quackBehavior = behavior

    def display(self):
        pass

    def performFly(self):
        "{0}".format(self.flyBehavior.fly())

    def performQuack(self):
        "{0}".format(self.quackBehavior.quack())


class ModelDuck(Duck):
    def __init__(self):
        super(ModelDuck, self).__init__(FlyNoWay(), MuteQuack())

m1 = ModelDuck()
m1.performFly()
m1.performQuack()

