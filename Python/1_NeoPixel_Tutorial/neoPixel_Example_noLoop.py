# NeoPixel example for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017

# Demonstrates how to use the neoPixel library


from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)

while True:
    np[0] = (233, 108, 45)  # Set the colour for np 0
    np.show()  # show the colour
    sleep(300)  # pause for 300mS
    np[0] = (0, 0, 0)  # turn the np off
    np.show()
    np[1] = (233, 108, 45)
    np.show()
    sleep(300)
    np[1] = (0, 0, 0)
    np.show()
    np[2] = (233, 108, 45)
    np.show()
    sleep(300)
    np[2] = (0, 0, 0)
    np.show()
    np[3] = (233, 108, 45)
    np.show()
    sleep(300)
    np[3] = (0, 0, 0)
    np.show()
    np[4] = (233, 108, 45)
    np.show()
    sleep(300)
    np[4] = (0, 0, 0)
    np.show()
    np[5] = (233, 108, 45)
    np.show()
    sleep(300)
    np[5] = (0, 0, 0)
    np.show()
