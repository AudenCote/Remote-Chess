import RPi.GPIO as gpio
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=800, height=800, background='black')
canvas.pack()


outPins = [2, 3]
inPins = [23, 24]

gpio.setmode(gpio.BCM)
for i in outPins:
    gpio.setup(i, gpio.OUT)
for i in inPins:
    gpio.setup(i, gpio.IN)

status = []
for i in range(len(outPins)*len(inPins)):
    status.append(0)
print(status)

while True:
    for i in range(len(outPins)):
        gpio.output(outPins[i], 1)
        for j in range(len(inPins)):
            if gpio.input(inPins[j]) == gpio.LOW:
                status[i*len(inPins)+j] = 1
            else:
                status[i*len(inPins)+j] = 0
        gpio.output(outPins[i], 0)
        time.sleep(.01)
        
    rect1 = canvas.create_rectangle(0, 0, 400, 400, fill='black')
    rect2 = canvas.create_rectangle(0, 400, 400, 800, fill='black')
    rect3 = canvas.create_rectangle(400, 0, 800, 400, fill='black')
    rect4 = canvas.create_rectangle(400, 400, 800, 800, fill='black')
    if status[0] == 1:
        canvas.itemconfig(rect1, fill = 'green')
    else:
        canvas.itemconfig(rect1, fill = 'black')
    if status[1] == 1:
        canvas.itemconfig(rect2, fill = 'green')
    else:
        canvas.itemconfig(rect2, fill = 'black')
    if status[2] == 1:
        canvas.itemconfig(rect3, fill = 'green')
    else:
        canvas.itemconfig(rect3, fill = 'black')
    if status[3] == 1:
        canvas.itemconfig(rect4, fill = 'green')
    else:
        canvas.itemconfig(rect4, fill = 'black')
        
    canvas.update()
    canvas.update_idletasks()
##
##while True:
##    if gpio.input(23) == gpio.HIGH:
##        print(0)
##    elif gpio.input(23) == gpio.LOW:
##        print(1)
##    time.sleep(.25)

#.875 inch radius of sensitivity through 3/16 inch thick plywood
