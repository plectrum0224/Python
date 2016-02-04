# encoding: utf-8
from PropertyAgent.apartmentClass import Apartment
from PropertyAgent.rentalClass import Rental


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


