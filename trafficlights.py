#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

YellowLed = 35
RedLed = 33
GreenLed = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedLed, GPIO.OUT)
GPIO.setup(YellowLed, GPIO.OUT)
GPIO.setup(GreenLed, GPIO.OUT)
GPIO.output(RedLed, GPIO.HIGH)
GPIO.output(YellowLed, GPIO.HIGH)
GPIO.output(GreenLed, GPIO.HIGH)

try:
        while True:
                #print ('GREEN light')
                GPIO.output(GreenLed, GPIO.LOW)
                time.sleep(1)

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
                
except KeyboardInterrupt:
	GPIO.output(RedLed, GPIO.HIGH)
	GPIO.output(YellowLed, GPIO.HIGH)
	GPIO.output(GreenLed, GPIO.HIGH)
	GPIO.cleanup()



