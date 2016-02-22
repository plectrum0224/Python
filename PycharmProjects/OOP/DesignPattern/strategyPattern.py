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
#==============================================================#四个武器装备
class SwordBehavior(object):
    def __init__(self):
        self.behaviorCode = "SWORD"

    def __call__(self):
        return "use the sword"

class KnifeBehavior(object):
    def __init__(self):
        self.behaviorCode = "KNIFE"

    def __call__(self):
        return "use the knife"

class BowAndArrowBehavior(object):
    def __init__(self):
        self.behaviorCode = "BOWANDARROW"

    def __call__(self):
        return "use the bow and arrow"

class AxeBehavior(object):
    def __init__(self):
        self.behaviorCode = "AXE"

    def __call__(self):
        return "use the axe"
#==============================================================#三个人物设定
class KingFigure(object):
    def __init__(self):
        self.figureCode = "KING"

    def __call__(self):
        return "I am a king"

class QueenFigure(object):
    def __init__(self):
        self.figureCode = "QUEEN"

    def __call__(self):
        return "I am a queen"

class TrollFigure(object):
    def __init__(self):
        self.figureCode = "TROLL"

    def __call__(self):
        return "I am a troll"

class KnightFigure(object):
    def __init__(self):
        self.figureCode = "KNIGHT"

    def __call__(self):
        return "I am a knight"
#==============================================================#三种攻击策略
class attack1Method(object):
    def __init__(self):
        self.attackCode = "ATTACK1"

    def __call__(self):
        return "with attack1"

class attack2Method(object):
    def __init__(self):
        self.attackCode = "ATTACK2"

    def __call__(self):
        return "with attack2"

class attack3Method(object):
    def __init__(self):
        self.attackCode = "ATTACK3"

    def __call__(self):
        return "with attack3"
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
        self.__attackImpls = [attack1Method(),
                              attack2Method(),
                              attack3Method]

    def __call__(self, weapon, character, attack):
        for wimpl in self.__weaponImpls:
            if wimpl.behaviorCode == weapon:
                for fimpl in self.__figureImpls:
                    if fimpl.figureCode == character:
                        for aimpl in self.__attackImpls:
                            if aimpl.attackCode == attack:
                                return fimpl() + " " +wimpl() + " " + aimpl()


def main():
    chracterCreator = CharacterCreator()
    king = chracterCreator("SWORD", "KING", "ATTACK1")
    queen = chracterCreator("KNIFE", "QUEEN", "ATTACK2")
    print(king)
    print(queen)



if __name__ == '__main__':
    main()
