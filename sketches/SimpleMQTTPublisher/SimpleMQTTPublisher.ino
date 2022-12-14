/*
  SimpleMQTTClient.ino
  The purpose of this exemple is to illustrate a simple handling of MQTT and Wifi connection.
  Once it connects successfully to a Wifi network and a MQTT broker, it subscribe to a topic and send a message to it.
  It will also send a message delayed 5 seconds later.
*/

#include "EspMQTTClient.h"

EspMQTTClient client(
  "Vodafone-DC65",
  "4TMFPgGBrpdRhhaP",
  "192.168.0.218",  // MQTT Broker server ip
  "pi",             // MQTT usermame
  "raspi",          // MQTT password for username
  "Esp8266",        // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);

void setup()
{
  Serial.begin(9600);

  // Optional functionalities of EspMQTTClient
  client.enableDebuggingMessages(); // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater(); // Enable the web updater. User and password default to values of MQTTUsername and MQTTPassword. These can be overridded with enableHTTPWebUpdater("user", "password").
  client.enableOTA(); // Enable OTA (Over The Air) updates. Password defaults to MQTTPassword. Port is the default OTA port. Can be overridden with enableOTA("password", port).
  // client.enableLastWillMessage("TestClient/lastwill", "I am going offline");  // You can activate the retain flag by setting the third parameter to true
}

// This function is called once everything is connected (Wifi and MQTT)
// WARNING : YOU MUST IMPLEMENT IT IF YOU USE EspMQTTClient
void onConnectionEstablished()
{
  Serial.println("Connection established!");
  // Subscribe to "mytopic/test" and display received message to Serial
  //client.subscribe("u3/rooms/kitchen/sensors/moisture", [](const String & payload) {
  //  Serial.println(payload);
  //});

  // Publish a message to "mytopic/test"
  client.publish("u3/rooms/kitchen/sensors/moisture", "This is a message"); // You can activate the retain flag by setting the third parameter to true

  // Execute delayed instructions
  client.executeDelayed(5 * 1000, []() {
    client.publish("u3/rooms/kitchen/sensors/humidity", "This is a message sent 5 seconds later");
  });
}

void loop()
{
  client.loop();
}
