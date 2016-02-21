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

class WeaponBehavior(object):
    def useWeapon(self):
        pass


class SwordBehavior(WeaponBehavior):
    def useWeapon(self):
        print("I Use sword as my weapon!!")


class KnifeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("I Use knife as my weapon!!")


class BowAndArrowBehavior(WeaponBehavior):
    def useWeapon(self):
        print("I Use bow and arrow as my weapon!!")


class AxeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("I Use axe as my weapon!!")


class Character(object):
    def __init__(self, weapon):
        self.weaponBehavior = weapon

    def fight(self):
        return self.weaponBehavior.useWeapon()

    def setWeapon(self, weaponBehavior):
        self.weaponBehavior = weaponBehavior


class King(Character):
    def __init__(self):
        super(King, self).__init__(BowAndArrowBehavior())


class Knight(Character):
    def __init__(self):
        super(Knight, self).__init__(SwordBehavior())


class Queen(Character):
    def __init__(self):
        super(Queen, self).__init__(KnifeBehavior())


class Troll(Character):
    def __init__(self):
        super(Troll, self).__init__(AxeBehavior())


def main():
    king = King()
    king.fight()
    king.setWeapon(KnifeBehavior())
    king.fight()


if __name__ == '__main__':
    main()
