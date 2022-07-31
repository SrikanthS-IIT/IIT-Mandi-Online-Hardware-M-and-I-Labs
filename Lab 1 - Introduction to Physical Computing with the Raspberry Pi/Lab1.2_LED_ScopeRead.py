import ScopeRead as scope
import RPi.GPIO as gpio
from time import sleep
import matplotlib.pyplot as plt


#==========Preparing the Oscilloscope=====================
#For initializing the connection with the oscilloscope
scope_id = scope.initialize()

#For setting the vertical scale on the oscilloscope
scope.voltagescaleset_ch1(scope_id,1)

#For setting the trigger level on the oscilloscope
scope.triggerset_ch1(scope_id,2.5)

#For setting the time window on the oscilloscope
scope.timerange_set(scope_id,1.0)

#Giving some time to the oscilloscope for making the above settings
sleep(2)

#Getting a single sweep from the oscilloscope
scope_id.single()
#==========================================================


#==================HARDWARE CODE===========================
gpio.setmode(gpio.BCM)

channel = 17

gpio.setup(channel, gpio.OUT)
gpio.output(channel,gpio.LOW)
sleep(1)

for ii in range(1):
    gpio.output(channel,gpio.HIGH)
    sleep(0.2)
    gpio.output(channel, gpio.LOW)
    sleep(0.2)

sleep(1)
#============================================================

#===================PLOTTING=================================
data = scope.acquire_ch1(scope_id)
t = data[0]
ch1 = data[1]

plt.plot(t,ch1);
plt.xlabel('Time, s')
plt.ylabel('Voltage, V')
plt.show()
#============================================================


gpio.cleanup()
