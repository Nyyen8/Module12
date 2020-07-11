"""
Program: ValidationFunctions.py
Author: Paul Elsea
Last Modified: 07/10/2020

Defining a variety of validation utility functions.
"""
import re
from custom_exceptions.classes import customer_exceptions as cust_ex

'''valid_id_check function
:param input_num: Number to be checked, required: 4 digit integer between 1000 and 9999 inclusive
Returns: validated input_num or InvalidIdException exception'''
def valid_id_check(input_num):
    if isinstance(input_num, int):
        if input_num >= 1000 and input_num <= 9999:
            return input_num
        else:
            raise cust_ex.InvalidCustomerIdException('Input "' + str(input_num) + '" outside of acceptable range'
                                                         r'(1000-9999)')
    else:
        raise cust_ex.InvalidCustomerIdException('Input "' + str(input_num) + '" is not an integer.')

'''valid_name_check function
:param input_string: Name to be checked, required: string
Returns: validated input_string or InvalidNameException exception'''
def valid_name_check(input_string):
    result = bool(re.fullmatch(r"^[^\W0-9_]+([ :'\-‧][^\W0-9_]+)*?$", input_string))
    if result:
        return input_string
    else:
        raise cust_ex.InvalidNameException('Invalid name: ' + input_string + '. Non-alphabetic or '
        r'illegal connecting characters.')


'''valid_phone_check function
:param input_num: Phone number to be checked, required: 10 digit number connected with dashes (###-###-####)
Returns: validated input_string or InvalidPhoneNumberFormat exception'''
def valid_phone_check(input_num):
    result = bool(re.fullmatch("^[0-9-]*$", input_num))
    if result:
        cleaned_num = input_num.replace("-", "")
        if len(str(cleaned_num)) == 10:
            if input_num[3] == '-':
                if input_num[7] == '-':
                    return input_num
                else:
                    raise cust_ex.InvalidPhoneNumberFormat(
                        'Input "' + str(input_num) + '" missing "-" between 6th and 7th number.')
            else:
                raise cust_ex.InvalidPhoneNumberFormat(
                    'Input "' + str(input_num) + '" missing "-" between 3rd and 4th number.')
        else:
            raise cust_ex.InvalidPhoneNumberFormat('Input "' + str(input_num) + '" is the wrong length.')
    else:
        raise cust_ex.InvalidPhoneNumberFormat('Input "' + str(input_num) + '" has illegal characters.')

if __name__ == '__main__':
    pass