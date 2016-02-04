# encoding: utf-8
from PropertyAgent.GetValidValue import get_valid_input


class Property(object):
    def __init__(self, square_feet = '', beds = '', baths = '', **kwargs):
        super(Property, self).__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_bathrooms = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_bathrooms))
        print("\n")

    def prompt_init():
        return dict(square_feet = raw_input("Enter the square feet: "),
                    beds = raw_input("Enter number of bedrooms: "),
                    baths = raw_input("Enter number of bathrooms: ")
                    )
    prompt_init = staticmethod(prompt_init)



