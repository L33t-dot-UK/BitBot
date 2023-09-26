from microbit import *  # generic microbit functionality
import neopixel  # used to illuminate the LEDs
import radio  # used to communicate with other microbits
from utime import ticks_us, sleep_us, ticks_ms  # used to calc distance

robotType = ""
SONAR = pin15

minDist = 50  # Distance in CM when the robot will turn

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

def sonar():  # This function will get distance using the sonar module

    global SONAR

    start_time = 0
    end_time = 0

    SONAR.write_digital(1) # Send 10us Ping pulse
    sleep_us(10)
    SONAR.write_digital(0)
    SONAR.set_pull(SONAR.NO_PULL)
    while SONAR.read_digital() == 0: # ensure Ping pulse has cleared
        pass
    start = ticks_us() # define starting time
    while SONAR.read_digital() == 1: # wait for Echo pulse to return
        pass
    end = ticks_us() # define ending time
    echo = end-start
    distance = int(0.01715 * echo) # Calculate cm distance
    return distance

def Drive(_leftSpeed, _rightSpeed, _leftDirection, _rightDirection):
    # speed values between 1 - 1023
    # smaller values == faster speed moving backwards
    # Smaller values == lower speeds when moving forwards
    # direction 0 == forwards, 1 == backwards
    leftSpeed.write_analog(_leftSpeed)  # Set the speed of left motor
    rightSpeed.write_analog(_rightSpeed)  # Set the speed of right motor
    if (_leftDirection != 2):
        leftDirection.write_digital(_leftDirection)  # left motor
        rightDirection.write_digital(_rightDirection)  # right motor

detectModel()

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

while True:
    # path finding alogirthm
    distance = sonar()  # get a distance measurement
    if distance < minDist:
        sleep(200)
        Drive(1, 1023, 1,1)
    else:
        Drive(1023,1023,0,0)


