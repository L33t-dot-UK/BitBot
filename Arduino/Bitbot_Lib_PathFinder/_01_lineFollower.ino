/*
 * Simple line following algorithm for the 4Tronix Bit:Bot
 * Author David Bradshaw 2018
 */

void followLine()
{
    boolean isLeftLine = detectLine(0);  //Left line detector
    boolean isRightLine = detectLine(1); //Right line detector

    if(isLeftLine == true && isRightLine == true)
    {
        //both sensors can see a line
        setColourRight(32,0,0);
        setColourLeft(32,0,0);
        while (isLeftLine == true && isRightLine == true)
        {
            isLeftLine = detectLine(0);  //Left line detector
            isRightLine = detectLine(1); //Right line detector
            backwards(125);
        }
        delay(350); //carry on going backwards for 350mS
        forwards(0); //Stop bitbot
    }   
    if (isLeftLine == true && isRightLine == false)
    {
        //Line on left hand side
        setColourRight(0,32,0);
        setColourLeft(32,0,0);
        while (isLeftLine == true && isRightLine == false)
        {
            isLeftLine = detectLine(0);  //Left line detector
            isRightLine = detectLine(1); //Right line detector
            left(50);
            delay(50);
        }
        forwards(0);
    }
    else if (isLeftLine == false && isRightLine == true)
    {
        //line on right hand side
        setColourRight(32,0,0);
        setColourLeft(0,32,0);
        while (isLeftLine == false && isRightLine == true)
        {
            isLeftLine = detectLine(0);  //Left line detector
            isRightLine = detectLine(1); //Right line detector
            right(50);
            delay(50);
        }
        forwards(0);
    }
    else if (isLeftLine == false && isRightLine == false)
    {
        //no line detected
        setColourRight(0,32,0);
        setColourLeft(0,32,0);
        forwards(50);
    }
}
