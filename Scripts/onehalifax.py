import RPi.GPIO as gpio
import time


outPins = [21, 20, 16, 12, 7, 8, 25, 25]
inPins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 23]

gpio.setmode(gpio.BCM)
for i in outPins:
    gpio.setup(i, gpio.OUT)
for i in inPins:
    gpio.setup(i, gpio.IN)

while True:
    gpio.output(outPins[0], 1)
    if gpio.input(inPins[0]) == gpio.LOW:
        status = 0
    else:
        status = 1
    print(status)
    time.sleep(1)