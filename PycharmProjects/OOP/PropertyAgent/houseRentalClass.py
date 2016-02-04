# encoding: utf-8
from PropertyAgent.houseClass import House
from PropertyAgent.rentalClass import Rental


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
# print HouseRental.mro()
# [<class '__main__.HouseRental'>,
# <class 'PropertyAgent.rentalClass.Rental'>,
# <class 'PropertyAgent.houseClass.House'>,
# <class 'PropertyAgent.property.Property'>,
# <type 'object'>]

# [<class '__main__.HouseRental'>,
# <class 'PropertyAgent.houseClass.House'>,
# <class 'PropertyAgent.property.Property'>,
# <class 'PropertyAgent.rentalClass.Rental'>,
# <type 'object'>]