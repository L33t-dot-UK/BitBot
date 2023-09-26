# NeoPixel example that allows control of indvidual
# LEDs for the 4tronix Bit:Bot and BBC Micro:Bit
# This code will light the LEDs in random order
# Author David Bradshaw 2017
# Demonstrates how to use the neoPixel library
from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights
import random

np = neopixel.NeoPixel(pin13, 12)
leftLightsStatus = [0, 0, 0, 0, 0, 0]  # controls which left lights are on
rightLightsStatus = [0, 0, 0, 0, 0, 0]  # controls which right lights are on


def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 6):
        if (leftLightsStatus[pixel_id] == 0):
            np[pixel_id] = (0, 0, 0)
        else:
            np[pixel_id] = (Red, Green, Blue)
    np.show()


def rightLights(Red, Green, Blue):
    for pixel_id in range(6, 12):
        if (rightLightsStatus[pixel_id - 6] == 0):
            np[pixel_id] = (0, 0, 0)
        else:
            np[pixel_id] = (Red, Green, Blue)
    np.show()


while True:
    delay = 100
    leftLightsStatus = [
        random.getrandbits(1), random.getrandbits(1), random.getrandbits(1),
        random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)
    ]
    rightLightsStatus = [
        random.getrandbits(1), random.getrandbits(1), random.getrandbits(1),
        random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)
    ]
    leftLights(0, 32, 0)
    rightLights(0, 32, 0)
    sleep(delay)
