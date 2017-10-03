# uncompyle6 version 2.11.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
# [GCC 7.1.1 20170630]
# Embedded file name: .\Simulator.py
# Compiled at: 2017-08-30 16:00:41
# Size of source mod 2**32: 3405 bytes
from Controller import Controller
from Vessel import Vessel, MixtureVessel
from Sensor import *
from Effector import *
from Constants import *
from Gui import GUI
from typing import Dict
import time


class Plant:
    def __init__(self):
        self._vessels = {'mix': MixtureVessel(amount=500, temperature=36, colour=50, )}
        self._vessels['a'] = Vessel(colour=0, amount=liquidMax, flowTo=self._vessels['mix'], )
        self._vessels['b'] = Vessel(colour=100, amount=liquidMax, flowTo=self._vessels['mix'], )
        self._sensors = {'color': ColourSensor(self._vessels['mix']),
                         'temp': TemperatureSensor(self._vessels['mix']),
                         'level': LevelSensor(self._vessels['mix'])

                         }
        self._effectors = {'heater': Heater(self._vessels['mix']),
                           'pumpA': Pump(self._vessels['a']),
                           'valveA': Valve(self._vessels['a']),
                           'pumpB': Pump(self._vessels['b']),
                           'valveB': Valve(self._vessels['b'])

                           }

    def update(self):
        for vessel in self._vessels.values():
            vessel.update()

        for sensor in self._sensors.values():
            sensor.update()

        for effector in self._effectors.values():
            effector.update()

    def printState(self):
        for sensor in self._sensors.values():
            print('type:', type(sensor), 'value:', sensor.readValue(), '->', sensor.measure())

        for effector in self._effectors.values():
            print('type:', type(effector), 'value:', 'on' if effector.isOn() else 'off')


class Simulator:
    def __init__(self, gui):
        self._Simulator__plant = Plant()
        self._Simulator__controller = Controller(self._Simulator__plant._sensors, self._Simulator__plant._effectors)
        self._Simulator__monitor = Monitor(self._Simulator__plant._sensors, self._Simulator__plant._effectors)
        if gui:
            self._Simulator__gui = GUI(self._Simulator__plant, self._Simulator__controller, self._Simulator__monitor)
        else:
            self._Simulator__gui = None

    def run(self):
        if self._Simulator__gui is None:
            timestamp = 0
            while True:
                timestamp += 1
                time.sleep(1)
                print(timestamp, '-' * 40)
                self._Simulator__plant.update()
                self._Simulator__controller.update()
                self._Simulator__monitor.update()
                self._Simulator__plant.printState()

        else:
            self._Simulator__gui.run()


class Monitor:
    def __init__(self, sensors, effectors):
        self._Monitor__sensors = sensors
        self._Monitor__effectors = effectors
        self._sensorReadings = {}
        self._effectorValues = {}
        for sensor in self._Monitor__sensors:
            self._sensorReadings[sensor] = []

        for effector in self._Monitor__effectors:
            self._effectorValues[effector] = []

    def update(self):
        for sensor in self._Monitor__sensors:
            self._sensorReadings[sensor].append(self._Monitor__sensors[sensor].readValue())

        for effector in self._Monitor__effectors:
            self._effectorValues[effector].append(self._Monitor__effectors[effector].isOn())


if __name__ == '__main__':
    simulator = Simulator(True)
    simulator.run()
