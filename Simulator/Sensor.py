# uncompyle6 version 2.12.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
# [GCC 5.4.0 20160609]
# Embedded file name: .\Sensor.py
# Compiled at: 2017-08-29 16:33:33
# Size of source mod 2**32: 1866 bytes
from Vessel import Vessel
from math import pi
from Constants import *

class Sensor:

    def __init__(self, vessel):
        self._vessel = vessel
        self._value = 0
        self._unitOfMeasure = ''

    def update(self):
        pass

    def readValue(self):
        return round(self._value, 2)

    def measure(self):
        return str(self._convertToValue()) + self._unitOfMeasure

    def _convertToValue(self):
        return round(self._value, 2)


class ColourSensor(Sensor):

    def __init__(self, vessel):
        Sensor.__init__(self, vessel)
        self._unitOfMeasure = '%'

    def update(self):
        if type(self._vessel) != None:
            colour = self._vessel.getColour()
            self._value = colour * colourConversion

    def _convertToValue(self):
        return round(self._value / colourConversion, 2)


class TemperatureSensor(Sensor):

    def __init__(self, vessel):
        Sensor.__init__(self, vessel)
        self._unitOfMeasure = 'C'

    def update(self):
        if type(self._vessel) != None:
            temperature = self._vessel.getTemperature()
            self._value = temperature * tempConversion

    def _convertToValue(self):
        return round(self._value / tempConversion, 2)


class LevelSensor(Sensor):

    def __init__(self, vessel):
        Sensor.__init__(self, vessel)
        self._unitOfMeasure = 'ml'

    def update(self):
        if type(self._vessel) != None:
            level = self._vessel.getFluidAmount()
            height = level / pi / 10 / 10
            self._value = height * levelConversion

    def _convertToValue(self):
        return round(self._value / levelConversion * pi * 10 * 10, 2)

