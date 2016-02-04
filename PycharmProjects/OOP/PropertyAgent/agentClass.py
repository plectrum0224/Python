# encoding: utf-8
from PropertyAgent.GetValidValue import get_valid_input
from PropertyAgent.apartmentPurchaseClass import ApartmentPurchase
from PropertyAgent.apartmentRentalClass import ApartmentRental
from PropertyAgent.housePurchaseClass import HousePurchase
from PropertyAgent.houseRentalClass import HouseRental


class Agent(object):
    type_map = {
        ("house", "rental"):HouseRental,
        ("apartment", "rental"):ApartmentRental,
        ("house", "purchase"):HousePurchase,
        ("apartment","purchase"):ApartmentPurchase
    }
    def __init__(self):
        self.property_list = []

    def display_Properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")
        ).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")
        ).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_kwargs = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_kwargs))

agent = Agent()
agent.add_property()
agent.display_Properties()