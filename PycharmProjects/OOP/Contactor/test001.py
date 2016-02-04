# encoding: utf-8
class ContactList(list):
    def search(self, name):
        """Return all contact that contain the search value in their name"""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts

class Contact(object):
    all_contact = ContactList()

    def __init__(self, name = '', email = '', **kwargs):
        super(Contact, self).__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

class Supplier(Contact):
    def order(self, order):
        print ("If this is a real system we would send "
               "'{}' order to '{}'".format(order, self.name))

class AddressHolder(object):
    def __init__(self, street = '', city = '', state = '', code = '', **kwargs):
        super(AddressHolder, self).__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone = '', **kwargs):
        super(Friend, self).__init__(**kwargs)
        # super(Friend, self).__init__(name, email)
        self.phone = phone



__name__ = "__main__"
f = Friend()
print f.name, f.email, f.phone
print Friend.mro()