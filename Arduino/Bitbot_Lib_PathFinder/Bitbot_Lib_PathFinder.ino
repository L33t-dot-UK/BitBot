/*
 * Bit:Bot code ported from MicroPython to C++. This code provides basic functions
 * that were worked through from tutorials 1 - 5 from www.l33t.uk/bitbot.
 * Author David Bradshaw 2018
 * 
 * Version 1.2 adds support for Neopixel Library on pin 3 for modified BitBots
 * To see how to modify the Bitbot goto https://www.l33t.uk/bitbot/?page_id=656
 * Dependcies NewPing Library; https://playground.arduino.cc/Code/NewPing
 *            Adafruit NeoPixel Library 1.1.6; https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-installation
 * 
 * If you have a unmodified Bitbot you can delete the neoPixel code however it might be easier to keep it incase you modify your
 * Bitbot at somepoint and later examples will use the neoPixel code so it would be easier to leave it.
 */



//Ultrasonic stuff
#include <NewPing.h> //Imports library to be used with HC-SR04 sensor
NewPing sonar(15, 15, 400); //Create a newPing object with a range of 400cm

//NeoPixel stuff
#include <Adafruit_NeoPixel.h>
#define PIN 3  //Pin number thats connected to the Neopiexels
#define LEDNUM 12  //number of Neopixels
Adafruit_NeoPixel neoPixels = Adafruit_NeoPixel(LEDNUM, PIN, NEO_GRB + NEO_KHZ800);


//Motor pin assignments
#define leftSpeed 0
#define leftDirection 8
#define rightSpeed 1
#define rightDirection 12

//IR assignments
#define leftLineSensor 11
#define rightLineSensor 5

//Light Sensor assignments
#define lightSensor 2
#define sensorSelect 16

/*
 * THE BELOW ARE HELPER METHODS THAT WILL MAKE BIT:BOT DO THINGS
 * SUCH AS MAKING THE MOTORS ROTATE AND TAKING READINGS FROM THE 
 * SENSORS.
 */

/*
 * NeoPixel helper methods
 * It takes 650uS to light up each neoPixel when lighting a strip of 6 neopixels.
 * This means that it will take 4.3mS to light up each side of the Bitbot.
 * With this in mind we will endevour to write to the NeoPixels as little as possible
 * A good update rate would be 1hz i.e. once per second or on colour change.
 * The neopixles brightness will be adjusted if the room is pitch black the nP's
 * will be white in colour regardless of the values you give to them.
 */
void setColour(uint8_t pixelIndex, float bF, uint8_t red, uint8_t green, uint8_t blue) //650uS Execution time
{
    neoPixels.setPixelColor(pixelIndex, neoPixels.Color(applyBF(red, bF), applyBF(green, bF), applyBF(blue, bF)));
    neoPixels.show();
}
void setColourLeft(uint8_t red, uint8_t green, uint8_t blue) //4300uS execution time
{
    float bF = getBrightnessFactor();
    for (uint8_t ii = 0; ii < 6; ii++)
    {
        setColour(ii, bF, red, green, blue);
    }
}
void setColourRight(uint8_t red, uint8_t green, uint8_t blue) //4300uS execution time
{
    float bF = getBrightnessFactor();
    for (uint8_t ii = 6; ii < 12; ii++)
    {
        setColour(ii, bF, red, green, blue);
    }
}
float getBrightnessFactor() //300uS execution time
{
    //Returns a value depending on how bright the room is so we can set the brightness
    //of the neopixels. Bright in bright rooms and dim in dark rooms
    uint32_t brightness = detectLight("LEFT");
    brightness = (brightness + detectLight("RIGHT")) / 2;  //Average brightness for left and right sensor
    float rtnValue = float(brightness) / 1000;
    if(rtnValue > 1){rtnValue = 1;}
    return rtnValue;
}
uint8_t applyBF(uint8_t colour, float brightnessFactor) //Around 12uS execution time
{
    //Changes the colour value so the Neopixels will automatically adjust their brightness
    //If a value is less than 1 it will be rounded up to a 1 in getBrightnessFactor() to 
    //stop the LEDs from switching off. This means that in very dark conditions the LEDS will
    //either turn white or a paler colour.
    colour = colour * brightnessFactor;
    if (colour < 1){colour = 1;}
    return colour;
}

/*
 * Returns the distance between Bit:Bot and an object range == 400CM
 */
int getDistance() //Takes upto 30mS to execute, upto 50mS with the delay
{
    delay(25); //settle time ensures more accurate readings                
    unsigned int uS = sonar.ping();
    int rtnVal = int(uS / US_ROUNDTRIP_CM);
    if(rtnVal == 0){rtnVal = 450;} //Out of range or somethings gone wrong
    return(rtnVal); 
}

/*
 * IR sensor function for line following
 */
boolean detectLine(uint8_t side)
{
    uint8_t isLine;
    if(side == 0)
    {
        isLine = digitalRead(leftLineSensor);
    }
    else
    {
        isLine = digitalRead(rightLineSensor);
    }
    
    if (isLine == 1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

/*
 * Light sensor
 */
uint32_t detectLight(String side)
{
    if(side.equals("LEFT"))
    {
        digitalWrite(sensorSelect, LOW);
    }
    else
    {
         digitalWrite(sensorSelect, HIGH);
    }
    return uint32_t(analogRead(lightSensor));
}

/*
 * Motor Functions
 * Due to the arduino implementation we have lost precision for the motor
 * argument speed. the values it can take is between 0 - 255. In the microPython
 * version the largest value was 1023.
 */
void move(uint8_t _leftSpeed, uint8_t _rightSpeed, uint8_t _leftDirection, uint8_t _rightDirection)
{
    analogWrite(leftSpeed, _leftSpeed);
    analogWrite(rightSpeed, _rightSpeed);
    digitalWrite(leftDirection, _leftDirection);
    digitalWrite(rightDirection, _rightDirection);
}
void forwards(uint8_t speed)
{
    move(speed, speed, 0, 0);
}
void backwards(uint8_t speed)
{
    speed = 255 - speed; 
    move(speed, speed, 1, 1);
}
void left(uint8_t speed)
{
    move(254 + -speed, speed, 1, 0);
}
void right(uint8_t speed)
{
    move(speed, 254 + -speed, 0, 1);
}



