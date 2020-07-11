"""
Program: test_customer_exceptions.py
Author: Paul Elsea
Last Modified: 07/10/2020

Tests to verify functions from ValidationFunctions.py used in customer and customer_exception class function correctly.
"""

import unittest
from custom_exceptions.classes import customer as cust
from custom_exceptions.classes import customer_exceptions as ce

class GoodCustomerExceptionTestCases(unittest.TestCase):
    '''Method to set up test object'''
    def setUp(self):
       self.customer = cust.customer(5555, 'Last', 'First', '123-456-7890')

    '''Method to delete test object'''
    def tearDown(self):
        del self.customer

    '''Test to ensure attributes are being properly applied and don't produce exceptions'''
    def test_object_created_all_attributes(self):
        self.assertEqual(self.customer._cust_id, 5555)
        self.assertEqual(self.customer._last_name, 'Last')
        self.assertEqual(self.customer._first_name, 'First')
        self.assertEqual(self.customer._phone_num, '123-456-7890')

    '''Test to ensure str() returns proper string'''
    def test_customer_str(self):
        self.assertEqual(str(self.customer.display()), '5555\nFirst Last\n123-456-7890\n')

class CustomerBadIdExceptionTestCase(unittest.TestCase):
    '''Test to ensure bad ID results in InvalidCustomerIdException'''
    def test_bad_id_exception(self):
        with self.assertRaises(ce.InvalidCustomerIdException):
            self.customer_bad_id = cust.customer('aaaa', 'Last', 'First', '123-456-7890')
        with self.assertRaises(ce.InvalidCustomerIdException):
            self.customer_bad_id = cust.customer(999, 'Last', 'First', '123-456-7890')
        with self.assertRaises(ce.InvalidCustomerIdException):
            self.customer_bad_id = cust.customer(10000, 'Last', 'First', '123-456-7890')

class CustomerBadLNameExceptionTestCases(unittest.TestCase):
    '''Test to ensure bad last name results in InvalidNameException'''
    def test_bad_lname_exception(self):
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, '0000', 'First', '123-456-7890')
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, '', 'First', '123-456-7890')
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, 'Bad1', 'First', '123-456-7890')
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, 'Bad.', 'First', '123-456-7890')

class CustomerBadFNameExceptionTestCases(unittest.TestCase):
    '''Test to ensure bad first name results in InvalidNameException'''
    def test_bad_fname_exception(self):
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, 'Last', '0000', '123-456-7890')
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, 'Last', '', '123-456-7890')
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, 'Last', 'Bad1', '123-456-7890')
        with self.assertRaises(ce.InvalidNameException):
            self.customer_bad_id = cust.customer(5555, 'Last', 'Bad.', '123-456-7890')
        
class CustomerBadPhoneExceptionTestCases(unittest.TestCase):
    '''Test to ensure bad phone number results in InvalidPhoneNumberFormat'''
    def test_bad_phone_exception(self):
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', 'aaaaaaaaaa')
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', 'aaa-aaa-aaaa')
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', '1234567890')
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', '123456-7890')
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', '123-456789')
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', '123-456-789')
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            self.customer_bad_id = cust.customer(5555, 'Last', 'First', '123-456-78900')


if __name__ == '__main__':
    unittest.main()
