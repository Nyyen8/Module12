"""
Program: CountyDictionary.py
Author: Paul Elsea
Last Modified: 07/9/2020

Defining the CountyDictionary class.
"""
import csv
from Classes.CountyDemos import CountyDemos as cd

'''build_county_dictionary:
:csv: csv file to be read from, required
Returns: Dictionary of Iowa counties'''
def build_county_dictionary(input_csv):
    with open(input_csv) as county_csv_file:
        csv_reader = csv.reader(county_csv_file, delimiter=',')
        line_count = 0
        county_dict = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            elif row[0] == '':
                continue
            county_dict[str(row[1])] = cd(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    return county_dict


'''find_county_pop
:Function to find the population and households of a given county object from a dictionary of county objects:
:input_dict: dictionary of county objects, required
:county_name: string of county who's population is being queried, required
Returns: String with country name, population and households with connecting text'''
def find_county_pop(input_dict, county_name):
    return county_name + ' county has a population of ' + str(format(input_dict[county_name]._population, ',d')) +\
    ' spread across ' + str(format(input_dict[county_name]._number_of_households, ',d')) + ' households'

'''find_total_pop
:Function to find the total population of a dictionary of county objects:
:input_dict: dictionary of county objects, required
Returns: String with total population and text to explain number'''
def find_total_pop(input_dict):
    pop_total = 0
    for county in input_dict:
        pop_total += input_dict[county]._population
    return 'The total population is ' + str(format(pop_total, ',d'))

if __name__ == '__main__':
    iowa_counties = build_county_dictionary(r'C:\Users\15712\PycharmProjects\Module12\Data\Iowa 2010 '
                                            r'Census Data Population Income.csv')

    print(find_county_pop(iowa_counties, 'Dallas'))
    print(str(find_total_pop(iowa_counties)))