# Controller for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2018

from microbit import *
import radio

radio.on()
radio.config(channel=33)
radio.config(power=7)

while True:
    txMsg = ""
    if button_a.is_pressed() and button_b.is_pressed():
        txMsg = "F"
        display.show(Image.ARROW_N, loop=False, delay=10)
    elif button_a.is_pressed():
        txMsg = "L"
        display.show(Image.ARROW_W, loop=False, delay=10)
    elif button_b.is_pressed():
        txMsg = "R"
        display.show(Image.ARROW_E, loop=False, delay=10)
    else:
        txMsg = "S"
        display.show(Image.STICKFIGURE, loop=False, delay=10)
    radio.send(txMsg)
    sleep(10)
