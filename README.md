# Online-Hardware Measurement and Instrumentation Labs
This repository contains Python codes, configuration notes, laboratory manuals and bill of materials for realizing an online-hardware hybrid Measurement and Instrumentation lab course based around the Raspberry Pi Platform.

## Introduction
This repository contains Python codes, configuration notes, laboratory manuals and bill of materials for realizing an online-hardware hybrid Measurement and Instrumentation lab course. This course was first implemented at the School of Computing and Electrical Engineering, IIT Mandi (course module description included) in the Spring 2022 semester, and offered as IC231 - Measurement and Instrumentation. 

The course content is designed by 

- **Dr. Srikanth Sugavanam**, Assistant Professor, School of Computing and Electrical Engineering, IIT Mandi, and
- **Dr. Erwin Fuhrer**, Assistant Professor, School of Computing and Electrical Engineering, IIT Mandi. 

The course is licensed under the Creative-Commons CC-BY-NC-SA license. 

## Course Design Essentials
The course is designed to be implemented in an ‘online-hardware’ and hybrid mode. The online-hardware mode enables remote learning on real-world sensors, actuators and other electronics. The hybrid mode implies that both students present in person in the lab and those attending the course remotely can do the experiments simultaneously. 

Implementations of the experiments are centred around the Raspberry Pi, which enables the remote interrogation and control of sensors and other instruments. Remote access of the RPi is faciltiated by the VLC Connect software that comes pre-loaded with the RPi OS. 

Lab experiments are complemented by taught lectures, which are offered in step with the lab activities. The first four labs are essentially for scaffolding learning, enabling the students to become comfortable with the hardware and software aspects. To keep the emphasis on the physics and engineering aspects of the course, essential libraries and code examples are provided to the students for implementing the lab tasks. 

## Description of materials provided

### Raspberry Pi configuration note
For enabling the online-hardware based remote measurements, we used the RPi together with a Keysight DSOX1102G oscilloscope. For this, the RPis need to be configured to support serial communication via USB. In addition, several libraries need to be installed (sometimes in a sequential fashion) to implement the experiments. An application note has been provided to enable this configuration.

### Wrapper libraries
The Pymeasure library is used for communicating with the Keysight oscilloscope. However, the codes rely on an understanding of GPIB commands, and sometimes also require the use of the oscilloscope programming manual. To simplify the coding task on the students, we wrote wrapper commands for commonly used commands like setting of triggers, time and voltage axis scales, channel sweeps and acquisitions. While these are not too complicated, these help the students to focus more on the lab tasks. 
### Laboratory manuals and supporting codes
Lab manuals for the 9 experimental activities and their supporting codes are provided in the respective shared folders. The lab manuals are not written in a step-by-step ‘cookbook’ fashion, but rather present the problems or tasks that need to be addressed. The successful completion of the task required that the students read the provided reading material, and also rely on their knowledge of fundamental concepts. Clear task completion criteria are provided for each experiment, where each consequent task is dependent on the results of the previous one. The manuals also sometimes include questions that require the students to reflect on the task at hand, prompting them to think before they leap. Some basic codes are provided in the labs requiring remote control and interrogation, so that the students don’t have to start from scratch and only need to focus on the logic of the code rather than its syntax.

### Other supporting materials
Additional supporting materials in the form of datasheets, application whitepapers, or YouTube videos are provided to the students as preparation material for the lab. These link directly to the experiment at hand and facilitate task completion.
### Bill of materials
An exemplary bill of materials is provided that was used to implement the labs. This may be used to start building your own experimental kits and scale it up as per requirement.

## List of experiments
### Lab 1 - Introduction to physical computing with Raspberry PI
This is the first of the scaffolding experiments, where the students are introduced to the Raspberry Pi OS, the GPIO pins and their control using Python on the on-board Thonny IDE. Pull-up and pull-down resistor concepts are introduced by writing codes to pulse an LED using software timing. 
### Lab 2 - Time of flight distance measurement
This is the second scaffolding experiment where the commonly used HC-SR04 ultrasound detector is triggered using the RPi and distance measurements are made. Remote automation and control of the oscilloscope are introduced in this experiment. The students ultimately write a Python script for interrogating the ultrasound sensor, and also for setting the scales of the axis and the trigger levels on the oscilloscope that is directly recording the data from the sensor outputs. 
### Lab 3 - Hardware timing and distance measurement
This is an extension of the above experiment where the students see the limitations of the software based trigger and timing issues of the RPi. They are introduced to the pigpio library, which is used to obtain a much better estimate of the distance measurements from the HC-SR04. 
### Lab 4 - Digital Potentiometers
This is the last of the scaffolding experiments, where the students are introduced to the digital potentiometer X9C103. Writing the codes for remote control of the X9C103 from scratch is out of scope for the students, as it would require them to study the timing diagrams and the wiper configuration sequence. So the basic commands for moving the potentiometer wiper by one step up or down is provided to the students. Using simple logic and provided code examples, the students construct a voltage divider, and read its output using a remotely controlled oscilloscope.  
### Lab 5 - The Wheatstone bridge
This is the first experiment that introduces the students to the concept of sensors and sensor interrogation. The students mount the digital potentiometer in one of the arms of the Wheatstone bridge and measure the voltage response of the bridge as the potentiometer sweeps linearly. The students uses codes they have already developed in their previous labs, so the students quickly advance to the actual learning outcomes of the experiment, which is investigation of the nonlinear response of the bridge, and the dependence of the sensitivity on the chosen values of the resistances in the other arms of the bridge. 
### Lab 6 - Temperature measurements 
This is an exploratory lab, where the students use a thermistor and a platinum resistance thermometer to measure the temperature of a Peltier element. This introduces students to the concept of sensor mounting, calibration, and error analysis approaches. For instance, the students first have to calibrate the temperature of the Peltier element as a function of its current using a digital thermometer. This information is then used to calibrate the temperature-dependent resistance of the thermistor and PTC. Finally, the students mount the thermistor and PTC in a Wheatstone bridge configuration and read out the temperature as a function of the voltage across the bridge. 
### Lab 7 - Pressure sensors
### Lab 8 - Wind tunnel based wind velocity measurements
### Lab 9 – Innovation
In this final lab, the students are asked to develop an application by choosing a sensor or actuator from a provided list with supporting material. Some basic guidelines are provided to help students structure their strategy, and also enable uniformity of assessment across the cohort. The purpose of this lab is to show the students that they have been provided with a core skill set that will enable them to pick up any sensor or actuator from the marketplace and use it in their own application. 
