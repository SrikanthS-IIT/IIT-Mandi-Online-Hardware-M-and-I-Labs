#ScopeRead example
#Written by Srikanth Sugavanam, IIT Mandi, 27th February 2022

#A simple program to show how to use the ScopeRead library to read and store data from the oscilloscope

import ScopeRead as scope
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

#Connecting to the scope
scope_id = scope.initialize()

#Setting the trigger level - the trigger level is set at 1.5 V for Channel 2,
#NOTE - Sweep mode is Normal, EDGE - which means that the scope will wait for a signal to appear before sweeping.
#For setting the values on Channel 1, use scope.triggerset_ch1(scope_id, triggerlevel)
scope.triggerset_ch2(scope_id,1.5)

#This is inherited from pymeasure via ScopeRead - commands the oscilloscope to take a single sweep.
#As the trigger is set to Normal and EDGE, the scope will wait for a signal to appear before it sweeps.
#This is helpful, as the Scope essentially waits for a signal to be generated, say a PWM signal from an LED Leg,
#before it starts sweeping. 
scope_id.single()

###INSERT YOUR HARDWARE CODE HERE

###INSERT YOUR HARDWARE CODE HERE

sleep(5)   #To give some time to the scope to display the acquired data. Otherwise you will run into timeout.

#Read the time and voltage axis of channel 2.
#For acquiring data on channel 1, use scope.acquire_ch1(scope_id)
data = scope.acquire_ch2(scope_id)

#Extracting the time and voltage information from the 'data' variable
t = data[0]
ch2 = data[1]

#Function that stores the time and voltage data as two CSV files
scope.store('Pot_run3',t,ch2)

plt.plot(t,ch2);
plt.show()
