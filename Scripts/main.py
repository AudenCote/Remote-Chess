import time
import EmailNotEmail

ene = EmailNotEmail('jaspervosschess@gmail.com', 'Pa1n!nTheAspen')
turn = True #True means local turn, False means turn of other board

pieces = [
               ['br', 8, 4],
               ['bn', 8, 5],
               ['bb', 8, 6],
               ['bq', 8, 7],
               ['bk', 8, 8],
               ['bb', 8, 9],
               ['bn', 8, 10],
               ['br', 8, 11],
                              
               ['bp', 7, 4],
               ['bp', 7, 5],
               ['bp', 7, 6],
               ['bp', 7, 7],
               ['bp', 7, 8],
               ['bp', 7, 9],
               ['bp', 7, 10],
               ['bp', 7, 11],

               
               ['wr', 1, 4],
               ['wn', 1, 5],
               ['wb', 1, 6],
               ['wq', 1, 7],
               ['wk', 1, 8],
               ['wb', 1, 9],
               ['wn', 1, 10],
               ['wr', 1, 11],
                              
               ['wp', 2, 4],
               ['wp', 2, 5],
               ['wp', 2, 6],
               ['wp', 2, 7],
               ['wp', 2, 8],
               ['wp', 2, 9],
               ['wp', 2, 10],
               ['wp', 2, 11]
]

pins = [] #first 8 are output pins, running up side of board, next 14 are inputs, running along bottom of board
for i in range(0, 8):
    gpio.setup(pins[i], gpio.OUT)
for i in range(8, 22):
    gpio.setup(pins[i], gpio.IN)

while True:         #main loop
     if turn:
         #sensing
         for i in range(0, 8):
             gpio.out
         
        
