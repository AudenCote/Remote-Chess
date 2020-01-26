import time
import motorClass
import move

#ene = emailbutnotemail('jaspervosschess@gmail.com', 'Pa1n!nTheAspen')
turn = True  # True means local turn, False means turn of other board

a_motors = motorClass.Motor('A')
b_motors = motorClass.Motor('B')

# pins = [] #first 8 are output pins, running up side of board, next 14 are inputs, running along bottom of board
# for i in range(0, 8):
#     gpio.setup(pins[i], gpio.OUT)
# for i in range(8, 22):
#     gpio.setup(pins[i], gpio.IN)

steps = move.fullPlot([200, 200], [200, 210], 10)
##for s in range(len(steps)):
##    print(steps[s], end='   ')
##    if s%4 == 3:
##        print('')

for s in steps:
    if s[0] == 'A1':
        a_motors.move_step(s[1], 0)
    elif s[0] == 'A2':
        a_motors.move_step(s[1], 1)
    if s[0] == 'B1':
        b_motors.move_step(s[1], 0)
    elif s[0] == 'B2':
        b_motors.move_step(s[1], 1)
    time.sleep(.005)

# while True:         #main loop
#      if turn:
#          #sensing
#          for i in range(0, 8):
#              gpio.output(pins[i], gpio.HIGH)
#              for j in range(8, 22):
#                  if gpio.input(pins[j]) == gpio.HIGH:
