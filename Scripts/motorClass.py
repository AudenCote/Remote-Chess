import RPi.GPIO as gpio
import time
import math

gpio.setmode(gpio.BCM)

class Motor:
                      #8   10   11  9
    def __init__(self, p1, p2, p3, p4):
        self.control_pins_cw = [p1, p2, p3, p4]

        for pin in self.control_pins_cw:
            gpio.setup(pin, gpio.OUT)
            
        self.curr_step = 0
        
        self.step_seq = [
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]
        ]

    def move_step(self, dir):
        self.curr_step += 1*dir
        if self.curr_step > 7:
            self.curr_step = 0
        if self.curr_step < 0:
            self.curr_step = 7
        for pin in range(4):
            gpio.output(self.control_pins_cw[pin], self.step_seq[self.curr_step][pin])

  

motor = Motor(8, 10, 11, 9)
for i in range(67890):
    motor.move_step(-1)
    time.sleep(.01)










