#Remote display for micro:bit game
#Author David Bradshaw 2018

from microbit import *
import radio

radio.on()
radio.config(channel=33)
radio.config(power=7)

while True:
    score = '0'
    time = 1
    maxTime = 1
    display.show(score)
    mode = 0 # 0 = score mode, 1 = time mode, 2 = both 5 second delay
    subMode = 0
    
    currentTicks = 0
    lastTicks = 0
    incomingList  = ["0","0","0"]
    
    while (-1):
        if(button_a.is_pressed()):
            mode = 2
            sleep(750)
        if(button_b.is_pressed()):
            if(mode == 0):
                mode = 1
                sleep(750)
            else:
                mode = 0
                sleep(750)
        
        sleep(30)
        try:
            incoming = radio.receive()
            elapsedPercent = (int(time)) / int(maxTime)
            if incoming is not None:
                incomingList = incoming.split(',')
                print(incoming)
                score = incomingList[0]
                time = incomingList[1]
                maxTime = incomingList[2]
                elapsedPercent = (int(time)) / int(maxTime)
     
            if(mode == 2):
                currentTicks = int(incomingList[1])
                if (currentTicks - lastTicks > 360):
                    lastTicks = currentTicks
                    if(subMode == 0):
                        subMode = 1
                    else:
                        subMode = 0
                    
            if (mode == 0 or (mode == 2 and subMode == 0)):
                if(int(score) < 10 and int(score) > -10):
                    display.show(score)
                elif(int(score) < -10):
                    display.scroll(score, 100)
                else:
                    display.scroll(score, 100)
            if(mode == 1 or (mode == 2 and subMode == 1)):
                if(elapsedPercent < 0.04):
                    display.show(Image('09999:99999:99999:99999:99999'))
                elif(elapsedPercent < 0.08):
                    display.show(Image('00999:99999:99999:99999:99999'))
                elif(elapsedPercent < 0.12):
                    display.show(Image('00099:99999:99999:99999:99999'))
                elif(elapsedPercent < 0.16):
                    display.show(Image('00009:99999:99999:99999:99999'))
                elif(elapsedPercent < 0.20):
                    display.show(Image('00000:99999:99999:99999:99999'))
                elif(elapsedPercent < 0.24):
                    display.show(Image('00000:09999:99999:99999:99999'))
                elif(elapsedPercent < 0.28):
                    display.show(Image('00000:00999:99999:99999:99999'))
                elif(elapsedPercent < 0.32):
                    display.show(Image('00000:00099:99999:99999:99999'))
                elif(elapsedPercent < 0.36):
                    display.show(Image('00000:00009:99999:99999:99999'))
                elif(elapsedPercent < 0.40):
                    display.show(Image('00000:00000:99999:99999:99999'))
                elif(elapsedPercent < 0.44):
                    display.show(Image('00000:00000:09999:99999:99999'))
                elif(elapsedPercent < 0.48):
                    display.show(Image('00000:00000:00999:99999:99999'))
                elif(elapsedPercent < 0.52):
                    display.show(Image('00000:00000:00099:99999:99999'))
                elif(elapsedPercent < 0.56):
                    display.show(Image('00000:00000:00009:99999:99999'))
                elif(elapsedPercent < 0.60):
                    display.show(Image('00000:00000:00000:99999:99999'))
                elif(elapsedPercent < 0.64):
                    display.show(Image('00000:00000:00000:09999:99999'))
                elif(elapsedPercent < 0.68):
                    display.show(Image('00000:00000:00000:00999:99999'))
                elif(elapsedPercent < 0.72):
                    display.show(Image('00000:00000:00000:00099:99999'))
                elif(elapsedPercent < 0.76):
                    display.show(Image('00000:00000:00000:00009:99999'))
                elif(elapsedPercent < 0.80):
                    display.show(Image('00000:00000:00000:00000:99999'))
                elif(elapsedPercent < 0.84):
                    display.show(Image('00000:00000:00000:00000:09999'))
                elif(elapsedPercent < 0.88):
                    display.show(Image('00000:00000:00000:00000:00999'))
                elif(elapsedPercent < 0.92):
                    display.show(Image('00000:00000:00000:00000:00099'))
                elif(elapsedPercent < 0.96):
                    display.show(Image('00000:00000:00000:00000:00009'))
                elif(elapsedPercent < 1):
                    display.show(Image('00000:00000:00000:00000:00000'))
                else:
                    display.show(Image('99999:99999:99999:99999:99999'))
        except:
            pass
