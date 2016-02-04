# encoding: utf-8
from PropertyAgent.houseClass import House
from PropertyAgent.purchaseClass import Purchase


class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)