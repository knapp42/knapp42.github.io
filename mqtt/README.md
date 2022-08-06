# Docker setup for MQTT Broker

Setup local instance of MQTT Broker utilizing `eclipse-mosquitto` image.

First step:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`docker pull eclipse-mosquitto:latest`

Second step:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run instance via `docker_run_mqtt.sh` Script.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Script will use bind mount to mount configurations.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When changing the port for docker run, make sure to expose the right port in the mosquitto.conf.

# Usage of MQTT Broker
- Broker is ready to subscribing and publishing.
- Topics are created "on the fly" when publishing, no explicit creation is necessary.
- Setup uses the minimalistic passwordfile authentication.
  - Creating new authorized users needs to be done in the container with `mosquitto_passwd -c <password file> <username>`.  A prompt will pop up to enter the password.
  - Include username with password in custom client to pass authorization.