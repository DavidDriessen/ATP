# uncompyle6 version 2.11.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
# [GCC 7.1.1 20170630]
# Embedded file name: .\Controller.py
# Compiled at: 2017-08-29 16:53:26
# Size of source mod 2**32: 1554 bytes
from Effector import Effector
from Sensor import Sensor, TemperatureSensor, LevelSensor, ColourSensor
from Constants import *
from typing import Dict

class Controller:

    def __init__(self, sensors, effectors):
        """Controller is build using two Dictionaries:
        - sensors: Dict[str, Sensor], using strings 'temp', 'color', 'level'
        - effectors: Dict[str, Effector], using strings 'heater', 'pumpA', 'pumpB'
        """
        self._Controller__sensors = sensors
        self._Controller__effectors = effectors

    def update(self):
        if not self._Controller__effectors['heater'].isOn():
            if self._Controller__sensors['temp'].readValue() + tempReaction < tempSetPoint:
                self._Controller__effectors['heater'].switchOn()
        elif self._Controller__sensors['temp'].readValue() + tempReaction > tempSetPoint:
            self._Controller__effectors['heater'].switchOff()
        if self._Controller__sensors['level'].readValue() + levelReaction < levelSetPoint:
            if self._Controller__sensors['color'].readValue() < colourSetPoint:
                self._Controller__effectors['pumpB'].switchOn()
            else:
                self._Controller__effectors['pumpA'].switchOn()
        elif self._Controller__sensors['level'].readValue() + levelReaction > levelSetPoint:
            self._Controller__effectors['pumpA'].switchOff()
            self._Controller__effectors['pumpB'].switchOff()