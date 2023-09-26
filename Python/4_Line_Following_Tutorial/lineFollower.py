# Simple line follower for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017

# When using this code ensure that the lines the BitBot follows are
# At 35px in width, otherwise the sensor wont see them. Best way is
# to create the track on a computer and print it off.

from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)

# Motor pins; these tell the motor to go
# forward, backwards or turn
leftSpeed = pin0
leftDirection = pin8
rightSpeed = pin1
rightDirection = pin12

# Set the IR sensor pins on the bottom of the BitBot
leftLineSensor = pin11
rightLineSensor = pin5

# Both light sensor are on the same pin so we also use a select pin
lightSensor = pin2
sensorSelect = pin16


def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 6):  # Start of for loop
        np[pixel_id] = (Red, Green, Blue)  # Code to be executed in the loop
    np.show()  # Change the NeoPixels colour


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


# Motor control to tell the motor what direction and speed to move
def move(_leftSpeed, _rightSpeed, _leftDirection, _rightDirection):
    # speed values between 1 - 1023
    # smaller values == faster speed moving backwards
    # Smaller values == lower speeds when moving forwards
    # direction 0 == forwards, 1 == backwards
    leftSpeed.write_analog(_leftSpeed)  # Set the speed of left motor
    rightSpeed.write_analog(_rightSpeed)  # Set the speed of right motor
    if (_leftDirection != 2):
        leftDirection.write_digital(_leftDirection)  # left motor
        rightDirection.write_digital(_rightDirection)  # right motor


def drive(speed):
    if (speed > 0):
        move(speed, speed, 0, 0)  # move the motors forwards
    else:
        speed = 1023 + speed
        move(speed, speed, 1, 1)  # move the motors backwards


def sharpRight():
    move(100, 1023 + -200, 0, 1)


def sharpLeft():
    move(1023 + -200, 100, 1, 0)


def gentleRight():
    move(200, 0, 0, 0)


def gentleLeft():
    move(0, 200, 0, 0)


def coast():
    move(0, 0, 2, 2)


def stop():
    move(0, 0, 0, 0)


sleep(1000)
while True:
    isLeftLine = lineDetector(0)
    isRightLine = lineDetector(1)
    if(isLeftLine is True) and (isRightLine is False):
        leftLights(setBrightness(1), 0, 0)
        stop()
        sleep(50)
        sharpLeft()
        sleep(200)
        stop()
        sleep(50)
        while(lineDetector(0) is True):
            leftLights(setBrightness(1), 0, 0)
            gentleLeft()

    elif(isRightLine is True) and (isLeftLine is False):
        rightLights(setBrightness(1), 0, 0)
        stop()
        sleep(50)
        sharpRight()
        sleep(200)
        stop()
        sleep(50)
        while(lineDetector(1) is True):
            rightLights(setBrightness(1), 0, 0)
            gentleRight()

    elif(isRightLine is False) and (isLeftLine is False):
        leftLights(0, setBrightness(1), 0)
        rightLights(0, setBrightness(1), 0)
        drive(150)
    else:
        leftLights(0, setBrightness(1), setBrightness(1))
        rightLights(0, setBrightness(1), setBrightness(1))
        stop()
        sleep(200)
