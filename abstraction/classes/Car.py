"""
Program: Car.py
Author: Paul Elsea
Last Modified: 07/11/2020

Defining the Car class.
"""

from abstraction.classes.Rider import Rider

#ar class inheriting from the abstract Rider class
class Car(Rider):
    def __init__(self, enclosed=True, engine=True):
        self._enclosed = enclosed
        self._engine = engine

    def ride(self):
        return 'Vrooom, beep beep.'

    def riders(self):
        return 'It was an absolute clown car. Arms and legs everywhere.'


if __name__ == '__main__':
    pass