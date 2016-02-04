# encoding: utf-8

class Purchase(object):
    def __init__(self, price = '', taxes = '', **kwargs):
        super(Purchase, self).__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super(Purchase, self).display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
        print("\n")

    def prompt_init():
        return dict(
            price = raw_input("What is the selling price? "),
            taxes = raw_input("What are the estimated taxes? ")
        )
    prompt_init = staticmethod(prompt_init)
