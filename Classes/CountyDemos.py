"""
Program: CountyDemos.py
Author: Paul Elsea
Last Modified: 07/9/2020

Defining the CountyDemo class.
"""

from Validation import ValidationFunctions as vFunc

class CountyDemos():
    '''CountyDemos class constructor'''
    #Constructor

    '''CountyDemos class constructor:
    :rank: rank of all counties, required: int
    :county: name of county, required: string
    :per_capita_income: per capita income of county, required: int
    :median_household_income: median household income, required: int
    :median_family_income: median family income of county, required: int
    :population: population of county, required: int
    :number_of_households: number of households in county, required: int
    Returns: CountyDemo object with the above attributes'''
    def __init__(self, rank, county, per_capita_income, median_household_income, median_family_income, population,
                 number_of_households):
        self._rank = vFunc.valid_int_num(rank)
        self._county = vFunc.valid_name_check(county)
        self._per_capita_income = vFunc.valid_cleaned_num_check(per_capita_income)
        self._median_household_income = vFunc.valid_cleaned_num_check(median_household_income)
        self._median_family_income = vFunc.valid_cleaned_num_check(median_family_income)
        self._population = vFunc.valid_cleaned_num_check(population)
        self._number_of_households = vFunc.valid_cleaned_num_check(number_of_households)

if __name__ == '__main__':
    pass