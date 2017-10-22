from math import pi

from Simulator.Constants import *


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


class KeyMatrix(Sensor):
    def __init__(self):
        Sensor.__init__(self, False)
        self._value = ''

    def set(self, x):
        self._value = x

    def readValue(self):
        v = self._value
        self._value = ''
        return v

    def measure(self):
        return ''


class Pin(Sensor):
    def __init__(self):
        Sensor.__init__(self, False)
        self._value = True

    def update(self):
        pass

    def set(self, val):
        self._value = val

    def readValue(self):
        return self._value

    def measure(self):
        return ''


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
