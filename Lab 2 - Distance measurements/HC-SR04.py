#Distance measurement using HC-SR04 using software triggered pulses.

#Tasks:
#1. Complement the code under "Set GPIO pins" and "Create single trigger..." and check if the code is running
#2. Complement the code under "Compute the measured distance..." 
#3. Uncomment the code under "Prepare the scope..." and complete the code with the correct scale settings
#   Uncomment the code under "Acquire the data from scope" to acquire the data. Ensure you have the
#   ScopeRead.py in the working directory.


import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import ScopeRead as scope
import numpy as np

#Preparing the RPi------------------------------------------- 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
TRIG = 
ECHO =  
 
#set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# set Trigger to FALSE for sensor settlement
GPIO.output(TRIG, False)



#Preparing the Scope------------------------------------------ 
'''
scope_id = scope.initialize()
scope_id.single()
scope.triggerset_ch2(scope_id, )
scope.timescale_set(scope_id, )
scope.voltagescaleset_ch1(scope_id,)
scope.voltagescaleset_ch2(scope_id,)
scope.vertoffset_ch1(scope_id,)
scope.vertoffset_ch2(scope_id,)
'''
#-------------------------------------------------------------
time.sleep(1)
#-------------------------------------------------------------


#Create single trigger pulse with 10 ms on the TRIG pin

#------------------------------------------------------------


# save StartTime
while GPIO.input(ECHO) == 0:
    StartTime = time.time()

    # save time of arrival
while GPIO.input(ECHO) == 1:
    StopTime = time.time()


TimeElapsed = (StopTime - StartTime)*1E6


#Compute the measured distance in mm as per the time-of-flight

#-----------------------------------------------------------------------


#Change the data 
print('The sound travelled %d μs' %TimeElapsed)

#Acquire the data from scope and create variable for time, channel 1, channel 2
'''
time.sleep(1)
data1 = scope.acquire_ch1(scope_id)
data2 = scope.acquire_ch2(scope_id)

t = data1[0]*1E3
ch1 = data1[1]
ch2 = data2[1]
'''
#-------------------------------------------------------------------------------

GPIO.cleanup()

