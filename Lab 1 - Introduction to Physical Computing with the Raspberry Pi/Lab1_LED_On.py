import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

channel = 17

gpio.setup(channel, gpio.OUT)
gpio.output(channel,gpio.LOW)

for ii in range(5):
    gpio.output(channel,gpio.HIGH)
    sleep(5)
    gpio.output(channel, gpio.LOW)
    sleep(5)

gpio.cleanup()