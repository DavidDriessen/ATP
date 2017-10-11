from threading import Thread

from Lem_sim_interface import *
import rpyc


class lemonatorService(rpyc.Service):
    hw = None

    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        self.hw = lemonator_sim_interface()

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_lemonator(self):  # this is an exposed method
        return self.hw

    def exposed_run(self):  # this is an exposed method
        thread = Thread(target=self.hw.run)
        thread.start()


from rpyc.utils.server import ThreadedServer

t = ThreadedServer(lemonatorService, port=18861, protocol_config={"allow_public_attrs": True})
t.start()

# print(hw.pin.get())
# print(hw.keypad.getc())
# hw.lcd.write('test bericht')
# hw.heater.set(True)
# hw.heater.set(False)
# hw.sirup_pump.set(True)
# hw.water_pump.set(True)
# print(hw.distance.read_mm())
# print(hw.distance.read_mm())
# print(hw.distance.read_mm())
# print(hw.distance.read_mm())
# print(hw.distance.read_mm())
# print(hw.distance.read_mm())
# hw.sirup_valve.set(True)
# hw.water_valve.set(True)
# print(hw.distance.read_mm())
# print(hw.distance.read_mm())
# hw.led_green.set(True)
# hw.led_green.set(False)
# hw.led_yellow.set(True)
