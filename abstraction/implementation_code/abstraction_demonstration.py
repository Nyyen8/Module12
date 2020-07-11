"""
Program: abstraction_demonstration.py
Author: Paul Elsea
Last Modified: 07/11/2020

Defining functions to demonstrate abstract class children.
"""

from abstraction.classes import Car, Motorcycle, Bicycle

if __name__ == '__main__':
    bike = Bicycle.Bicycle()
    car = Car.Car()
    moto = Motorcycle.Motorcycle()

    print(bike.ride())
    print(bike.riders())
    print(car.ride())
    print(car.riders())
    print(moto.ride())
    print(moto.riders())
