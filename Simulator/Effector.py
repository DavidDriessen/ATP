from Simulator.Vessel import Vessel, MixtureVessel
from Simulator.Constants import *

class Effector:

    def __init__(self, vessel):
        self._vessel = vessel
        self._value = False
        self._text = None

    def switchOn(self):
        self._value = True

    def switchOff(self):
        self._value = False

    def isOn(self):
        return self._value

    def update(self):
        pass

class Lcd(Effector):
    def __init__(self):
        Effector.__init__(self, False)
        self._text = ''

    def update(self):
        self._value = True

    def write(self, text):
        self._text = text


class Led(Effector):

    def __init__(self):
        Effector.__init__(self, False)


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
    def __init__(self, vessel, pump):
        Effector.__init__(self, vessel)
        self._pump = pump
        self.tick = 0

    def update(self):
        if self.tick > pressureRampDown:
            self._pump.switchOff()
            self.tick = 0
            self._value = False

        if self._value:
            self.tick += 1



class Heater(Effector):

    def update(self):
        if self._value:
            if isinstance(self._vessel, MixtureVessel):
                self._vessel.heat(True)
        elif isinstance(self._vessel, MixtureVessel):
            self._vessel.heat(False)