# Light sensor example for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017
# Demonstrates how to use the light sensors

from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)

# For Bit:Bot Classic
# Both light sensor are on the same pin so we also use a select pin
lightSensor = pin2
sensorSelect = pin16

# For Bit:Bot XL
leftLightSensor = pin2
rightLightSensor = pin1

def detectModel():  # Detects which model were using XL or classic
    global robotType
    try:
        value = i2c.read(28, 1, repeat=False)  # Read i2c bus
        robotType = "XL"  # If we can read it then it must be XL
        display.show("X")
    except:
        robotType = "classic"  # If we can't read it it must be classic
        display.show("C")      # or Micro:bit is unplugged
    sleep(1000)  # Do this so the user can see if the correct model is found


def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 6):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def rightLights(Red, Green, Blue):
    for pixel_id in range(6, 12):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def lightSense(model):
	if model == "classic":
		sensorSelect.write_digital(0)
		brightness = lightSensor.read_analog()
		brightness = int(brightness / 100)
		leftLights(brightness, 0, 0)
	
		sensorSelect.write_digital(1)
		brightness = lightSensor.read_analog()
		brightness = int(brightness / 100)
		rightLights(brightness, 0, 0)
	
	else:  # XL model
		brightness = leftLightSensor.read_analog()
		brightness = int(brightness / 50)
		leftLights(brightness, 0, 0)
	
		brightness = rightLightSensor.read_analog()
        brightness = int(brightness / 50)
        rightLights(brightness, 0, 0)

detectModel()

while True:
    lightSense(robotType) # use this for Classic, use lightSense("XL") for XL
