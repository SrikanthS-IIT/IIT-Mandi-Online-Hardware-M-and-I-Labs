The chapter "GPIO Pads Control" teaches in some more detail about the current that can be delivered by a GPIO pin.

Of great importance are those two sentences:

If you set the pad high, you can draw up to 16mA, and the output voltage is guaranteed to be >=VOH.
Why can't I set all pins to 16 mA?--> The Raspberry Pi 3.3V supply was designed with a maximum current of ~3mA per GPIO pin. If you load each pin with 16mA, the total current is 272mA. The 3.3V supply will collapse under that level of load.
Click https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio-pads-control link to open resource.
