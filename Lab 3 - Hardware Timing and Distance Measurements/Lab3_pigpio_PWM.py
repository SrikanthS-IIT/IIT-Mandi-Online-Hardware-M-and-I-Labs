#IMPORTANT - Before running this program, execute the following command in the terminal - sudo pigpiod

import pigpio
from time import sleep

pi = pigpio.pi()

#set GPIO Pins
pin = 12
pi.set_mode(pin, pigpio.OUTPUT)

#Use this pin to generate a PWM signal of frequency 10 Hz, and duty cycle 50%
freq = int(50)     # Frequency in Hertz, the typecasting is required.
dutycycle = 50     # Dutycycle in %

pi.hardware_PWM(pin,freq,int(dutycycle/100*1E6)) #See how the dutycycle is defined

input('Press enter to stop the program.')

#Stop pigpio
pi.write(pin,0)  #This is required to pull the output to low, otherwise the RPi will keep generating the PWM
pi.stop()

