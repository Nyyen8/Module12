"""
Program: Bicycle.py
Author: Paul Elsea
Last Modified: 07/11/2020

Defining the Bicycle class.
"""

from abstraction.classes.Rider import Rider

#Bicycle class inheriting from the abstract Rider class
class Bicycle(Rider):
    def __init__(self, enclosed=False, engine=False):
        self._enclosed = enclosed
        self._engine = engine

    def ride(self):
        return "Pedal powered. It doesn't get easier, you just go faster"

    def riders(self):
        return 'Just the one.'

if __name__ == '__main__':
    pass