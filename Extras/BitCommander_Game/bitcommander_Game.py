#Micro:bit game designed for Bit:Commander
#Author David Bradshaw 2018

from microbit import *
import radio
import random
import music
import neopixel

np = neopixel.NeoPixel(pin13, 6)

radio.on()
radio.config(channel=33)
radio.config(power=7)

yVal = 0

button_green = pin14
button_red = pin12
button_yellow = pin16
button_blue = pin15
dial = pin0

def setLEDs(start, end, red, green, blue):
    for pixel_id in range(start, end):  # Start of for loop
        np[pixel_id] = (red, green, blue)  # Code to be executed in the loop
    np.show()

while True:
    inProgress = False
    isSelecting = False
    isCorrect = False
    ticks = 0
    score = 0
    
    
    while (inProgress == False):
        display.show(Image.SMILE)
        if(button_a.is_pressed() == True and button_b.is_pressed() == True):
            inProgress = True
            music.play(music.POWER_UP)
            score = 0
            ticks = 0
            maxTicks = 2500 # about 34 seconds each tick around 13.6 mS
             
    #Game loop
    while (inProgress == True):
        target = random.randint(1,6)
        random.seed(ticks)
        display.show(str(target))
        value = -1
        direction = 0
        targetSelected = False
        
        colour = random.randint(0,3)
        RGB = [0,0,0]
        #set colour
        if(colour == 0):
            #red
            RGB = [8,0,0]
        elif(colour == 1):
            #green
            RGB = [0,8,0]
        elif(colour == 2):
            #blue
            RGB = [0,0,8]
        elif(colour == 3):
            #yellow
            RGB = [8,8,0]
 
        isSelecting = True  
        #colour and number selection loop
        while(isSelecting == True):
            targetSelected = False
            sleep(1)
            ticks = ticks + 1
            txPacket = str(score) + "," + str(ticks) + "," + str(maxTicks)
            radio.send(txPacket)
            print(txPacket)
            
            yVal = pin2.read_analog()
            
            if (yVal > 512 and yVal > 25 + 512):
                direction = 0 # 0 = up
                yVal = (yVal - 512) * 2
            elif (yVal < 25 + 512 and yVal > 512 - 25):
                yVal = 0
                direction = 0
            elif (yVal < 512):
                direction = 1
                yVal = yVal * 2
                if (yVal < 0):
                    yVal = 0
            #LED light up stuff
            setLEDs(0,6,0,0,0) 
            if(yVal < 20 and direction == 0): #Stick is centered turn lights off
                setLEDs(0,6,0,0,0)
            elif (yVal < 200):
                if(direction == 0):
                    setLEDs(0,1,RGB[0],RGB[1],RGB[2])
                    value = 1
                else:
                    setLEDs(0,6,RGB[0],RGB[1],RGB[2])
                    value = 6
            elif (yVal < 400):
                if(direction == 0):
                    setLEDs(0,2,RGB[0],RGB[1],RGB[2])
                    value = 2
                else:
                    setLEDs(0,5,RGB[0],RGB[1],RGB[2])
                    value = 5
            elif (yVal < 550):
                if(direction == 0):
                    setLEDs(0,3,RGB[0],RGB[1],RGB[2])
                    value = 3
                else:
                    setLEDs(0,4,RGB[0],RGB[1],RGB[2])
                    value = 4
            elif (yVal < 725):
                if(direction == 0):
                    setLEDs(0,4,RGB[0],RGB[1],RGB[2])
                    value = 4
                else:
                    setLEDs(0,3,RGB[0],RGB[1],RGB[2])
                    value = 3
            elif (yVal < 850):
                if(direction == 0):
                    setLEDs(0,5,RGB[0],RGB[1],RGB[2])
                    value = 5
                else:
                    setLEDs(0,2,RGB[0],RGB[1],RGB[2])
                    value = 2
            elif (yVal < 1030):
                if(direction == 0):
                    setLEDs(0,6,RGB[0],RGB[1],RGB[2])
                    value = 6
                else:
                    setLEDs(0,1,RGB[0],RGB[1],RGB[2])
                    value = 1
           
            if(value == target): # correct amount of lights lit up
                #now check the buttons
                if(colour == 0 and button_red.read_digital() == 1):
                    isCorrect = True
                elif(colour == 1 and button_green.read_digital() == 1):
                    isCorrect = True
                if(colour == 2 and button_blue.read_digital() == 1):
                    isCorrect = True
                if(colour == 3 and button_yellow.read_digital() == 1):
                    isCorrect = True
                if(isCorrect == True):
                    isSelecting = False
                    
            #incorrect choice
            if(button_yellow.read_digital() == 1 or button_red.read_digital() == 1 or button_green.read_digital() == 1 or button_blue.read_digital() == 1):
                if(value != target):
                    isSelecting = False # new number and colour is chosen
                    music.play(music.JUMP_DOWN)
            if(button_red.read_digital() == 1 and colour != 0):
                isSelecting = False # new number and colour is c
                music.play(music.JUMP_DOWN)
            elif(button_green.read_digital() == 1 and colour != 1):
                isSelecting = False # new number and colour is c
                music.play(music.JUMP_DOWN)
            elif(button_blue.read_digital() == 1 and colour != 2):
                isSelecting = False # new number and colour is 
                music.play(music.JUMP_DOWN)
            elif(button_yellow.read_digital() == 1 and colour != 3):
                isSelecting = False # new number and colour is 
                music.play(music.JUMP_DOWN)
                
            if (ticks > maxTicks):
                inProgress = False
                setLEDs(0,6,0,0,0)
                music.play(music.PUNCHLINE)
                display.scroll(str(score), 200)
                isSelecting = False

        if(isCorrect == False):
            score = score - 1
            if(score < 0):
                score = 0

        if(isCorrect == True):
            score = score + 1
            setLEDs(0,value,12,12,12)
            music.play(music.BA_DING)
            isCorrect = False
            maxTicks = maxTicks + 36 #add 36 ticks for correct answer 500 mS
        