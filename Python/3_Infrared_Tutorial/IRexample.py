# IR sensor example for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017
# Demonstrates how to use the IR sensors TCR5000

from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)

# Both light sensor are on the same pin so we also use a select pin
lightSensor = pin2
sensorSelect = pin16

# Set the pin number of the IR detectors
leftLineSensor = pin11
rightLineSensor = pin5


def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 6):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def rightLights(Red, Green, Blue):
    for pixel_id in range(6, 12):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def setBrightness(minValue):
    sensorSelect.write_digital(0)
    brightnessLeft = lightSensor.read_analog()
    sensorSelect.write_digital(1)
    brightnessRight = lightSensor.read_analog()

    brightness = int((brightnessLeft + brightnessRight) / 2)
    brightness = int(brightness / 25)
    if(brightness < minValue):
        brightness = minValue
    return brightness


def lineDetector(side):  # 0 == left, 1 == right
    if(side == 0):
        isLine = leftLineSensor.read_digital()
    else:
        isLine = rightLineSensor.read_digital()

    if(isLine == 1):  # Sensor can see the line
        return True
    else:
        return False


while True:
    if(lineDetector(1) is True):
        rightLights(setBrightness(3), 0, 0)
    else:
        rightLights(0, 0, 0)

    if(lineDetector(0) is True):
        leftLights(setBrightness(3), 0, 0)
    else:
        leftLights(0, 0, 0)
