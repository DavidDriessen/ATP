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
        if self._Controller__sensors['level'].readValue() + (pressureRampDown * levelReaction) < levelSetPoint:
            if self._Controller__sensors['color'].readValue() < colourSetPoint:
                self._Controller__effectors['valveB'].switchOff()
                self._Controller__effectors['pumpB'].switchOn()
            else:
                self._Controller__effectors['valveA'].switchOff()
                self._Controller__effectors['pumpA'].switchOn()
        elif self._Controller__sensors['level'].readValue() + (pressureRampDown * levelReaction) > levelSetPoint:
            #self._Controller__effectors['pumpA'].switchOff()
            #self._Controller__effectors['pumpB'].switchOff()
            self._Controller__effectors['valveA'].switchOn()
            self._Controller__effectors['valveB'].switchOn()
