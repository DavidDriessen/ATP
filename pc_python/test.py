from Simulator.Lem_sim_interface import *
# import lemonator
import time

print("Python interface demo running")
hw = lemonator.lemonator(2)

state = 1
timer1 = 0
timer2 = 0
led_state = True

while 1:
    c = hw.keypad.getc()
    if state is 1:  # Idel
        hw.lcd << "Waiting for input."
        if c is "A":
            while not hw.presence.readValue() or hw.distance.get() > 1:
                if not hw.presence.readValue():
                    hw.lcd << "Put a cup."
                elif hw.distance.get() > 1:
                    hw.lcd << "Empty the cup."
            hw.lcd << "Making lemonate."
            time.sleep(1)
            hw.sirup_valve.set(0)
            hw.water_valve.set(0)
            hw.sirup_pump.set(1)
            hw.water_pump.set(1)
            timer1 = time.clock() + 4
            timer2 = time.clock() + 3
            state = 2
        elif c is "B":
            state = 3
        elif c is "C":
            state = 4
    elif state is 2:  # Making
        hw.led_yellow.set(not led_state)
        if timer1 is 0 and timer2 is 0:
            state = 1
            hw.lcd << "Done."
            time.sleep(2)
        if timer1 < time.clock():
            hw.water_valve.set(1)
            hw.water_pump.set(0)
            timer1 = 0
        if timer2 < time.clock():
            hw.sirup_valve.set(1)
            hw.sirup_pump.set(0)
            timer2 = 0
    elif state is 3:
        pass
    elif state is 4:
        pass
