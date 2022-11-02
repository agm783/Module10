"""
invoice_class.py

Author: Andrew May

Last Modified: 10/28/2022

=========================================

This program takes in key/value pairs of priced items (items_with_price),

appends them to a dictionary, calculates the tax/grand total,

and outputs the completed invoice.

"""


class Invoice:

    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price=()):
        """
        This function initializes, and facilitates, all 7 parameters of user input.
        :param invoice_id: Invoice identification number (required)
        :param customer_id: Customer identification number (required)
        :param last_name: Customer's last name (required)
        :param first_name: Customer's first name (required)
        :param phone_number: Customer's phone number (required)
        :param address: Customer's home address (required)
        :param items_with_price: Key/Value pairs associated with store merchandise/prices (optional)
        """
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = dict(items_with_price)

    def add_item(self, item=()):
        """
        As the name implies, this function adds passed-in dictionary entries (item)
        to the Invoice Class' empty 'items_with_price' dictionary.
        :param item: Merchandise key/value pair, surrounded by curly brackets
        :return: Appends passed-in 'item' to the 'items_with_price' dictionary
        """
        self.items_with_price.update(item)

    def create_invoice(self):
        """
        This function takes all entries appended to the dictionary, sums the values,
        calculates the necessary sales tax (6%), and tallies up the grand total,
        before finally printing the generated invoice to the screen.
        :return: Invoice of customer transaction, in proper format
        """
        for key, values in self.items_with_price.items():
            print(f"{key}....${values}")
        tax_rate = .06
        tax_calc = sum(self.items_with_price.values()) * tax_rate
        print(f'Tax......${tax_calc:.2f}')
        print(f'Total....${sum(self.items_with_price.values()) + tax_calc:.2f}')


# Driver
invoice = Invoice(1, 123, 'Mouse', 'Minnie', '1313 Disneyland Dr, Anaheim, CA 92802', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
