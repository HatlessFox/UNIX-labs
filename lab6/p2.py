#!/usr/local/bin/python3

class Car(object):
  def who(self): print("I'm a Car")

class DriftCar(Car):
  def who(self): print("I'm a super car")

class Bulldozer(Car):
  def who(self): print("I'm a Bulldozer")

for car in [Car(), DriftCar(), Bulldozer()]: car.who()