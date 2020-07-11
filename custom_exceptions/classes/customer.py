"""
Program: customer.py
Author: Paul Elsea
Last Modified: 07/10/2020

Defining the customer_exceptions class.
"""
from custom_exceptions.Validation import ValidationFunctions as vFunc
from custom_exceptions.classes import customer_exceptions as ce

class customer:
    '''customer class constructor'''

    '''CountyDemos class constructor:
    :param idnum: Number to be checked, required: 4 digit integer between 1000 and 9999 inclusive
    :param lanme: Name to be checked, required: string
    :param fname: Name to be checked, required: string        
    :param phone: Phone number to be checked, required: 10 digit number connected with dashes (###-###-####)
    Returns: customer object with the above attributes'''
    def __init__(self, idnum, lname, fname, phone):
        self._cust_id = vFunc.valid_id_check(idnum)
        self._last_name = vFunc.valid_name_check(lname)
        self._first_name = vFunc.valid_name_check(fname)
        self._phone_num = vFunc.valid_phone_check(phone)


    '''Functions to change individual characteristics of an customer object'''
    def set_cust_id(self, idnum):
        self._cust_id = vFunc.valid_id_check(idnum) #customer ID, required: 4 digit number between 1000 and 9999

    def set_last_name(self, lname):
        self._last_name = vFunc.valid_name_check(lname) #last name, required: string

    def set_first_name(self, fname):
        self._first_name = vFunc.valid_name_check(fname) #first name, required: string

    def set_phone_num(self, phone):
        self._phone_num = vFunc.valid_phone_check(phone) #phone #, required: 10 digit number formatted (###-###-####)

    '''Function to create output string based off an employee class'''
    def display(self):
        return (str(self._cust_id) + '\n' +
                (self._first_name) + ' ' + str(self._last_name) + '\n' +
                str(self._phone_num) + '\n')

if __name__ == '__main__':
    try:
        bad_customer_id = customer(5555, 'Threepwood', 'Guy', '123-456-7890')
        print(bad_customer_id.display())
    except ce.InvalidCustomerIdException:
        print('Bad customer ID')
    try:
        bad_customer_lname = customer(1234, '0000', 'Guy', '123-456-7890')
    except ce.InvalidNameException:
        print('Bad customer last name')
    try:
        bad_customer_fname = customer(1234, 'Threepwood', '0000', '123-456-7890')
    except ce.InvalidNameException:
        print('Bad customer first name')
    try:
        bad_customer_phone = customer(1234, 'Threepwood', 'Guy', 'aaa-aaa-aaaa')
    except ce.InvalidPhoneNumberFormat:
        print('Bad customer phone number')