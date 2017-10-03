# uncompyle6 version 2.11.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
# [GCC 7.1.1 20170630]
# Embedded file name: .\Effector.py
# Compiled at: 2017-08-29 16:43:31
# Size of source mod 2**32: 1451 bytes
from Vessel import Vessel, MixtureVessel
from Constants import *

class Effector:

    def __init__(self, vessel):
        self._vessel = vessel
        self._value = False

    def switchOn(self):
        self._value = True

    def switchOff(self):
        self._value = False

    def isOn(self):
        return self._value

    def update(self):
        pass


class Pump(Effector):

    def __init__(self, vessel):
        Effector.__init__(self, vessel)
        self._pressure = 0

    def update(self):
        if self._pressure > 100:
            if self._vessel != None:
                self._vessel.flow()
        if self._value:
            self._pressure = min(self._pressure + 100 / pressureRampUp, 100)
            if self._pressure == 100:
                self._pressure = 200
        else:
            self._pressure = max(self._pressure - 100 / pressureRampDown, 0)


class Valve(Effector):
    pass


class Heater(Effector):

    def update(self):
        if self._value:
            if isinstance(self._vessel, MixtureVessel):
                self._vessel.heat(True)
        elif isinstance(self._vessel, MixtureVessel):
            self._vessel.heat(False)