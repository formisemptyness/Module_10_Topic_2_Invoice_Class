'''
Program: invoice.py
Author: Joshua M. McGinley
Last date modified: 11/08/2022

Write an Invoice class with the following data members, which are identified as required or optional in the
constructor.

    invoice_id - required
    customer_id - required
    last_name - required
    first_name - required
    phone_number - required
    address - required
    items_with_price - dictionary, optional

Methods:

    constructor that sets all required items as listed above and uses appropriate default values for optional
    built-ins (str() and repr())
    add_item() that adds an item to items_with_price dictionary (Recall: what is the dictionary function to add?)
    create_invoice() that prints each item and price, then a total with tax calculated

Driver:

# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

Output:
iPad.....$799.99
Surface.....$999.99
Tax......... $108.00
Total.......$1907.98
'''

class Invoice:

    def __init__(self, cid, iid, addy, fname, lname, pnum, item_dict = dict()):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        #customer_id_characters = set("1234567890")
        #invoice_id_characters = set("1234567890")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not phone_number_characters.issuperset(pnum):
            raise ValueError
        #if not customer_id_characters.issuperset(cid):
        #    raise ValueError
        #if not invoice_id_characters.issuperset(iid):
        #    raise ValueError
        self.invoice_id = iid
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnum
        self.address = addy
        self.items = item_dict
    def __str__(self):
        return self.invoice_id + self.customer_id + ": " + self.address + ", " + self.last_name + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return  'Invoice({},{},{},{},{},{})'.format(self.invoice_id, self.customer_id, self.address, self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def change_address(self, addy):
        self.address = addy


    def add_item(self, item_dict = {'':0.0}):
        self.items.update(item_dict)


    def create_invoice(self):
        tax = .06
        subtotal = (sum(self.items.values()))
        tax = (subtotal * tax)
        tax = round(tax)
        total = subtotal + tax
        for key, value in self.items.items():
            print(key,'....${0:.2f}'.format(value))
        print('Tax.........${0:.2f}'.format(tax))
        print('Total........${0:.2f}'.format(total))


# Driver code
if __name__== "__main__":
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()

'''
Output:
iPad.....$799.99
Surface.....$999.99
Tax......... $108.00
Total.......$1907.98
'''
