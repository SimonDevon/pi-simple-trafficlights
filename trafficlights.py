#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Pin header IDs for LEDs and button
YellowLed = 35
RedLed = 33
GreenLed = 37
button = 11

# Set up LEDs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedLed, GPIO.OUT)
GPIO.setup(YellowLed, GPIO.OUT)
GPIO.setup(GreenLed, GPIO.OUT)
GPIO.output(RedLed, GPIO.HIGH)
GPIO.output(YellowLed, GPIO.HIGH)
GPIO.output(GreenLed, GPIO.HIGH)

# Set up button
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def cycleLights ():
        print ('GREEN off, AMBER on')
        GPIO.output(GreenLed, GPIO.HIGH)
        GPIO.output(YellowLed, GPIO.LOW)
        time.sleep(1)

        print ('AMBER off, RED on')
        GPIO.output(YellowLed, GPIO.HIGH)
        GPIO.output(RedLed, GPIO.LOW)
        time.sleep(5)

        print ('AMBER and RED on')
        GPIO.output(YellowLed, GPIO.LOW)
        time.sleep(1.5)

        print ('AMBER and RED off, GREEN on')
        GPIO.output(RedLed, GPIO.HIGH)
        GPIO.output(YellowLed, GPIO.HIGH)
        GPIO.output(GreenLed, GPIO.LOW)
        time.sleep(4)
        return

try:
        while True:
                ButtonPress = False
                # Lights start with the green light on
                GPIO.output(GreenLed, GPIO.LOW)
                time.sleep(1)

                # Wait until button is presses
                print ('Waiting for button press')
                while not ButtonPress:
                        # Check every 2 seconds for a press
                        print ('Waiting for a button press...')
                        time.sleep(1)
                        ButtonPress = GPIO.input(button)

                print ('Button press detected')
                cycleLights()
                        
                
                
except KeyboardInterrupt:
	GPIO.output(RedLed, GPIO.HIGH)
	GPIO.output(YellowLed, GPIO.HIGH)
	GPIO.output(GreenLed, GPIO.HIGH)
	GPIO.cleanup()



