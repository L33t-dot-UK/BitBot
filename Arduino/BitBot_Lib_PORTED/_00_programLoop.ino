void setup() {
    // put your setup code here, to run once:
    pinMode(leftSpeed, OUTPUT); //Set pin modes, this is not needed for HC-SR04 pins
    pinMode(leftDirection, OUTPUT);
    pinMode(rightSpeed, OUTPUT);
    pinMode(rightDirection, OUTPUT);
      
    pinMode(leftLineSensor, INPUT); 
    pinMode(rightLineSensor, INPUT);

    pinMode(lightSensor, INPUT);
    pinMode(sensorSelect, OUTPUT);
  
    Serial.begin(115200); //Setup the serial port so we can get debug data

    pinMode(PIN, OUTPUT); //Set the pinmode for the neopixels
    neoPixels.begin(); //initilise the neoPixel object
    neoPixels.show(); 
}

/*
 * THIS IS THE PROGRAM LOOP PUT CODE HERE THAT WILL BE ITERATED THROUGH
 * USING THE HELPER METHODS BELOW.
 */
void loop() 
{
    //---- Used to calculate the time taken for the main program loop to iterate ----
    unsigned long startTime;
    unsigned long endTime;
    unsigned long runTime;
    startTime = micros();
    //---- End of program loop calc stuff ----

    /*
    * PUT YOUR MAIN LOOP CODE HERE
    */
    neoPixels.clear();
    setColourRight(255,0,0);
    delay(500);
    neoPixels.clear();
    setColourLeft(0,255,0);
    delay(500);
    
  // ---- Calculate program loop runtime and o/p ----
  endTime = micros();
  runTime = endTime - startTime;
  //Serial.println(runTime);  //This value is in micro seconds 1000uS == 1mS
  //We want the program loop to execute as quickly as possible so the robot is 
  //As responsive as it can be. Functions that take a long time should be called 
  //less frequently. 
  //---- End of program loop calc stuff ----
}
