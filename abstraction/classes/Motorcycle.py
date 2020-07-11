"""
Program: Motorcycle.py
Author: Paul Elsea
Last Modified: 07/11/2020

Defining the Motorcycle class.
"""

from abstraction.classes.Rider import Rider

#Motorcycle class inheriting from the abstract Rider class
class Motorcycle(Rider):
    def __init__(self, enclosed=False, engine=True):
        self._enclosed = enclosed
        self._engine = engine

    def ride(self):
        return '400lbs and 200hp. What could go wrong?'

    def riders(self):
        return 'Very cozy accommodations for two.'


if __name__ == '__main__':
    pass