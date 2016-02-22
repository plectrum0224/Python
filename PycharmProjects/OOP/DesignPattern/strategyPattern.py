#!/usr/bin/env python
# encoding: utf-8
#
#
# class FlyBehavior(object):
#
#     def fly(self):
#         pass
#
#
# class QuackBehavior(object):
#
#     def quack(self):
#         pass
#
#
# class FlyWithWings(FlyBehavior):
#     def fly(self):
#         print("can fly")
#
#
# class FlyNoWay(FlyBehavior):
#     def fly(self):
#         print("can't fly")
#
#
# class Quack(QuackBehavior):
#     def quack(self):
#         print("quacccccck")
#
#
# class Squeak(QuackBehavior):
#     def quack(self):
#         print("squeaaaaak")
#
#
# class MuteQuack(QuackBehavior):
#     def quack(self):
#         print("mute")
#
#
# class Duck(object):
#     def __init__(self, *behavior):
#         self.flyBehavior, self.quackBehavior = behavior
#
#     def display(self):
#         pass
#
#     def performFly(self):
#         "{0}".format(self.flyBehavior.fly())
#
#     def performQuack(self):
#         "{0}".format(self.quackBehavior.quack())
#
#
# class ModelDuck(Duck):
#     def __init__(self):
#         super(ModelDuck, self).__init__(FlyNoWay(), MuteQuack())
#
# m1 = ModelDuck()
# m1.performFly()
# m1.performQuack()
#==============================================================#武器策略
class SwordBehavior(object):
    def __init__(self):
        self.behaviorCode = "SWORD"

    def __call__(self):
        return "use the sword"

class KnifeBehavior(object):
    def __init__(self):
        self.behaviorCode = "KNIFE"

class BowAndArrowBehavior(object):
    def __init__(self):
        self.behaviorCode = "BOWANDARROW"

class AxeBehavior(object):
    def __init__(self):
        self.behaviorCode = "AXE"
#==============================================================#人物策略
class KingFigure(object):
    def __init__(self):
        self.figureCode = "KING"

    def __call__(self):
        return "I am a king"

class QueenFigure(object):
    def __init__(self):
        self.figureCode = "QUEEN"

class TrollFigure(object):
    def __init__(self):
        self.figureCode = "TROLL"

class KnightFigure(object):
    def __init__(self):
        self.figureCode = "KNIGHT"
#==============================================================#
class CharacterCreator(object):
    def __init__(self):
        self.__weaponImpls = [SwordBehavior(),
                        KnifeBehavior(),
                        BowAndArrowBehavior(),
                        AxeBehavior()]
        self.__figureImpls = [KingFigure(),
                              QueenFigure(),
                              TrollFigure(),
                              KnightFigure()]

    def __call__(self, weapon, character):
        for wimpl in self.__weaponImpls:
            for fimpl in self.__figureImpls:
                if wimpl.behaviorCode == weapon and fimpl.figureCode == character:
                    return fimpl() + " " +wimpl()
            else:
                return None


def main():
    chracterCreator = CharacterCreator()
    king = chracterCreator("SWORD", "KING")
    print(king)


if __name__ == '__main__':
    main()
