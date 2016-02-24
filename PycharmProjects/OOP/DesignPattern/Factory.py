class GreekPizza(object):
    def __init__(self):
        self.description = "GREEK"

    def prepare(self):
        return "Prepare greek pizza"

    def bake(self):
        return "bake greek pizza"

class CheesePizza(object):
    def __init__(self):
        self.description = "CHEESE"

    def prepare(self):
        return "Prepare cheese pizza"

    def bake(self):
        return "bake cheese pizza"

#=============================================================#
class PizzaStore(object):
    # def __init__(self, description):
    #     self.description = description
    #     if self.description == "GREEK":
    #         self.pizza = GreekPizza()
    #     if self.description == "CHEESE":
    #         self.pizza = CheesePizza()

    def __init__(self, factory):
        self.factory = factory

    def orderPizza(self, type):
        self.pizza = self.factory.createPizza(type)
        print (self.pizza.prepare())
        print (self.pizza.bake())

#=============================================================#

class SimpleFactory(object):
    def createPizza(self, type):
        self.desc = type
        if self.desc == "GREEK":
            self.pizza = GreekPizza()
        if self.desc == "CHEESE":
            self.pizza = CheesePizza()
        return self.pizza

ps = PizzaStore(SimpleFactory())
ps.orderPizza("GREEK")

