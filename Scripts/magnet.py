import RPi.GPIO as gpio
import time

control_pin = 22


gpio.setmode(gpio.BCM)
gpio.setup(control_pin, gpio.OUT)

def on():
    gpio.output(control_pin, 1)
    
def off():
    gpio.output(control_pin, 0)
