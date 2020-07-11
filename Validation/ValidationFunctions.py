"""
Program: ValidationFunctions.py
Author: Paul Elsea
Last Modified: 07/9/2020

Defining a variety of validation utility functions.
"""

from datetime import datetime as date
import re

'''Function to verify that input is valid name'''
def valid_name_check(input_string):
    result = bool(re.fullmatch(r"^[^\W0-9_]+([ :'\-‧][^\W0-9_]+)*?$", input_string))
    if result:
        return input_string
    else:
        raise ValueError('Invalid name: ' + input_string + '. Non-alphabetic or illegal connecting characters.')

'''Function to verify that input is valid customer ID'''
def valid_id_check(input_num):
    if isinstance(input_num, int):
        if len(str(input_num)) == 9:
            return input_num
        else:
            print('Error: Invalid customer ID: ' + str(input_num))
            exit()
    else:
        raise AttributeError('"Customer" object has no attribute _cust_id')

'''Function to verify that input is valid gpa'''
def valid_gpa_check(input_num):
    if isinstance(input_num, (int, float)):
        if input_num <= 4.0 and input_num >= 0.0:
            return input_num
        else:
            raise ValueError('Invalid GPA: ' + str(input_num) + '. Outside of acceptable range.')
    else:
        raise ValueError('Invalid GPA: ' + str(input_num) + '. Not int or float variable.')

'''Function to verify that input uses only alphabetic characters'''
def valid_alpha_check(input_string):
    result = input_string.replace(" ", "").isalpha()
    if result:
        return input_string
    else:
        print('Error: Invalid input: ' + str(input_string))
        exit()

'''Function to verify that input uses only alpha-numeric characters'''
def valid_alpha_num_check(input_string):
    result = input_string.replace(" ", "").replace("'", "").replace("-", "").replace(".", "").isalnum()
    if result:
        return input_string.title()
    else:
        print('Error: Invalid input: ' + str(input_string))
        exit()

'''Function to add dashes to phone nums to make them more readable in output'''
def format_phone_num(input_phone):
    if len(input_phone) == 10:
        return str(input_phone[:3] + '-' + input_phone[3:6] + '-' + input_phone[6:])
    elif len(input_phone) == 7:
        return str(input_phone[:3] + '-' + input_phone[4:])

'''Function to verify that input is valid US phone number'''
def valid_phone_check(input_num):
    result = input_num.replace(" ", "").replace('(', '').replace(')', '').replace('-', '').replace('.', '')
    if result.isnumeric():
        if len(result) == 10 or len(result) == 7:
            return result
        else:
            print('Error: Invalid phone number: ' + str(input_num))
            exit()
    else:
        print('Error: Invalid phone number: ' + str(input_num))
        exit()

'''Function to determine if state abbreviation or full name has been input'''
def state_abbrv_or_full(input_string):
    if len(input_string) <= 2:
        return valid_state_abbrv_check(input_string)
    else:
        return valid_state_check(input_string)

'''Function to verify that input is valid US state abbreviation'''
def valid_state_abbrv_check(input_string):
    state_abbrv_list = ['al', 'ak', 'as', 'az', 'ak', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'gu', 'hi', 'id', 'il',
                        'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh',
                        'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'pr', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut',
                        'vt', 'vi', 'va', 'wa', 'wv', 'wi', 'wy']
    if input_string.lower() in state_abbrv_list:
        return input_string.upper()
    else:
        print('Error: Invalid State abbreviation: ' + str(input_string))
        exit()

'''Function to verify that input is valid US state'''
def valid_state_check(input_string):
    state_list = ['alabama', 'alaska', 'american samoa', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut',
                  'delaware', 'district of columbia', 'florida', 'georgia', 'guam', 'hawaii', 'idaho', 'illinois',
                  'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts',
                  'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire',
                  'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma',
                  'oregon', 'pennsylvania', 'puerto rico', 'rhode island', 'south carolina', 'south dakota',
                  'tennessee', 'texas', 'utah', 'vermont', 'virgin islands', 'virginia', 'washington', 'west virginia',
                  'wisconsin', 'wyoming']
    if input_string.lower() in state_list:
        return input_string.title()
    else:
        print('Error: Invalid State: ' + str(input_string))
        exit()

'''Function to verify that input is float value type'''
def valid_float_num(input_string):
    try:
        verified_float = float(input_string)
        return verified_float
    except ValueError:
        print('Error: Invalid Number: ' + str(input_string))
        exit()

'''Function to verify that input is int value type'''
def valid_int_num(input_num):
    try:
        verified_int = float(input_num)
        return verified_int
    except ValueError:
        print('Error: Invalid Number: ' + str(input_num))
        exit()

'''Function to verify that input uses only alphabetic characters'''
def valid_cleaned_num_check(input_string):
    try:
        cleaned_input = int(input_string.replace("$", "").replace(",", "").replace(" ", ""))
        return cleaned_input
    except ValueError:
        print('Error: Invalid input: ' + str(input_string))

'''Function to verify that input is float value type'''
def valid_date(input_string):
    try:
        return date.strptime(input_string, '%d-%m-%Y').date()
    except ValueError:
        print('Error: Invalid Number: ' + str(input_string))
        exit()

'''Function to verify that a bool value has been input'''
def valid_bool(input_string):
    try:
        return bool(input_string)
    except ValueError:
        print('Error: Invalid Boolean: ' + str(input_string))
        exit()
