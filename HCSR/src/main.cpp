#include <Arduino.h>
#include "Ultrasonic/Ultrasonic.h"

#define TRIG_PIN 7
#define ECHO_PIN 6

Ultrasonic sensor(TRIG_PIN, ECHO_PIN);

void setup() {
  Serial.begin(9600);
  Serial.println("HC-SR04 Sensor Started...");
}

void loop() {
  float distance = sensor.readDistanceCM();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(1000);
}
