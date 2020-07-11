"""
Program: Rider.py
Author: Paul Elsea
Last Modified: 07/11/2020

Defining the abstract Rider class.
"""

from abc import ABC, abstractmethod

#Abstract class inheriting from the abstract base class
class Rider(ABC):

    '''Empty abstract class method'''
    @abstractmethod
    def ride(self): # Empty method
        pass

    '''Empty abstract class method'''
    @abstractmethod
    def riders(self): # Empty method
        pass

if __name__ == '__main__':
    pass