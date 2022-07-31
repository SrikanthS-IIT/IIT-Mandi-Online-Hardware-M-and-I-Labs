#IMPORTANT - Before running this program, execute the following command in the terminal - sudo pigpiod

import pigpio
from time import sleep

pi = pigpio.pi()

#set GPIO Pins
pin = 12
pi.set_mode(pin, pigpio.OUTPUT)

#Use this pin to generate a 10 mu-s trigger signal
pi.gpio_trigger(pin,10,1)   #(channel number, trigger pulse width in mu-s, channel NOT level after trigger)

#Stop pigpio
pi.stop()
