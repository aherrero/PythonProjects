#!/usr/bin/python
import RPi.GPIO as GPI
import time

print 'start gpio raspberry'
 
GPIO.setmode(GPIO.BCM)
RED_LED = 23
GPIO.setup(RED_LED, GPIO.OUT)
 
while True:
    GPIO.output(RED_LED, False)
    time.sleep(1)
    GPIO.output(RED_LED, True)
    time.sleep(1)
