"""
Program: customer_exceptions.py
Author: Paul Elsea
Last Modified: 07/10/2020

Defining the customer_exceptions classes.
"""

'''Exception for an invalid customer ID, derived from Exception base class'''
class InvalidCustomerIdException(Exception):
    pass

'''Exception for an invalid customer name, derived from Exception base class'''
class InvalidNameException(Exception):
    pass

'''Exception for an invalid customer phone number, derived from Exception base class'''
class InvalidPhoneNumberFormat(Exception):
    pass

if __name__ == '__main__':
    pass
