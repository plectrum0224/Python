# encoding: utf-8
from PropertyAgent.GetValidValue import get_valid_input
from PropertyAgent.property import Property


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony = '', laundry = '', **kwargs):
        super(Apartment, self).__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super(Apartment, self).display()
        print("APARTMENT DETAIL")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        print("\n")

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have?", Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have balcony?", Apartment.valid_balconies)
        parent_init.update({"laundry":laundry,
                            "balcony":balcony
                            })
        return parent_init
    prompt_init = staticmethod(prompt_init)