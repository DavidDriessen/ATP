from Simulator import *

class Observable:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            return observer.notify(self, *args, **kwargs)


class Observer(Simulator):
    def __init__(self, observable):
        Simulator.__init__(self, True)
        observable.register_observer(self)




    def notify(self, observable, *args, **kwargs):
        if args[0] == 'read_mc':
            val = self._Simulator__plant._sensors['temp'].readValue()

        elif args[0] == 'read_rgb':
            val = self._Simulator__plant._sensors['color'].readValue()

        elif args[0] == 'read_mm':
            val = self._Simulator__plant._sensors['level'].readValue()

        elif args[0] == 'on_heater':
            val = self._Simulator__plant._effectors['heater'].switchOn()

        elif args[0] == 'off_heater':
            val = self._Simulator__plant._effectors['heater'].switchOff()

        elif args[0] == 'on_valveA':
            val = self._Simulator__plant._effectors['valveA'].switchOn()

        elif args[0] == 'on_valveB':
            val = self._Simulator__plant._effectors['valveB'].switchOn()

        elif args[0] == 'off_valveA':
            val = self._Simulator__plant._effectors['valveA'].switchOff()

        elif args[0] == 'off_valveB':
            val = self._Simulator__plant._effectors['valveB'].switchOff()

        elif args[0] == 'on_pumpA':
            val = self._Simulator__plant._effectors['pumpA'].switchOn()

        elif args[0] == 'on_pumpB':
            val = self._Simulator__plant._effectors['pumpB'].switchOn()

        elif args[0] == 'off_pumpA':
            val = self._Simulator__plant._effectors['pumpA'].switchOff()

        elif args[0] == 'off_pumpB':
            val = self._Simulator__plant._effectors['pumpB'].switchOff()

        elif args[0] == 'on_ledG':
            val = self._Simulator__plant._effectors['ledG'].switchOn()

        elif args[0] == 'on_ledY':
            val = self._Simulator__plant._effectors['ledY'].switchOn()

        elif args[0] == 'off_ledG':
            val = self._Simulator__plant._effectors['ledG'].switchOff()

        elif args[0] == 'off_ledY':
            val = self._Simulator__plant._effectors['ledY'].switchOff()

        elif args[0] == 'read_c':
            val = self._Simulator__plant._sensors['key'].readValue()

        elif args[0] == 'read_get':
            val = self._Simulator__plant._sensors['pin_in'].readValue()

        elif args[0] == 'write_lcd':
            val = self._Simulator__plant._effectors['lcd'].write(args[1])

        else:
            print('unknown command')

        return val


