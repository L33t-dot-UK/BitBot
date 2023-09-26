# Light avoider/follower for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2017

# Will either avoid or follow light

from microbit import *
import neopixel  # Neopixel Library so we can control the NeoPixels lights

np = neopixel.NeoPixel(pin13, 12)

robotType = ""

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

detectModel()  # Call the above function

# Motor pins; these tell the motor to go
# forward, backwards or turn
if robotType == "classic":
    leftSpeed = pin0
    leftDirection = pin8
    rightSpeed = pin1
    rightDirection = pin12

else:  # Bit:Bot XL
    leftSpeed = pin16
    leftDirection = pin8
    rightSpeed = pin14
    rightDirection = pin12


# Both light sensors are on the same pin so we also use a select pin
if robotType == "classic":
    lightSensor = pin2
    sensorSelect = pin16

else:  # Bit:Bot XL
    leftLightSensor = pin2
    rightLightSensor = pin1



refLevel = 0  # Reference light level
mode = 0


def leftLights(Red, Green, Blue):
    for pixel_id in range(0, 1):  # Start of for loop
        np[pixel_id] = (Red, Green, Blue)  # Code to be executed in the loop
    np.show()  # Change the NeoPixels colour


def rightLights(Red, Green, Blue):
    for pixel_id in range(6, 7):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def setBrightness(minValue):
    global robotType
    if robotType == "classic":
        sensorSelect.write_digital(0)
        brightnessLeft = lightSensor.read_analog()
        sensorSelect.write_digital(1)
        brightnessRight = lightSensor.read_analog()
    else:  # Bit:Bot XL
        brightnessLeft = leftLightSensor.read_analog()
        brightnessRight = rightLightSensor.read_analog()

    brightness = int((brightnessLeft + brightnessRight) / 2)
    brightness = int(brightness / 25)
    if(brightness < minValue):
        brightness = minValue
    return brightness


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


def lightMove(direction):
    global robotType
    if robotType == "classic":
        sensorSelect.write_digital(0)  # select left sensor
        brightnessLeft = lightSensor.read_analog()  # read value
        sensorSelect.write_digital(1)  # select right sensor
        brightnessRight = lightSensor.read_analog()  # read value
    else:  # Bit:Bot XL
        brightnessLeft = leftLightSensor.read_analog()
        brightnessRight = rightLightSensor.read_analog()

    avgBrightness = int((brightnessLeft + brightnessRight) / 2)

    if (avgBrightness <= refLevel + 10):
        stop()  # stop Moving
        if (refLevel >= 900):  # LEDs are blue to indicate very bright room
            leftLights(0, setBrightness(1), setBrightness(1))
            rightLights(0, setBrightness(1), setBrightness(1))
        else:  # LEDs are pinkish to indicate a dim room
            leftLights(setBrightness(1), 0, setBrightness(1))
            rightLights(setBrightness(1), 0, setBrightness(1))

    elif(brightnessLeft > brightnessRight - 25) and (brightnessLeft < brightnessRight + 25):
        if (direction == 1):
            drive(-512)  # drive backwards
        else:
            drive(512)  # drive forwards
        leftLights(setBrightness(1), setBrightness(1), 0)
        rightLights(setBrightness(1), setBrightness(1), 0)

    else:  # turn the robot
        if (direction == 1):
            move(brightnessLeft, brightnessRight, direction, direction)
            leftLights(setBrightness(1), 0, 0)
            rightLights(setBrightness(1), 0, 0)
        else:
            move(brightnessRight, brightnessLeft, direction, direction)
            leftLights(0, setBrightness(1), 0)
            rightLights(0, setBrightness(1), 0)


def setReference():
    global robotType
    if robotType == "classic":
        sensorSelect.write_digital(0)  # select left sensor
        val1 = lightSensor.read_analog()  # read value
        sensorSelect.write_digital(1)  # select right sensor
        val2 = lightSensor.read_analog()
    else:
        val1 = leftLightSensor.read_analog()  # read value
        val2 = rightLightSensor.read_analog()
    return int((val1 + val2) / 2)


sleep(1000)
refLevel = setReference()

while True:
    buttonA = button_a.get_presses()  # Get how many times bA was pressed
    buttonB = button_b.get_presses()  # Get how many times bB was pressed
    if (buttonA > buttonB):  # If bA was pressed more than bB then mode 1
        mode = 1
    elif(buttonB > buttonA):  # If bB was pressed more go into mode 2
        mode = 2
        # If no buttons were pressed stay in whatever mode it was in before
    if(mode == 1):
        lightMove(0)  # If in mode 1 call lightFollower method
        display.show("F")
    elif(mode == 2):
        lightMove(1)
        display.show("A")
    else:
        display.show("N")
