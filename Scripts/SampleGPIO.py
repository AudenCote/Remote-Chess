import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.OUT)
gpio.setup(12, gpio.IN)

gpio.output(16, gpio.LOW)
##while True:
##    gpio.output(16, gpio.HIGH)
##    time.sleep(1)
##    gpio.output(16, gpio.LOW)
##    dt = time.time()
##    while True:
##        if gpio.input(12) == gpio.HIGH:
##            print('h')
##        if gpio.input(12) == gpio.LOW:
##            dt = time.time()-dt
##            break
##    print(dt)
