/*
 * Shows how to use the NewPing library with HC-SR04
 * Author David Bradshaw 2018
 */

#include <NewPing.h>
NewPing sonar(15, 15, 400);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  delay(50);                      // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  unsigned int uS = sonar.ping(); // Send ping, get ping time in microseconds (uS).
  Serial.print("Ping: ");
  Serial.print(uS / US_ROUNDTRIP_CM); // Convert ping time to distance and print result (0 = outside set distance range, no ping echo)
  Serial.println("cm");
}
