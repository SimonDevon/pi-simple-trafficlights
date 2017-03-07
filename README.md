# pi-simple-trafficlights
Simple Traffic light controller written in Python 3 for the Raspberry Pi

The program uses the following physical pins:

Traffic Lights:
- Red LED: 35
- Yellow LED: 33
- Green LED: 37

Padestrian Light:
- Green LED: 38

Padestrian button:
- Button: 11

The program waits for a button press and then cycles the traffic lights including turning on and the flashing the green padestrian indicator (I ran out of jumper wires to add the red padestrian light!) 
