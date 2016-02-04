# encoding: utf-8
from PropertyAgent.GetValidValue import get_valid_input
from PropertyAgent.property import Property


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories = '', garage = '', fenced = '', **kwargs):
        super(House, self).__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super(House, self).display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
        print("\n")

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = raw_input("How many stories? ")
        parent_init.update({
            "fenced":fenced,
            "garage":garage,
            "num_stories":num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)