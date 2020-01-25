import time
import emailbutnotemail

ene = emailbutnotemail('jaspervosschess@gmail.com', 'Pa1n!nTheAspen')
turn = True #True means local turn, False means turn of other board

pins = [] #first 8 are output pins, running up side of board, next 14 are inputs, running along bottom of board
for i in range(0, 8):
    gpio.setup(pins[i], gpio.OUT)
for i in range(8, 22):
    gpio.setup(pins[i], gpio.IN)

while True:         #main loop
     if turn:
         #sensing
         for i in range(0, 8):
             gpio.output(pins[i], gpio.HIGH)
             for j in range(8, 22):
                 if gpio.input(pins[j]) == gpio.HIGH:
                     
         
        
