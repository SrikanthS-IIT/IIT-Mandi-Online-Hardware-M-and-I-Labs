import ctypes
import os

#Import driver for sensor reading ------------------------------
wd = os.getcwd()                      #Get working directory
driver_file ="/driver_D6F_PH0505.so"  #Define driver filename
driver_filepath = wd+driver_file      #Create full path name 
sensor = ctypes.CDLL(driver_filepath) #Load driver functions
#---------------------------------------------------------------

#Read and print one data point with the pressue sensor
sensor_data_point = sensor.main()
print(sensor_data_point)

