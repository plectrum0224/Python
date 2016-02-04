#coding: UTF8
# class JapaneseGetter:
#     """A simple localizer a la gettext"""
#     def __init__(self):
#         self.trans = dict(dog="狗", cat="喵", bear='嗷') #trans = {dog:'犬', cat:'猫'}
#     def get(self, msgid):
#         """We'll punt if we don't have a translation"""
#         try:
#             return unicode(self.trans[msgid], "utf-8")
#         except KeyError:
#             return unicode(msgid)
# class EnglishGetter:
#     """Simply echoes the msg ids"""
#     def get(self, msgid):
#         return unicode(msgid)
#
#
#
# def get_localizer(language="English"):
#     """The factory method"""
#     languages = dict(English=EnglishGetter, Japanese=JapaneseGetter)
#     return languages[language]()          #default return EnglishGetter()
#
# # Create our localizers
# e, j = get_localizer("English"), get_localizer("Japanese")  #e = EnglishGetter(), j = JapaneseGetter()
#
# # Localize some text
# for msgid in "dog parrot cat bear".split():
#     print e.get(msgid), j.get(msgid)

"""Implementation of the abstract factory pattern"""
import random
class PetShop:
    """A pet shop"""
    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.
        We can set it at will."""
        self.pet_factory = animal_factory
    def show_pet(self):
        """Creates and shows a pet using the
        abstract factory"""
        pet = self.pet_factory.get_pet()
        print "This is a lovely", pet
        print "It says", pet.speak()
        print "It eats", self.pet_factory.get_food()

# Stuff that our factory makes
class Dog:
    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"

# Factory classes
class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"
class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "cat food"
# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()
# Show pets with various factories
shop = PetShop()
for i in range(3):
    shop.pet_factory = get_factory()
    shop.show_pet()
    print "=" * 10
