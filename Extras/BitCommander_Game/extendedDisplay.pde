import processing.serial.*;

Serial mySerial;

int score = 0;
int ticks = 0;
int maxTicks = 0;
String incomingData = null;
int CR = 10; //Carage return

void setup()
{
  size(400,200);
  String myPort = Serial.list() [2]; //change this for your serial port
                                    //this is comm port 5 for me not sure why!!!! 
                                    //remember the display will only transmit serial data when a game is in progress!!!!
  mySerial = new Serial(this, myPort, 115200);
  PFont f = createFont("Georgia", 64);
  textFont(f);
  textSize(32);
  text("Game Not Started", 0, 50);
}

void draw()
{


  
  while(mySerial.available() > 0)
  {
    incomingData = mySerial.readStringUntil(CR);
    
    if (incomingData != null) //Serial port has data on it lets process it
    {
      println(incomingData);
      background(0); //update background
      String[] data = split(incomingData, ',');
      Double timeLeft = 0.0d;
      Double a = 0.0d;
      Double b = 0.0d;
      
      try
      {
        data[2] = data[2].replaceAll("\"","3");
        a = Double.parseDouble(data[2]);
        b = Double.parseDouble(data[1]);
        timeLeft = (a - b);
       
      }
      catch (Exception e)
      {
        println(e);
      }
      
      timeLeft = (timeLeft * 20) / 1000;
      
      text("Score", 0, 50);
      text("Time Left", 200, 50);
      text(data[0], 25, 100);
      text(Double.toString(timeLeft), 220, 100);
    }
  }
  
}