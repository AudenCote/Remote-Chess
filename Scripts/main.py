import time, emailbutnotemail, motorClass

ene = emailbutnotemail('jaspervosschess@gmail.com', 'Pa1n!nTheAspen')
turn = True #True means local turn, False means turn of other board

a_motors = Motor('A')
b_motors = Motor('B')

# pins = [] #first 8 are output pins, running up side of board, next 14 are inputs, running along bottom of board
# for i in range(0, 8):
#     gpio.setup(pins[i], gpio.OUT)
# for i in range(8, 22):
#     gpio.setup(pins[i], gpio.IN)

steps = plotSteps([200, 200], [200, 400])
for steps in steps:
	if s[0] == 'A1':
		a_motors.move_step(i[1], 0)
	elif s[0] == 'A2':
		a_motors.move_step(i[1], 1)
	if s[0] == 'B1':
		b_motors.move_step(i[1], 0)
	elif s[0] == 'B2':
		b_motors.move_step(i[1], 1)    

# while True:         #main loop
#      if turn:
#          #sensing
#          for i in range(0, 8):
#              gpio.output(pins[i], gpio.HIGH)
#              for j in range(8, 22):
#                  if gpio.input(pins[j]) == gpio.HIGH:    
