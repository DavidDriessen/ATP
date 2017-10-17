from threading import Thread
from Simulator.SimObserver import *

class input_proxy:
    def __init__(self, string, subject):
        self.string = string
        self.subject = subject

    def read_mm(self):
        return self.subject.notify_observers('read_' + self.string)


    def read_mc(self):
        return self.subject.notify_observers('read_' + self.string)


    def read_rgb(self):
        return self.subject.notify_observers('read_' + self.string)


    def getc(self):
        return self.subject.notify_observers('read_' + self.string)


    def get(self):
        return self.subject.notify_observers('read_' + self.string)


class output_proxy:
    def __init__(self, string, subject):
        self.string = string
        self.subject = subject

    def set(self, bool):
        if bool:
            self.subject.notify_observers('on_'+self.string)
        else:
            self.subject.notify_observers('off_' + self.string)

    def write(self, text):
        self.subject.notify_observers('write_' + self.string, text)

class lemonator:
    @staticmethod
    def lemonator(p):
        return lemonator_sim_interface()


class lemonator_sim_interface(Observer):
    def __init__(self):

        #init the interfaces to the simulator objects
        self.subject = Observable()
        Observer.__init__(self, self.subject)

        self.lcd         = output_proxy('lcd', self.subject)
        #self.keypad      = input_proxy('c', self.subject)
        self.distance    = input_proxy('mm', self.subject)
        self.color       = input_proxy('rgb', self.subject)
        self.temperature = input_proxy('mc', self.subject)
        self.led_yellow = output_proxy('ledY', self.subject)
        #self.pin         = input_proxy('get', self.subject)
        #self.presence    = self._Simulator__plant._sensors['pres']
        #self.heater      = output_proxy('heater', self.subject)
        self.sirup_pump  = output_proxy('pumpA', self.subject)
        self.sirup_valve = output_proxy('valveA', self.subject)
        self.water_pump  = output_proxy('pumpB', self.subject)
        self.water_valve = output_proxy('valveB', self.subject)
        #self.led_green   = output_proxy('ledG', self.subject)


        #start the thread of simulator
        thread = Thread(target=self.run)
        thread.start()






