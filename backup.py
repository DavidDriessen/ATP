"""
class SimSensor:

    def isSensor(self):
        return True

class SimDistance(SimSensor):

    def read_mm(self):
        print("10 cm")

class SimColor(SimSensor):

    def read_rgb(self):
        print("Red")

class SimTemperature(SimSensor):

    def read_mc(self):
        print("50 graden")

class SimPresence(SimSensor):

    def getPresence(self):
        print("Cup present")

class SimActuator:

    def set(self, bool):
        print(bool)



class Heater(SimActuator):
    def isActuator(self):
        return True

class PumpA(SimActuator):
    def isActuator(self):
        return True
class ValveA(SimActuator):
    def isActuator(self):
        return True
class PumpB(SimActuator):
    def isActuator(self):
        return True
class ValveB(SimActuator):
    def isActuator(self):
        return True
class GreenLed(SimActuator):
    def isActuator(self):
        return True
class YellowLed(SimActuator):
    def isActuator(self):
        return True




class SimulatorInterface():
    def __init__(self ):
        self.heater = Heater()
        self.pumpA = PumpA()
        self.valveA = ValveA()
        self.pumpB = PumpB()
        self.valveB = ValveB()
        self.greenLed = GreenLed()
        self.yellowLed = YellowLed()
        self.distance = SimDistance()
        self.color = SimColor()
        self.temperature = SimTemperature()
        self.presence = SimPresence()
        self.vesselA = Vessel(self.pumpA, self.valveA)
        self.vesselB = Vessel(self.pumpB, self.valveB)

hw = SimulatorInterface()

hw.heater.set(1)
hw.pumpA.set(0)
hw.valveA.set(1)
hw.pumpB.set(0)
hw.valveB.set(1)
hw.greenLed.set(0)
hw.yellowLed.set(1)
hw.distance.read_mm()
hw.color.read_rgb()
hw.temperature.read_mc()
hw.presence.getPresence()
hw.fillerA.set(0)
"""

from Simulator import Simulator
simulator = Simulator(False) # use Simulator(False) to disable the GUI
simulator.run()