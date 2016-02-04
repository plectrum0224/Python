# encoding: utf-8
from PropertyAgent.GetValidValue import get_valid_input


class Rental(object):
    def __init__(self, furnished = '', utilities = '', rent = '', **kwargs):
        super(Rental, self).__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super(Rental, self).display()
        print("RENT DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
        print("\n")

    def prompt_init():
        return dict(
            rent = raw_input("What is the monthly rent? "),
            utilities = raw_input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished? ", ("yes", "no"))
        )
    prompt_init = staticmethod(prompt_init)
