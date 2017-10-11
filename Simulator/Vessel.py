from Constants import *


class Vessel():

    def __init__(self, amount, colour, temperature, flowTo ):
        self._amount = amount
        self._colour = colour
        self._temperature = temperature
        self._flowTo = flowTo

    def getFluidAmount(self):
        return self._amount

    def getColour(self):
        return self._colour

    def getTemperature(self):
        return self._temperature

    def flow(self):
        amount = flowRate
        if flowRate > self._amount:
            amount = self._amount
        self._amount -= amount
        if self._flowTo != None:
            self._flowTo.flowIn(amount, self._colour)

    def flowIn(self, amount, colour):
        if self._amount + amount > liquidMax:
            print('ERROR', 'overflow occuring in', type(self))
        else:
            self._colour = (self._colour * self._amount + colour * amount) / (self._amount + amount)
            self._amount += amount

    def update(self):
        """Periodically called method to update the state of the vessel"""



class MixtureVessel(Vessel):
    def __init__(self, amount, colour, temperature):
        Vessel.__init__(self, amount, colour, temperature, None)
        self._heat = False

    def heat(self, state):
        self._heat = state


    def update(self):
        if self._heat:
            self._temperature += heatRate
        elif self._temperature > environmentTemp:
            self._temperature -= temperatureDecay
