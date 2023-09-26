# NeoPixel example that allows control of indvidual
# LEDs for the 4tronix Bit:Bot and BBC Micro:Bit
# This code will light the LEDs with a rainbow effect
# Author David Bradshaw 2017
# Demonstrates how to use the neoPixel library
from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)
leftLightsStatus = [0, 0, 0, 0, 0, 0]  # controls which left lights are on
rightLightsStatus = [0, 0, 0, 0, 0, 0]  # controls which right lights are on

# Both light sensor are on the same pin so we also use a select pin
lightSensor = pin2
sensorSelect = pin16


# I added this so the lights arnt too bright and dont loose
# their colour properties. It dampens the colour value.
# In certain conditions the LEDs will turn off
def setDampenedValue(value):
    sensorSelect.write_digital(0)
    brightnessLeft = lightSensor.read_analog()
    sensorSelect.write_digital(1)
    brightnessRight = lightSensor.read_analog()

    brightness = int(brightnessLeft + brightnessRight) / 2
    brightness = int(brightness / 10)
    if (value == 0):
        brightness = 0
    else:
        brightness = int(brightness / (value / 150))
    print(brightness)
    return brightness


# More advanced version that allows you to light, switch offf
# or ignore individual LEDs
def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 6):
        if (leftLightsStatus[pixel_id] == 0):
            np[pixel_id] = (0, 0, 0)
        elif(leftLightsStatus[pixel_id] == 2):
            pass
        else:
            np[pixel_id] = (Red, Green, Blue)
    np.show()


def rightLights(Red, Green, Blue):
    for pixel_id in range(6, 12):
        if (rightLightsStatus[pixel_id - 6] == 0):
            np[pixel_id] = (0, 0, 0)
        elif(rightLightsStatus[pixel_id - 6] == 2):
            pass
        else:
            np[pixel_id] = (Red, Green, Blue)
    np.show()


# Makes the code simplier by allowing us to
# control both sides with one method
def setBothLights(Red, Green, Blue):
    Red = setDampenedValue(Red)
    Green = setDampenedValue(Green)
    Blue = setDampenedValue(Blue)

    leftLights(Red, Green, Blue)
    rightLights(Red, Green, Blue)


# Simplifies the code by allowing us to use 1 method to set 
# the status of the LEDs
def setBothLightStatus(a, b, c, d, e, f):
    leftLightsStatus[0] = a
    leftLightsStatus[1] = b
    leftLightsStatus[2] = c
    leftLightsStatus[3] = d
    leftLightsStatus[4] = e
    leftLightsStatus[5] = f
    rightLightsStatus[0] = a
    rightLightsStatus[1] = b
    rightLightsStatus[2] = c
    rightLightsStatus[3] = d
    rightLightsStatus[4] = e
    rightLightsStatus[5] = f


while True:
    setBothLightStatus(1, 2, 2, 2, 2, 2)
    setBothLights(204, 0, 0)
    setBothLightStatus(2, 1, 2, 2, 2, 2)
    setBothLights(204, 204, 0)
    setBothLightStatus(2, 2, 1, 2, 2, 2)
    setBothLights(0, 204, 0)
    setBothLightStatus(2, 2, 2, 1, 2, 2)
    setBothLights(0, 128, 255)
    setBothLightStatus(2, 2, 2, 2, 1, 2)
    setBothLights(127, 0, 255)
    setBothLightStatus(2, 2, 2, 2, 2, 1)
    setBothLights(255, 0, 127)
