#import rpyc
from Simulator.Lem_sim_interface import *

hw = lemonator.lemonator()
hw.lcd.write('test bericht')
time.sleep(3)
hw.sirup_pump.set(True)
hw.water_pump.set(True)
while hw.distance.read_mm() < 1.5:
    hw.lcd.write(str(hw.distance.read_mm()))
hw.sirup_valve.set(True)
hw.water_valve.set(True)
hw.led_yellow.set(True)
hw.lcd.write('done')

# #print(hw.keypad.getc())



