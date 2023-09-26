# NeoPixel example (Looped + Method) for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017
# Demonstrates how to use the neoPixel library
from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)


def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 6):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def rightLights(Red, Green, Blue):
    for pixel_id in range(6, 12):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


while True:
    leftLights(32, 0, 0)
    sleep(500)
    leftLights(0, 0, 0)
    rightLights(0, 0, 32)
    sleep(500)
    rightLights(0, 0, 0)
