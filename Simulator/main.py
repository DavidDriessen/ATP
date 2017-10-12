#import rpyc
from Lem_sim_interface import *


hw = lemonator_sim_interface()
hw.lcd.write('test bericht')
hw.distance.read_mm()
hw.sirup_pump.set(True)
hw.water_pump.set(True)
while hw.distance.read_mm() < 1.5:
    hw.lcd.write(str(hw.distance.read_mm()))
hw.sirup_valve.set(True)
hw.water_valve.set(True)
hw.led_yellow.set(True)
hw.lcd.write('done')

# class lemonatorService(rpyc.Service):
#     hw = None
#     thread = None
#
#     def on_connect(self):
#         # code that runs when a connection is created
#         # (to init the serivce, if needed)
#         pass
#
#     def on_disconnect(self):
#         # code that runs when the connection has already closed
#         # (to finalize the service, if needed)
#         pass
#
#     def exposed_get_lemonator(self):  # this is an exposed method
#         return hw

#from rpyc.utils.server import ThreadedServer

#print('starting threaded server')
#t = ThreadedServer(lemonatorService, port=18861, protocol_config={"allow_public_attrs": True})
#t.start()

#print(hw.pin.get())
# #print(hw.keypad.getc())
#hw.lcd.write('test bericht')



