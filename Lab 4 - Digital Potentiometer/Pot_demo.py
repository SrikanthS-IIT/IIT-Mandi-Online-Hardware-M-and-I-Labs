import X9C103_BCM as pot

CS = 16
INC = 20
UD = 21
#GND = pin34
delay = 0.1

pot.initiate(CS,INC,UD)
pot.activate(CS,INC,UD)

flag = 1 #Wiper move up or down direction set.

no_of_steps = 10

pot.wiperset(CS,INC,UD,flag);

pot.wipermove(CS,INC,UD,no_of_steps);

pot.disconnect(CS,INC,UD)
