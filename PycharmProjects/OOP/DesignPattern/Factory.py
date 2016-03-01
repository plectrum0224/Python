# class GreekPizza(object):
#     def __init__(self):
#         self.description = "GREEK"
#
#     def prepare(self):
#         return "Prepare greek pizza"
#
#     def bake(self):
#         return "bake greek pizza"
#
# class CheesePizza(object):
#     def __init__(self):
#         self.description = "CHEESE"
#
#     def prepare(self):
#         return "Prepare cheese pizza"
#
#     def bake(self):
#         return "bake cheese pizza"
#
# #=============================================================#
# class PizzaStore(object):
#     # def __init__(self, description):
#     #     self.description = description
#     #     if self.description == "GREEK":
#     #         self.pizza = GreekPizza()
#     #     if self.description == "CHEESE":
#     #         self.pizza = CheesePizza()
#
#     def __init__(self, factory):
#         self.factory = factory
#
#     def orderPizza(self, type):
#         self.pizza = self.factory.createPizza(type)
#         print (self.pizza.prepare())
#         print (self.pizza.bake())
#
# #=============================================================#
#
# class SimpleFactory(object):
#     def createPizza(self, type):
#         self.desc = type
#         if self.desc == "GREEK":
#             self.pizza = GreekPizza()
#         if self.desc == "CHEESE":
#             self.pizza = CheesePizza()
#         return self.pizza
#
# ps = PizzaStore(SimpleFactory())
# ps.orderPizza("GREEK")
# class Pizza(object):
#     def prepare(self):
#         return "prepare pizza"
#
#     def bake(self):
#         return "bake pizza"
#
#     def cut(self):
#         return "cut pizza"
#
#     def box(self):
#         return "box pizza"
# class CheesePizza(object):
#     def prepare(self):
#         return "prepare Cheese pizza"
#     def bake(self):
#         return "bake Cheese pizza"
#     def cut(self):
#         return "cut Cheese pizza"
#     def box(self):
#         return "box Cheese pizza"
# class GreekPizza(object):
#     def prepare(self):
#         return "prepare Greek pizza"
#     def bake(self):
#         return "bake Greek pizza"
#     def cut(self):
#         return "cut Greek pizza"
#     def box(self):
#         return "box Greek pizza"
# class PepperoniPizza(object):
#     def prepare(self):
#         return "prepare Pepperoni pizza"
#     def bake(self):
#         return "bake Pepperoni pizza"
#     def cut(self):
#         return "cut Pepperoni pizza"
#     def box(self):
#         return "box Pepperoni pizza"
# # class PizzaStore(object):
# #     def orderPizza(self):
# #         self.pizza = Pizza()
# #         print(self.pizza.prepare())
# #         print(self.pizza.bake())
# #         print(self.pizza.cut())
# #         print(self.pizza.box())
# # class PizzaStore(object):
# #     def __init__(self, type):
# #         self.type = type
# #     def orderPizza(self):
# #         if self.type == "CHEESE":
# #             self.pizza = CheesePizza()
# #         if self.type == "GREEK":
# #             self.pizza = GreekPizza()
# #         if self.type == "PEPPERONI":
# #             self.pizza = PepperoniPizza()
# #         print(self.pizza.prepare())
# #         print(self.pizza.bake())
# #         print(self.pizza.cut())
# #         print(self.pizza.box())
#
# class SimplePizzaFactory(object):
#     def createPizza(self, type):
#         self.type = type
#         if self.type == "CHEESE":
#             self.pizza = CheesePizza()
#         if self.type == "GREEK":
#             self.pizza = GreekPizza()
#         if self.type == "PEPPERONI":
#             self.pizza = PepperoniPizza()
#         return self.pizza
#
# class PizzaStore(object):
#     def __init__(self):
#         self.factory = SimplePizzaFactory()
#
#     def orderPizza(self, type):
#         self.pizza = self.factory.createPizza(type)
#         print(self.pizza.prepare())
#         print(self.pizza.bake())
#         print(self.pizza.cut())
#         print(self.pizza.box())

#=============================================================================#
# class Pizza(object):
#     def prepare(self):
#         pass
#     def bake(self):
#         print("Bake for 25 min at 350")
#     def cut(self):
#         print("Cutting the pizza into diagonal slices")
#     def box(self):
#         print("Place pizza in official PizzaStore box")
#     def setName(self, name):
#         self.name = name
#     def getName(self):
#         return (self.name)
# # class NYStyleCheesePizza(Pizza):
# #     def __init__(self):
# #         self.dough = "Thin Crust Dough"
# #         self.sauce = "Marinara Sauce"
# # class NYStyleClamPizza(Pizza):
# #     def __init__(self):
# #         self.dough = "Thin Crust Dough"
# #         self.sauce = "Marinara Sauce"
# class CheesePizza(Pizza):
#     def __init__(self, ingredientFactory):
#         self.ingredientFactory = ingredientFactory
#     def prepare(self):
#         self.name = self.getName()
#         print("Prepare " + self.name)
#         self.daugh = self.ingredientFactory.createDough()
#         self.sauce = self.ingredientFactory.createSauce()
#         self.cheese = self.ingredientFactory.createCheese()
# class ClamPizza(Pizza):
#     def __init__(self, ingredientFactory):
#         self.ingredientFactory = ingredientFactory
#     def prepare(self):
#         self.name = self.getName()
#         self.daugh = self.ingredientFactory.createDough()
#         self.sauce = self.ingredientFactory.createSauce()
#         self.clam = self.ingredientFactory.createClam()
#
# #=============================================================================#
# class PizzaStore(object):
#     def createPizza(self, type):
#         pass
#     def orderPizza(self, type):
#         self.pizza = self.createPizza(type)
#         self.pizza.prepare()
#         self.pizza.bake()
#         self.pizza.cut()
#         self.pizza.box()
# class NYPizzaStore(PizzaStore):
#     def createPizza(self, item):
#         self.item = item
#         self.pizza = None
#         if self.item == "CHEESE":
#             self.pizza = CheesePizza(NYPizzaIngredientFactory())
#             self.pizza.setName("NY Style Sauce and Cheese Pizza")
#         if self.item == "CLAM":
#             self.pizza = ClamPizza(NYPizzaIngredientFactory())
#             self.pizza.setName("NY Style Sauce and Clam Pizza")
#         return self.pizza
# #=============================================================================#
# class PizzaIngredientFactory(object):
#     def createDough(self):
#         pass
#     def createSauce(self):
#         pass
#     def createCheese(self):
#         pass
#     def createPepperoni(self):
#         pass
#     def createClam(self):
#         pass
#
# class ThinCrustDough(object):
#     def __init__(self):
#         print("adding thin crust dough")
# class MarinaraSauce(object):
#     def __init__(self):
#         print("adding Marinara Sauce")
# class ReggianoCheese(object):
#     def __init__(self):
#         print("adding Reggiano Cheese")
# class SlicedPepperoni(object):
#     def __init__(self):
#         print("adding Sliced Pepperoni")
# class FreshClams(object):
#     def __init__(self):
#         print("adding Fresh Clams")
#
# class NYPizzaIngredientFactory(PizzaIngredientFactory):
#     def createDough(self):
#         return ThinCrustDough()
#     def createSauce(self):
#         return MarinaraSauce()
#     def createCheese(self):
#         return ReggianoCheese()
#     def createPepperoni(self):
#         return SlicedPepperoni()
#     def createClam(self):
#         return FreshClams()
#
# nyPizzaStore = NYPizzaStore()
# nyPizzaStore.orderPizza("CHEESE")
#=========================================================================#
class Document(object):
    def new(self):
        print ("new file")
    def open(self):
        print ("Open a file...")
    def close(self):
        print ("Close the file...")
    def save(self):
        print ("Save the file...")
class PDFDocument(object):
    def new(self):
        print ("new PDF file")
    def open(self):
        print( "Open a PDF file...")
    def close(self):
        print( "Close the PDF file...")
    def save(self):
        print( "Save the PDF file...")
class TXTDocument(object):
    def new(self):
        print ("new TXT file")
    def open(self):
        print( "Open a TXT file...")
    def close(self):
        print( "Close the TXT file...")
    def save(self):
        print( "Save the TXT file...")
class DOCDoucment(object):
    def new(self):
        print ("new DOC file")
    def open(self):
        print( "Open a DOC file...")
    def close(self):
        print( "Close the DOC file...")
    def save(self):
        print( "Save the DOC file...")
#===========================================================================#
class Application(object):
    def createDocument(self, type):
         pass
    def newDocument(self, type):
        self.doc = self.createDocument(type)
        self.doc.new()
    def openDocument(self, type):
        self.doc = self.createDocument(type)
        self.doc.open()
    def saveDocument(self, type):
        self.doc = self.createDocument(type)
        self.doc.save()

class TextApplication(Application):
    def createDocument(self, type):
        self.type = type
        if self.type == "PDF":
            return PDFDocument()
        if self.type == "TXT":
            return TXTDocument()
        if self.type == "DOC":
            return DOCDoucment()
#===========================================================================#


def main():
    ta = TextApplication()
    ta.newDocument("TXT")
    ta.openDocument("PDF")

if __name__ == '__main__':
    main()























































