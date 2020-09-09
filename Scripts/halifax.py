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
                status[i*len(outPins)+j] = 1
            else:
                status[i*len(outPins)+j] = 0
        gpio.output(outPins[i], 0)
        time.sleep(.01)
    for i in range(len(outPins)):
        for j in range(len(inPins)):
            print(status[i*len(outPins)+j], end='  ')
        print('')
