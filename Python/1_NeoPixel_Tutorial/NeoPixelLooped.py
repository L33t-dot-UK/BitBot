# NeoPixel example (Looped) for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017

# Demonstrates how to use the neoPixel library


from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)
while True:
    for pixel_id in range(0, 6):
        np[pixel_id] = (233, 108, 45)
        np.show()
        sleep(300)
        np[pixel_id] = (0, 0, 0)
        np.show()
